# Illuminati Translation Project — Devin: Nachtrag literal translation (corrected pp. 1–152)

You are translating part of the Bavarian Illuminati primary-source corpus. This is
**literal** (structure-preserving, traceability-first) translation of a 1787 German
Fraktur document that has already been corrected against the scans. This is pure
text-to-text work — no images needed. A human scholarly pass + Claude reconciliation
will follow later, so prioritize fidelity to the German, not polished prose.

## Repo / files
- Repo: `/mnt/data/projects/Research/illuminati_translation_project`
- Source (the corrected German, Phase 3 — DO NOT EDIT): `transcriptions/nachtrag_1787/nachtrag_1787_corrected.txt`
  - Pages are separated by `--- PDF page N ---` markers. **Translate pages 1 through 152.**
  - Page 152 is the CURRENT end — it ends mid-sentence ("...daß hier kein Stand und Anſe-/..."), correct.
- Translation context you MUST read first (people, terms, register): `translations/nachtrag_1787_translation_context.md`
- Output file: `translations/literal/nachtrag_1787_literal.md` (create it)
- Format template to follow EXACTLY: `translations/literal/anhang_1787_literal.md` (the already-completed sibling document's literal pass)

## What to do
1. Read `translations/anhang_1787_literal.md` FIRST — mirror its structure: a `## Methodology & status`
   header (say 2026-09-19, Devin, from corrected German), a "Translator's notes on recurring terms"
   section, then `--- page N ---` markers matching the corrected file.
2. Read `translations/nachtrag_1787_translation_context.md` and apply its resolve people/terms/register guidance.
3. Translate the corrected German pages 1–152 into English **literally**: preserve sentence
   structure/order close to the German wherever English allows, even if it reads stiffly.
   - Bracketed insertions `[...]` = words supplied for English grammar OR a brief clarifying note.
   - Keep Latin terms (de Indiciis, Areopagiten, Locus Sigilli, etc.) as-is per the context file.
   - Keep the source-specific symbols as the corrected file has them (☉ = Order, ▢ = lodge) with a
     footnote/gloss the way the Anhang does.
4. Flag ANY genuinely uncertain reading inline with `[?]` rather than silently guessing.

## Guardrails
- **NEVER edit** `nachtrag_1787_corrected.txt` or any `transcriptions/` file. Write ONLY the new
  literal file under `translations/literal/`.
- No `sed -i` anywhere.
- Do not translate page 153+ (not corrected yet). Only 1–152.
- If Bash hits ENOSPC on scratch, clear temp PNGs and retry — not a real error.
- Do not touch other documents (Anhang, Einige Originalschriften) or git history.

## Deliverable
- Create `translations/literal/nachtrag_1787_literal.md` covering corrected pages 1–152.
- Commit in house style: `translation: Nachtrag literal pp. 1-152 (from corrected text)`
- Report: page count covered, list of flagged uncertain readings, and any terms you kept
  untranslated.