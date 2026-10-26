#!/usr/bin/env python3
"""Build README.md from data/papers.yaml.

Usage: python3 scripts/build_readme.py
Reads data/papers.yaml, renders the awesome list grouped by
pluralism mode x research method, writes README.md.
"""
import pathlib
import yaml
from datetime import date

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "papers.yaml"
OUT = ROOT / "README.md"

MODES = [
    ("overton", "Overton Pluralism",
     "The model presents the full range of reasonable perspectives on contested questions without endorsing one."),
    ("steerable", "Steerable Pluralism",
     "The model adapts its behavior to a specified principal's values, persona, or preferences on demand."),
    ("distributional", "Distributional Pluralism",
     "The model's outputs across a population match the distribution of human views instead of collapsing to a single answer."),
    ("all", "Cross-cutting (all modes)",
     "Frameworks, methods, and resources that span or combine the three modes."),
]

METHODS = [
    ("empirical", "Empirical",
     "Measurement, audits, benchmarks used as instruments, human-subject and observational studies of existing models. No novel alignment artifact is proposed."),
    ("design_science", "Design science",
     "Novel artifacts: algorithms, training methods, decoding strategies, frameworks, and dataset/benchmark-as-artifact contributions, each with evaluation."),
]

KIND_TAG = {"dataset": "dataset", "benchmark": "benchmark"}


def entry_line(e):
    title = e["title"]
    url = e.get("url")
    head = f"**[{title}]({url})**" if url else f"**{title}**"
    meta = []
    if e.get("venue"):
        meta.append(e["venue"])
    if e.get("year"):
        meta.append(str(e["year"]))
    if e.get("kind") in KIND_TAG:
        meta.append(f"`{KIND_TAG[e['kind']]}`")
    if e.get("track") == "journals":
        meta.append("journal track")
    line = f"- {head}"
    if meta:
        line += " — " + ", ".join(meta)
    if e.get("blurb"):
        line += f". {e['blurb']}"
    if not url:
        line += " *(link pending)*"
    return line


def main():
    entries = yaml.safe_load(DATA.read_text())
    total = len(entries)
    with_links = sum(1 for e in entries if e.get("url"))
    low_conf = [e for e in entries if e.get("conf") in ("low", "medium") and e.get("method") != "na"]

    L = []
    L.append("# Awesome Pluralistic AI Alignment")
    L.append("")
    L.append("A curated reading list on **pluralistic AI alignment** — organized by pluralism mode "
             "× research method, with coverage spanning top CS conferences and (as the field grows) "
             "top ethics, behavioral, and IS journals.")
    L.append("")
    L.append("> Why this list: alignment training (RLHF, DPO) is widely observed to compress output "
             "diversity — a regression to the mean. Pluralistic alignment is the literature's main "
             "response: methods that preserve or restore variance across values, cultures, and viewpoints. "
             "This list tracks that literature by *mode* and by *method* so both builders and empiricists "
             "can find their half.")
    L.append("")
    L.append("## The taxonomy")
    L.append("")
    L.append("Following the roadmap that defined the field (Sorensen et al., ICML 2024 — see Position papers & surveys), "
             "pluralistic alignment comes in three modes:")
    L.append("")
    for _, name, desc in MODES[:3]:
        L.append(f"- **{name}** — {desc}")
    L.append("")
    L.append("Within each mode, entries are split by research method:")
    L.append("")
    for _, name, desc in METHODS:
        L.append(f"- **{name}** — {desc}")
    L.append("")
    L.append("## Venue scope")
    L.append("")
    L.append("| Method | Track | Venues covered |")
    L.append("|---|---|---|")
    L.append("| Empirical | Top ethics / behavioral / IS journals | "
             "IS: MIS Quarterly, Information Systems Research, JAIS, EJIS, JMIS · "
             "Ethics: Journal of Business Ethics, Ethics and Information Technology, AI & Society, Philosophy & Technology · "
             "Behavioral: OBHDP, Computers in Human Behavior, Management Science |")
    L.append("| Design science | Top CS conferences | "
             "NeurIPS, ICML, ICLR, AAAI, ACL, EMNLP, NAACL, COLM, FAccT, AIES, CHI |")
    L.append("")
    L.append("_Note: the literature is currently CS-conference heavy; the journal track is intentionally "
             "watched by the updater agent so IS/ethics/behavioral work gets picked up as it appears._")
    L.append("")
    L.append("## Contents")
    L.append("")
    for slug, name, _ in MODES:
        anchor = name.lower().replace(" ", "-").replace("(", "").replace(")", "")
        L.append(f"- [{name}](#{anchor})")
    L.append("- [Position papers & surveys](#position-papers--surveys)")
    L.append("- [Maintenance](#maintenance)")
    L.append("")

    for slug, name, desc in MODES:
        L.append(f"## {name}")
        L.append("")
        L.append(f"_{desc}_")
        L.append("")
        mode_entries = [e for e in entries if slug in e.get("modes", [])
                        and e.get("kind") not in ("survey", "position")]
        for mslug, mname, mdesc in METHODS:
            L.append(f"### {mname}")
            L.append("")
            L.append(f"_{mdesc}_")
            L.append("")
            sub = [e for e in mode_entries if e.get("method") == mslug]
            sub.sort(key=lambda e: (e.get("year") or 0, e["title"]))
            if not sub:
                L.append("_Nothing here yet — the updater agent is watching for it._")
            else:
                L.extend(entry_line(e) for e in sub)
            L.append("")

    L.append("## Position papers & surveys")
    L.append("")
    L.append("_Foundational framings and surveys of pluralistic (and adjacent) alignment._")
    L.append("")
    surv = [e for e in entries if e.get("kind") in ("survey", "position")]
    surv.sort(key=lambda e: (e.get("year") or 0, e["title"]))
    L.extend(entry_line(e) for e in surv)
    L.append("")
    L.append("## Maintenance")
    L.append("")
    L.append("This list is kept current by an **autonomous updater agent on a bi-weekly cadence**:")
    L.append("")
    L.append("- Queries the arXiv API for new pluralistic-alignment work (all modes, both methods).")
    L.append("- Diffs the upstream community list for additions worth porting.")
    L.append("- Hunts the journal track (IS / ethics / behavioral venues) via scholarly APIs.")
    L.append("- Classifies each candidate by mode × method, resolves canonical paper links, and rebuilds this README from `data/papers.yaml` (the source of truth).")
    L.append("- Commits changes to git; every run is logged under `agents/runs/`.")
    L.append("")
    L.append(f"_Stats: {total} entries · {with_links} with resolved links · "
             f"{len(low_conf)} seed classifications flagged for verification · last built {date.today().isoformat()}._")
    L.append("")
    L.append("Contributions welcome — see [CONTRIBUTING.md](CONTRIBUTING.md).")
    L.append("")
    OUT.write_text("\n".join(L))
    print(f"wrote {OUT} ({total} entries)")


if __name__ == "__main__":
    main()
