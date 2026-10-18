# Illuminati Main Volume — Sequential Block-Finish Prompt (resume-aware)
# One agent per block, runs the WHOLE block to completion.

**Document:** *Einige Originalschriften des Illuminatenordens* (1787) — Zwack house-search seizure.

## Your assigned block
Correct **physical PDF pages 327–364** (inclusive) of the main volume. This is a SEQUENTIAL block-finish pass: you are the sole agent on this range. **Complete the ENTIRE block**, not a slice of it — go page-by-page from whichever page is not yet corrected to `364`.

## Resume behavior (IMPORTANT)
This block may have been partially corrected in an earlier session and cut off by a session-limit. 
1. **Before starting, scan the corrected output file for which pages in 327–364 are already done** (look for `--- PDF page NNN ---` markers). 
2. **Begin at the first page in your range NOT yet present**, and continue to `364`. 
3. Never redo a page that already has a correct marker. Never skip a page.

## Key files (absolute paths)
- **Authoritative scan image:** `/mnt/data/projects/Research/illuminati_translation_project/scans/einige_originalschriften_1787/einigeoriginalsc01duke_0.pdf`
- **Raw OCR (what you fix) — Phase 2 output:** `/mnt/data/projects/Research/illuminati_translation_project/transcriptions/einige_originalschriften_1787/einige_originalschriften_1787_transcription.txt`
- **Pilot sample (method + corrected pp. 5,7,23-24):** `/mnt/data/projects/Research/illuminati_translation_project/transcriptions/einige_originalschriften_1787/einige_originalschriften_1787_eval_sample.md`

## Working files you CREATE/APPEND (never overwrite raw transcription/eval sample)
- **Corrected German (append only):** `transcriptions/einige_originalschriften_1787/einige_originalschriften_1787_corrected.txt`
  `cat >>` each page under a `--- PDF page NNN ---` marker (physical PDF page number). Pages 25-384 partly corrected already; append your pages.
- **Per-agent correction log (append):** `transcriptions/einige_originalschriften_1787/einige_originalschriften_1787_correction_log_guardian_327_364.md`
  One line per content-level correction. f/ſ fix silent; content misreads/drops itemized in full.

## Established domain conventions (same as Nachtrag / earlier main-volume passes)
- **☉** (circle-dot) = "der Orden"; OCR mangles as `(`/`Q`/`O`/drops. Restore.
- **▢ / ▢▢** (hollow square) = "Loge"/"Logen". Keep as printed.
- **"III."** is nearly always a misread of **"Ill."** (Illuminatus).
- **f/ſ** confusion = most common OCR error — fix silently.
- **Redacted names via dashes/equals** ("V===", "S==") = real printed convention — preserve, don't guess.
- **"x."-dot notation** ("M.x.x.", "R.x.") = Masonic raised-dot abbreviation (∴). Keep as printed.
- **Diagrams** → prose description, not garbage transcription.
- **Foreign-language quotations** — transcribe as legible, flag unverified.
- **Page-end catchwords & signature marks are NOT text** — exclude.
- **Silent whole-word omission is a real OCR failure** — watch.
- Flag genuinely uncertain readings as `[illegible]` — NEVER fabricate words or identities.

## Working method (block to completion)
1. Determine first not-yet-corrected page in 327–364 (via existing markers in `corrected.txt`).
2. Render scan: `pdftoppm -f N -l N -r 300 -png <pdf> /tmp/mv_g_N`
3. Read rendered image (vision); compare to raw OCR; correct; append under marker; log changes.
4. Commit every ~15-25 pages or a coherent slice, never accumulate: 
   `git add -A && git commit -m "correct main volume pp. N-M (Phase 3 sequential block 327-364, guardian)"`
   Work in repo root `/mnt/data/projects/Research/illuminati_translation_project`.
5. **Keep going to `364`** even if your session is cut off mid-block — commit before any pause; a relaunch/next-session will resume from the first uncorrected page.
6. When `364` is reached, update `todo.md` (list which pages in your block you covered), then report: pages corrected this run, total corrections logged, illegible flags, final commit hash(es).

## Stop conditions
- **ENOSPC / disk-full on /tmp:** clear `/tmp/mv_g_*.png`, not a real error.
- **Low-res scan (~540px):** degraded n/u/a/i — check crop before "fixing".
- Do NOT touch the Nachtrag/Anhang documents or the raw transcription file.
- If session cut off mid-block, you have committed work — that is a SUCCESSFUL partial stop; the next session resumes from the first uncorrected page in 327–364.

## Definition of done
Every page `327` through `364` has a correct `--- PDF page NNN ---` marker in `corrected.txt`, in order, no gaps; per-agent log written; commits pushed; `todo.md` updated. Until every page in the block is corrected, you are NOT done.