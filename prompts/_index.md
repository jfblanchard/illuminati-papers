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

- **2026-10-18 (rev B result) — 6-agent max-rate burn RAN and 429'd.** All 6
  launched 14:31, each hit `usage_limit_reached` (60-81 turns) by ~14:38 as 9
  concurrent sessions (3 interactive + 6 burn) drained the 5h window. Committed
  188 page-markers (pp. 25-66, 93-125, 161-186, 229-265, 297-326, 365-384);
  orphaned mid-commit work saved as `6596568`. Remaining uncorrected: 67-92,
  126-160, 187-228, 266-296, 327-364, 385-428 (0 pages each → 216 total).
  RESOLUTION: left 3 interactive threads to auto-resume at 5:10 (verified they
  self-continue); 6 headless agents stay dead (won't resurrect — `-p` one-shots).
  Commit seq-block prompts `seq-block-*.md` + `_seq_template.md` for a clean
  sequential re-arm if Jon wants to finish the 216 remaining pages later.

- **2026-10-24 (session burn) — parallel finish of the main volume, near the
  Claude session cap.** Started 10:35 with 61 pages uncorrected (348-364, 385-428).
  First launch (`gapfill-burn.md`) FAILED to write: ran headless WITHOUT
  `--dangerously-skip-permissions`, so it could read via vision but not write
  files/commit — exited clean having done nothing. RESCUE: relaunched 2 disjoint
  agents IN PARALLEL with `--dangerously-skip-permissions`:
    A = `seq-block-348-364.md` → COMPLETE, commit `a67be8d` (block 348-364 done)
    B = `seq-block-385-428.md` → still running, covering 399-428 tail
  Mid-run safety commit `606d13c` (pp. 348-396, 518 insertions) captured the
  interleaved work while both agents were mid-batch. Net result: present rose
  367 → 398+ ; remaining 399-428 (30pp) till B finishes. GOTCHA: concurrent
  append made corrected.txt page-order interleaved (A's 348-364 mixed with B's
  385-396); each page complete under its marker — needs a re-sort to ascending
  order once B is done. LAUNCH LESSON: headless `claude -p` burns MUST include
  `--dangerously-skip-permissions` or they silently can't write/commit.

