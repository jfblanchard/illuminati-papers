# Illuminati Translation Project — Nachtrag Phase 3 correction: continue from PDF p.74

You are the coordinator for the Illuminati Translation Project. Continue the Phase 3
(human-grade correction) pass on the **Nachtrag** — the 1787 Bavarian Illuminati
primary-source volume, "die Illuminatensekte überhaupt, sonderbar aber den Stifter
derselben Adam Weishaupt." OCR in-hand; your job is image-vs-OCR correction, page by
page, starting at PDF page 74.

## Workspace / current state
- Repo: `/mnt/data/projects/Research/illuminati_translation_project`
- Source PDF: `scans/nachtrag_1787/nachtragvonweite121duke_0.pdf` (436 pages)
- Raw OCR (Phase 2, unedited German/Fraktur): `transcriptions/nachtrag_1787/nachtrag_1787_transcription.txt`
- Corrected text (Phase 3, append here): `transcriptions/nachtrag_1787/nachtrag_1787_corrected.txt`
- Correction log (append dated entries here): `transcriptions/nachtrag_1787/nachtrag_1787_correction_log.md`
- **Correction is COMPLETE through PDF page 73.** Start at **PDF page 74**.
- Todo: `todo.md` under "▶ START HERE" — update its progress numbers as you go.

## The proven workflow (unchanged since page 1 — follow exactly)
For each PDF page from 74 onward:
1. Render the page to PNG: `pdftoppm -f <N> -l <N> -r 300 -png scans/nachtrag_1787/nachtragvonweite121duke_0.pdf /tmp/claude-1000/nachtrag_page_<N>`
   (run from the repo root; write PNGs to a scratch dir, NOT the repo).
2. **Read the rendered image directly** (this is the source of truth — always compare
   against the scan, never "fix" OCR without seeing the image).
3. Compare the image against the corresponding text in
   `nachtrag_1787_transcription.txt` AND the tail of `nachtrag_1787_corrected.txt`
   (so you see where the last session left off and match its style).
4. Append the corrected page's text to `nachtrag_1787_corrected.txt` (preserving the
   page-boundary markers the file already uses), and add a dated entry to
   `nachtrag_1787_correction_log.md` describing every correction you made and any
   uncertain reading you flagged.
5. WORK THROUGH PAGES CONTINUOUSLY in this session — don't stop after a handful.
   Commit per batch (see below). Update `todo.md` progress numbers as you go.

## Starting context — PDF p.73→74 boundary (from the previous session's log)
- p.73 ends mid-sentence: "Wenn's ſo fort geht, und noch aͤrger" — a catchword
  fragment "an=" was visible at the bottom of p.73, likely previewing "anwaͤchſt"
  (or similar). **Confirm against the p.74 image** and resolve the catchword.
- Still within letter 13 (Spartacus/Weishaupt's letter), which includes a "Notanda"
  numbered list (items 1-4, PDF p.72-73).
- p.73's notable finding: "▢▢ zu errichten" — strongest support yet for the
  "▢▢ = Loge (lodge)" hypothesis ("...auffodere, ▢▢ zu errichten" = "...urge him to
  establish a ▢▢/lodge"). Keep confidence HIGH but still flagged, per house standard.

## Recurring OCR patterns to apply (established on pages 1-73)
- **"☉"** (circle-with-dot) = "der Orden" (the Order). OCR mangles it as `(`, `Q`,
  `O`, or drops it. Occurs also MID-WORD (e.g. "☉sſachen" = "Ordensſachen").
- **"▢"/"▢▢"** (hollow square) = hypothesized "Loge" (lodge) — high confidence now,
  keep flagged.
- Roman-numeral-looking "III." = misread of "Ill." (Illuminatus).
- **f/ſ (long-s) confusion** is the single most common OCR error — fix liberally,
  don't itemize individually unless something else is also wrong on the word.
- **Redacted names via dashes** (e.g. "V===", "S==") are a real printed convention —
  8+ catalogued; do NOT guess who they are.
- **Diagrams** (recruitment pyramid p.40, hierarchy tree p.68) → OCR garbage; describe
  them in prose in the corrected text rather than transcribing noise.
- **French quotes** (Machiavelli p.59, Raynal p.65-66) → transcribe as legible, flag
  as not verified against a critical edition.
- **Catchword + page-number noise** between page markers (short fragment + bare
  number) is almost always catchword + page number, NOT missing text — verify against
  both adjacent page images only if it could plausibly be content.
- Letter header abbreviations ("Sp. [X]. S. d.") use single-letter recipient codes
  ("C." = Celsus). Others unresolved — flag, don't guess.

## Guardrails
- **NEVER edit the raw OCR** (`nachtrag_1787_transcription.txt`) — corrections go only
  in `..._corrected.txt` + the correction log.
- No `sed -i` on the corrected file.
- Every **uncertain** reading gets an explicit flag in the correction log (image-based
  correction is expensive/redone-hard; commentary is cheap to expand later — flag in
  prose, don't silently guess).
- Do NOT touch the other documents' files or the git history.
- Housekeeping: if Bash fails with ENOSPC/disk-full on scratch, clear `*.png` from the
  session scratch dir and retry — it's accumulated page renders, not a real error.

## Deliverables
- Extend `nachtrag_1787_corrected.txt` through a meaningful run of pages past p.74
  (as many as you can complete this session — this is a burn-the-credits session).
- Append dated corrections to `nachtrag_1787_correction_log.md`.
- Update `todo.md` progress numbers + `devnotes.md` briefly.
- **Commit per batch** in house style, e.g.:
  `correct: Nachtrag pp. 74-89 (letter 13 cont., Notanda; p73 catchword confirmed)`
- WORK TO COMPLETION: keep going until you hit a natural stopping point (page-batch
  boundary, a genuinely hard page you should flag rather than guess, or the session
  budget), then report pages covered + any flagged uncertainties.