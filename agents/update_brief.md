# Updater Agent Brief — Awesome Pluralistic AI Alignment

You run on a bi-weekly cadence (cron). Your job: keep `data/papers.yaml` current,
resolve missing canonical links, rebuild `README.md`, commit, and report.

## Repo layout

- `data/papers.yaml` — source of truth. One entry per paper/dataset/benchmark/survey.
- `scripts/build_readme.py` — regenerates `README.md` from the YAML. Always run after edits.
- `agents/runs/YYYY-MM-DD.md` — your run log. Write one every run.
- `README.md` — generated; never edit by hand.

## Entry schema (keep it exact)

```yaml
- title: "Exact Paper Title"
  authors: ["First Author", "Second Author"]   # full author list, or omit until resolved
  venue: "NeurIPS"            # or null if unknown/preprint
  year: 2025                 # or null if unknown
  vhint: arxiv               # where first seen: arxiv|aclanthology|openreview|neurips|aaai|acm|ieee|mit|city|...
  url: "https://..."         # canonical paper URL, or null until resolved
  modes: [overton]           # any of: overton, steerable, distributional, all
  method: empirical          # empirical | design_science | na (for surveys/position pieces)
  track: cs                  # cs | journals
  kind: method               # method | dataset | benchmark | survey | position
  blurb: "One neutral, factual sentence on what it contributes."
  conf: high                 # your confidence in the classification: high|medium|low
```

## Classification rubric

**Modes** (Sorensen et al., ICML 2024):
- `overton` — presents the range of reasonable views without endorsing one.
- `steerable` — adapts to a specified principal's values/persona/preferences.
- `distributional` — matches the distribution of views across a population.
- `all` — spans or combines modes. An entry may carry multiple modes.

**Method:**
- `empirical` — measures, audits, or explains existing models/phenomena; human-subject or
  observational studies; benchmarks used as measurement instruments. Proposes NO novel alignment artifact.
- `design_science` — proposes and evaluates a NOVEL artifact: algorithm, training method,
  decoding strategy, framework, or dataset/benchmark-as-artifact.
- `na` — surveys and position papers.
- When unsure, pick your best call and set `conf: low` so a human can review.

**Track:**
- `cs` — top CS conferences, workshops, and preprints (NeurIPS, ICML, ICLR, AAAI, ACL, EMNLP,
  NAACL, COLM, FAccT, AIES, CHI, arXiv).
- `journals` — top IS (MISQ, ISR, JAIS, EJIS, JMIS), ethics (JBE, Ethics and Information
  Technology, AI & Society, Philosophy & Technology), behavioral (OBHDP, Computers in Human
  Behavior, Management Science) journals.

## Each run, in order

1. **Read** this brief, `data/papers.yaml`, and the most recent run log in `agents/runs/`.
2. **Discover candidates** (last ~14 days, plus anything missed):
   a. arXiv API (`http://export.arxiv.org/api/query`) — search queries like
      `all:"pluralistic alignment"`, `all:"overton pluralism"`, `all:"distributional alignment"`,
      `all:"steerable alignment"`, `all:"value pluralism" LLM`. Sort by submitted date, filter to the window.
   b. Upstream community list — check `https://github.com/anudeex/Awesome-Pluralistic-Alignment`
      for new commits since your last run; port worthwhile additions (re-classify into our schema, don't copy blindly).
   c. Journal track — query Semantic Scholar / Crossref for the journal venues above with
      keywords (pluralistic alignment, value pluralism, algorithmic homogenization, AI values).
      This track is sparse; even zero hits is a valid result — say so.
3. **Deduplicate** — normalize titles (lowercase, strip punctuation) and compare against existing
   entries AND against candidates within this run. Never add the same paper twice.
4. **Backfill** — for entries with `url: null`, resolve the canonical URL: arXiv API exact-title
   search first, then ACL Anthology / publisher pages. Fill `venue`/`year` from the API record.
   Only set a URL you actually verified — never guess or construct one.
   Also resolve missing `authors` lists (run `agents/fetch_authors.py` — it batches arXiv,
   Crossref, and OpenReview lookups and only fills empty fields; entries it cannot resolve
   stay blank, never guessed). Every NEW entry must get its author list resolved in the same run.
5. **Classify** each new candidate per the rubric above; write a one-line neutral blurb.
6. **Append** to `data/papers.yaml` (keep the section comments tidy), then run
   `python3 scripts/build_readme.py` and confirm it succeeds.
7. **Commit**: `git add -A && git commit -m "updater: <date> — <n> new, <m> links resolved"`.
8. **Write** `agents/runs/YYYY-MM-DD.md`: counts (new entries, links resolved, per-mode/per-method),
   notable additions (2–4 with one-line why), journal-track hits or explicit zero, and anything
   flagged `conf: low` for human review.
9. **Report back to the user**: brief summary — new entries count, the 2–3 most notable papers,
   journal-track status, and any flags. Keep it short.
   **Always end the report with the manual-push reminder**: read `agents/last_github_sync.txt`,
   count local commits since that sync date (`git log --since=<date> --oneline | wc -l`), and add
   one line: "Reminder: the public GitHub repo was last synced <date> and is <N> commits behind —
   it stays stale until you ask for a manual sync." The local repo has no git remote; do NOT
   attempt to push.

## Guardrails

- Never delete entries. Corrections go through re-classification with a note in the run log.
- Never invent URLs, DOIs, venues, or years. Unverified = null.
- Cap additions at ~25 per run; queue the rest for next time (note it in the run log).
- Don't re-classify `conf: high` seed entries without concrete evidence; note disputes in the run log.
- Blurbs stay neutral and factual — no hype, no dismissiveness.
- If arXiv or an API is down, do the rest of the run and note the gap; don't fake it.
