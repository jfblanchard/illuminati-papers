# Illuminati Translation Project — Nachtrag Phase 4a: context-extraction pass (pp. 1-153 corrected text)

You are the translation coordinator for the Illuminati Translation Project — a scholarly
English translation package for the 1787 Bavarian Illuminati primary sources. Produce the
**context-extraction** layer for the Nachtrag (*Nachtrag von weitern Originalschriften...*,
the volume about "die Illuminatensekte überhaupt, sonderbar aber den Stifter derselben Adam
Weishaupt"), following the established `_translation_context.md` template used for the Anhang.

## Workspace / files
- Repo: `/mnt/data/projects/Research/illuminati_translation_project`
- **Corrected German text (your input):** `transcriptions/nachtrag_1787/nachtrag_1787_corrected.txt`
  (corrected through PDF page 153; pages 1-153. This is clean, high-quality German/Fraktur
  transcription with page markers.)
- **Template to match:** `translations/anhang_1787_translation_context.md` — read this FIRST
  and mirror its structure/level of detail exactly.
- **Other reference:** `devnotes.md` and `transcriptions/nachtrag_1787/nachtrag_1787_correction_log.md`
  for the document's established glossary (the ☉ = "der Orden/Order" symbol, ▢▢ = hypothesized
  "Loge/lodge", redacted-name dashes, "R. Lullus" diary material, Philo's 13-point list, etc.).

## What to produce
Write `translations/nachtrag_1787_translation_context.md` — the context-extraction pass:
1. **People/correspondents**: all named figures and their role in the Nachtrag as revealed so
   far (Adam Weishaupt/Spartacus = founder & major letter-writer; Celsus; Philo; Epictet;
   Hannibal; Marius; R. Lullus; Rosenkreutzer [resolved R]; Boulanger, Schlözer,
   Wolter/Leveling; etc. — pull roles from the corrected text, don't invent).
2. **Key terms / glossary**: the recurring symbols and abbreviations (☉ Order, ▢▢ lodge[?],
   redacted names, "Sp. [X]. S. d." recipient codes, single-letter names), each with the
   confirmed or hypothesized meaning and its evidence in the text.
3. **Register/tone guidance**: the document's register shifts (letters vs. editorial footnotes
   vs. the numbered "Notanda" lists vs. the diary entries of R. Lullus), and how that should
   drive the later literal/scholarly/narrative translation passes.
4. **Faithfulness flags**: any passages the correction log flagged as uncertain or ambiguous
   that a translator must watch (so you don't translate a guessed reading as fact).
5. **Structural map**: brief note on the document's section structure discovered to page 153
   (Sections III-VI: Epictet, Hannibal, Marius, R. Lullus's diary; the Christianity cover-story
   passage; grade table; the "Kassel letter").

## Guardrails
- This is a TEXT task on already-corrected German — do NOT re-read scan images, do NOT edit the
  corrected text or the correction log. Produce ONLY the new file
  `translations/nachtrag_1787_translation_context.md`.
- Match the Anhang template's structure and tone. Where a reading is uncertain in the source,
  flag it in the context file rather than resolving it silently.
- Keep it scholarly and traceable; cite page markers (e.g. "p.119") where useful.

WORK TO COMPLETION — write the full context file, then give a one-paragraph summary of the
document's structure and the key people/terms you catalogued.