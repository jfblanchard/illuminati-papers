# Prompts — one-line log

Convention: timestamped + sequenced filenames; update this index whenever a prompt
is created or run so we always know which prompt drove which agent/batch.

- **2026-10-18 (rev B) — MAXIMUM-RATE parallel burn.** Illuminati main volume Phase 3.
  6 agents, disjoint full-book split (all 404 un-piloted pages, 25–428):
  A=25–92, B=93–160, C=161–228, D=229–296, E=297–364, F=365–428.
  Redesigned for max token-burn: each agent gets a large range so it never runs dry;
  the Claude session cap is the stopper, not page count. Fire as many agents in
  parallel as you want (24 cores). Built from `_template_maxrate.md`.
  Run: `claude -p "$(cat prompts/prompt-2026-10-18-<LETTER>.md)"` per agent (own terminal).
  Pilot pages (5,7,23–24) already corrected in `..._eval_sample.md`; merge all agent
  logs at end.

- **2026-10-18 (rev A, superseded)** — 3-agent slices A=25–64, B=65–104, C=105–144.
  Replaced by rev B above for max burn; ranges folded into the full-book split.
