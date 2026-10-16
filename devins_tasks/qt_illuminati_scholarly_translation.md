# Illuminati Nachtrag — Phase 4 SCHOLARLY Translation (1787 German → English) — Devin + Sonnet

You are the scholarly translator for a 1787 Bavarian Illuminati document. This is the
**readable-pass** translation: natural modern English prose built from the already-corrected
German text. This is an accuracy-critical, citable scholarly record — translate what the text
SAYS, never soften, summarize, or invent.

**Repo (local, you are running in its root):** `/mnt/data/projects/Research/illuminati_translation_project`

## Your task (in one sentence)
Produce `translations/scholarly/nachtrag_1787_scholarly.md` — a scholarly/readable English
translation of the FULL corrected Nachtrag, PDF pages 5 through 436.

## Inputs (read these first)
1. **Source of truth (the German to translate):**
   `transcriptions/nachtrag_1787/nachtrag_1787_corrected.txt`
   This is the Phase-3 corrected German text. It contains `--- PDF page NNN ---` markers.
   Translate pages **5 through 436** — that is the whole document. (Pages 1-4 are cover/blank
   matter not in the digitized text.)
2. **The LITERAL pass (already done, pp.5-340) — use as a reference for consistency:**
   `translations/literal/nachtrag_1787_literal.md`
   This is a stiff, word-order-preserving first pass. Your job is the READABLE pass, but you
   should keep terminology, code names, and hard choices CONSISTENT with it. Where the literal
   pass solved a hard phrase, follow its lead unless it is clearly wrong.
3. **The translation context / glossary (READ THIS — it governs register and terms):**
   `translations/nachtrag_1787_translation_context.md`
4. **The model to match — the already-completed scholarly pass for the sibling document (Anhang):**
   `translations/scholarly/anhang_1787_scholarly.md`
   Read its "Methodology & status" header and a few pages. Match its register, its handling of
   page markers, and its formatting conventions.

## House conventions (non-negotiable — copied from the Anhang scholarly pass)
- **Page markers:** keep `--- page N ---` between pages, using the PDF page numbers from the
  corrected text (NOT the book's printed page numbers).
- **☉** (circle-with-dot) = "der Orden" (the Order). Keep the symbol as printed, exactly like the
  literal pass. Never translate it as "sun."
- **▢ / ▢▢** = "Loge"/"Logen" (lodge/lodges). Keep the symbol(s).
- **Redacted names** ("V===", "S==", "B.==", dash/equals-sign forms): preserve EXACTLY as printed.
  Never guess or resolve them.
- **"x."-dot notation** ("M.x.x.", "R.x."): Masonic raised-dot abbreviation. Keep as printed.
- **Latin and French passages:** leave in the original language, as the source does (these are
  direct quotations — Machiavelli, Raynal, Scripture pastiche — part of the document's texture).
- **Code names** (Spartacus, Philo, Celsus, Cato, Marius, etc.): keep the code names as-is.
- **Distinct voices:** the Nachtrag is a prosecution-style compilation — Weishaupt's own letters
  interleaved with hostile editorial footnotes. Where the editorial/footnote voice is clearly
  distinct from the letter-writer's, set it off (e.g. as a marked footnote/block quote) so the two
  voices stay visually separable, as the Anhang pass did for its footnote-writer.
- **Readable, not loose:** break up the original's long subordinate clauses where English demands
  it; update archaic diction; but add NOTHING, soften NOTHING, summarize NOTHING away. When a
  clause is genuinely ambiguous, translate the most literal defensible reading and flag it inline
  with `[?]` — never silently smooth it over.
- This is an AI-assisted first pass, **not** a final scholarly translation — say so in the header.

## Output format (match `translations/scholarly/anhang_1787_scholarly.md`)
Start the file with a `# ... — Scholarly Translation` title and a `## Methodology & status`
section matching that file's style, but stating: translated by Devin (Sonnet) on 2026-10-15/16,
directly from `transcriptions/nachtrag_1787/nachtrag_1787_corrected.txt`, informed by the literal
pass. Then the translated text with `--- page N ---` markers.

## Method — work in batches, commit as you go (IMPORTANT — do not lose work)
Translate in contiguous batches of ~20-30 pages. After each batch:
1. Append the translated batch to `translations/scholarly/nachtrag_1787_scholarly.md`.
2. Commit with a boring single-line message, e.g.:
   `git -c user.name="Devin" -c user.email="devin@local" commit -qm "scholarly translation: Nachtrag pp. 5-30"`
   (add only that one file by explicit path; never `git add -A`).
Committing per batch means if the session is interrupted, everything before the last commit is safe
and the next session resumes cleanly.

## Notes on the source text (from the correction pass — helps you translate)
- The Nachtrag is organized as per-correspondent "case files," not one continuous narrative:
  Spartacus's letters (pp.1-107) → Section II Philo's letters (pp.107-137) → Section III "Zween
  Briefe von Epictet" (pp.137-142) → Section IV "Zween Briefe von Hannibal" (pp.142-148) → Section
  V one letter from Marius to Hannibal (pp.148-149) → Section VI "Diarium" (pp.149- ) → Section IV
  "Anrede an die neu aufzunehmenden Ill. dir." (pp.308- ) → Section VI "Circulare an die Logen"
  (begins p.399) → Section VII National-Directions-Tabelle + forms (through p.436, the end).
- The document does NOT have a known-published scholarly English translation — this is the first.
- Letters date Jan 1781 – early 1783, mostly under the order's Persian-style (Yazdegerd-era)
  calendar month names (Benmeh, Dimeh, Meharmeh, etc.) — keep those arms.

## Deliverable
`translations/scholarly/nachtrag_1787_scholarly.md`, committed to local git in batches.
When you have translated as far as you can this session, state:
`DONE: scholarly Nachtrag translated pp. 5-<last>, <n> pages this session` and the last commit SHA.
If interrupted, stop cleanly at a page boundary and note the last page completed.

## Do NOT
- Do NOT modify the corrected German text, the literal translation, or any transcription file.
- Do NOT re-correct OCR. Take the corrected text as given.
- Do NOT touch any other project or directory.
- Do NOT use `git add -A` / `git add .` / `git commit -a`.
