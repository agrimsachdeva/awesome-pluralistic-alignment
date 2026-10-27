#!/usr/bin/env python3
"""Backfill authors (and missing venue/year) in data/papers.yaml.

Sources, in order: arXiv API (batch by ID), Crossref (by DOI, then by title),
OpenReview API (by forum id), Semantic Scholar (title search, fallback).
Only fills fields that are currently missing. Edits the YAML at text level to
preserve comments/formatting. Never invents data: unmatched entries stay null.
"""
import json
import pathlib
import re
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from difflib import SequenceMatcher

import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "papers.yaml"
UA = {"User-Agent": "awesome-pluralistic-alignment-updater/1.0 (mailto:agrim@arizona.edu)"}


def get(url, timeout=30):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()


def norm(t):
    return re.sub(r"[^a-z0-9]+", " ", (t or "").lower()).strip()


def ratio(a, b):
    return SequenceMatcher(None, norm(a), norm(b)).ratio()


text = DATA.read_text()
entries = yaml.safe_load(text)
found = {}  # idx -> {"authors": [...], "venue": str, "year": int}


def put(i, **kw):
    d = found.setdefault(i, {})
    for k, v in kw.items():
        if v:
            d[k] = v


# ---- 1. arXiv batch ----
arxiv_ids = {}
for i, e in enumerate(entries):
    m = re.search(r"arxiv\.org/abs/(\d{4}\.\d{4,5})", e.get("url") or "")
    if m:
        arxiv_ids[m.group(1)] = i
ids = sorted(arxiv_ids)
NS = {"a": "http://www.w3.org/2005/Atom", "x": "http://arxiv.org/schemas/atom"}
for s in range(0, len(ids), 40):
    chunk = ids[s:s + 40]
    q = urllib.parse.urlencode({"id_list": ",".join(chunk), "max_results": len(chunk)})
    root = ET.fromstring(get(f"https://export.arxiv.org/api/query?{q}"))
    for ent in root.findall("a:entry", NS):
        aid = ent.findtext("a:id", "", NS).rstrip("/").split("/")[-1]
        aid = re.sub(r"v\d+$", "", aid)
        if aid not in arxiv_ids:
            continue
        i = arxiv_ids[aid]
        authors = [a.findtext("a:name", "", NS).strip() for a in ent.findall("a:author", NS)]
        pub = ent.findtext("a:published", "", NS)
        jref = ent.findtext("x:journal_ref", "", NS).strip()
        kw = {"authors": authors}
        if pub:
            kw["year"] = int(pub[:4])
        if jref and len(jref) <= 80:
            kw["venue"] = jref
        put(i, **kw)
    print(f"arxiv batch {s // 40 + 1}: {len(chunk)} ids", flush=True)
    time.sleep(3)

# ---- 2. Crossref by DOI ----
for i, e in enumerate(entries):
    if found.get(i, {}).get("authors"):
        continue
    m = re.search(r"doi\.org/(10\.\S+)$", e.get("url") or "")
    if not m:
        continue
    try:
        w = json.loads(get("https://api.crossref.org/works/" + urllib.parse.quote(m.group(1), safe="")))["message"]
        authors = [f"{a.get('given', '')} {a.get('family', '')}".strip() for a in w.get("author", [])]
        venue = (w.get("container-title") or [None])[0]
        yr = ((w.get("issued") or {}).get("date-parts") or [[None]])[0][0]
        put(i, authors=authors, venue=venue, year=yr)
    except Exception as ex:
        print(f"crossref doi failed idx {i}: {ex}", flush=True)
    time.sleep(1)

