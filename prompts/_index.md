# Prompts — one-line log

Convention: timestamped + sequenced filenames; update this index whenever a prompt
is created or run so we always know which prompt drove which agent/batch.

- **2026-10-18** — Claude Code burn, Illuminati main volume Phase 3 (Parallel).
  3 agents, disjoint PDF page ranges: A=25–64, B=65–104, C=105–144.
  Builds `einige_originalschriften_1787_corrected.txt` from PDF page 25 up.
  Pilot pages (5,7,23–24) already corrected in `..._eval_sample.md`; merge at
  end. Run via `claude -p "$(cat prompts/prompt-2026-10-18-<LETTER>.md)"`.