# ---- 3. OpenReview by forum id ----
for i, e in enumerate(entries):
    if found.get(i, {}).get("authors"):
        continue
    m = re.search(r"openreview\.net/forum\?id=([\w-]+)", e.get("url") or "")
    if not m:
        continue
    try:
        d = json.loads(get("https://api2.openreview.net/notes?forum=" + m.group(1)))
        notes = d.get("notes") or []
        if notes:
            c = notes[0].get("content") or {}

            def val(k):
                v = c.get(k)
                return v.get("value") if isinstance(v, dict) else v

            put(i, authors=val("authors"), venue=(val("venue") or notes[0].get("venue")))
    except Exception as ex:
        print(f"openreview failed idx {i}: {ex}", flush=True)
    time.sleep(1)

# ---- 4. Crossref by title (leftovers) ----
for i, e in enumerate(entries):
    if found.get(i, {}).get("authors"):
        continue
    try:
        q = urllib.parse.urlencode({"query.bibliographic": e["title"], "rows": 3,
                                    "select": "title,author,container-title,issued"})
        items = json.loads(get("https://api.crossref.org/works?" + q))["message"]["items"]
        best, bs = None, 0.0
        for it in items:
            r = ratio(e["title"], (it.get("title") or [""])[0])
            if r > bs:
                best, bs = it, r
        if best is not None and bs >= 0.88:
            authors = [f"{a.get('given', '')} {a.get('family', '')}".strip() for a in best.get("author", [])]
            venue = (best.get("container-title") or [None])[0]
            yr = ((best.get("issued") or {}).get("date-parts") or [[None]])[0][0]
            put(i, authors=authors, venue=venue, year=yr)
    except Exception as ex:
        print(f"crossref title failed idx {i}: {ex}", flush=True)
    time.sleep(1)

# ---- 5. Semantic Scholar by title (fallback; stop on 429) ----
for i, e in enumerate(entries):
    if found.get(i, {}).get("authors"):
        continue
    try:
        q = urllib.parse.urlencode({"query": e["title"], "fields": "title,authors,venue,year", "limit": 3})
        d = json.loads(get("https://api.semanticscholar.org/graph/v1/paper/search?" + q))
        best, bs = None, 0.0
        for p in d.get("data") or []:
            r = ratio(e["title"], p.get("title"))
            if r > bs:
                best, bs = p, r
        if best is not None and bs >= 0.88:
            put(i, authors=[a["name"] for a in best.get("authors") or []],
                venue=best.get("venue"), year=best.get("year"))
    except urllib.error.HTTPError as ex:
        print(f"s2 http {ex.code} at idx {i} — stopping s2 pass", flush=True)
        if ex.code == 429:
            break
    except Exception as ex:
        print(f"s2 failed idx {i}: {ex}", flush=True)
    time.sleep(2)

# ---- apply at text level ----
lines = text.split("\n")
starts = [n for n, ln in enumerate(lines) if ln.startswith("- title:")]
assert len(starts) == len(entries), (len(starts), len(entries))
starts.append(len(lines))
out = []
for i in range(len(entries)):
    block = lines[starts[i]:starts[i + 1]]
    f = found.get(i, {})
    e = entries[i]
    newblock = []
    for ln in block:
        if ln.startswith("- title:"):
            newblock.append(ln)
            if f.get("authors"):
                newblock.append("  authors: " + json.dumps(f["authors"], ensure_ascii=False))
            continue
        if ln.strip() == "venue: null" and (f.get("venue") or (e.get("url") or "").find("arxiv.org") >= 0):
            v = f.get("venue") or "arXiv"
            newblock.append("  venue: " + json.dumps(v, ensure_ascii=False))
            continue
        if ln.strip() == "year: null" and f.get("year"):
            newblock.append(f"  year: {f['year']}")
            continue
        newblock.append(ln)
    out.extend(newblock)
DATA.write_text("\n".join(out))

# ---- validate + report ----
es2 = yaml.safe_load(DATA.read_text())
print("total:", len(es2))
print("with authors:", sum(1 for e in es2 if e.get("authors")))
print("with venue:", sum(1 for e in es2 if e.get("venue")))
print("with year:", sum(1 for e in es2 if e.get("year")))
print("missing authors:")
for e in es2:
    if not e.get("authors"):
        print(" -", e["title"][:90])
