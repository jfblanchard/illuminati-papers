# The Illuminati Papers

### A verified, fully traceable English translation of the documents seized from the Bavarian Illuminati and published in 1787

<p align="center">
  <img src="images/anhang_title.jpg" width="200" alt="Title page of the Anhang (1787)">
  <img src="images/nachtrag_degree_structure.jpg" width="200" alt="Nachtrag, p. 17: the order's degree structure">
  <img src="images/nachtrag_pyramid.jpg" width="200" alt="Nachtrag, p. 40: the recruitment pyramid">
  <img src="images/anhang_signature.jpg" width="200" alt="Anhang, p. 35: Zwack's signature">
</p>

In 1785, the Electorate of Bavaria outlawed the Illuminati — the secret order
founded by Adam Weishaupt in 1776 — and raided the homes of its leaders. Two
years later, the government published what it had found: letters, internal
instructions, membership records, and defense statements, issued as three
volumes:

- ***Einige Originalschriften des Illuminatenordens*** (1787) — the main collection
- ***Nachtrag von weitern Originalschriften*** (1787) — the supplement
- ***Anhang zu den Originalschriften des Illuminatenordens*** (1787) — the appendix, containing Xaver von Zwack's point-by-point defense letter

These three publications are the primary source record of the order that became
a legend — the raw material for two centuries of scholarship, speculation, and
conspiracy theory. Partial English excerpts have appeared before — in hostile
18th-century polemics (Robison 1798, Barruel 1799) and in an independent
researcher's translation of the main volume's first ~60 pages (Terry Melanson,
2008-2020, from a French intermediary) — but no complete scholarly English
translation of any of the three documents has ever existed. The *Anhang* has no
known English translation, complete or partial — this is the first. (Surveyed
August 2026: library catalogs, archive.org, German national catalogs, the
Source Library collection, and other web-search-indexed records; WorldCat and
HathiTrust were checked via indexed search results, not their own catalog
interfaces.)

This repository publishes the first complete, verified, fully traceable English
translation of all three documents — built from the original scans, not from
another translation.

## Why this is different

- **Corrected German source text.** The raw OCR of 18th-century Fraktur is
  unreliable — misread letters, dropped words, garbled passages, lost long-s and
  umlauts. Every page here has been corrected by direct visual inspection of
  the page images, and **every single correction is logged** with its reason
  (`page — raw OCR → corrected — why`). You can audit the text word by word.
- **Two independent looks at every page.** Each page passes through a
  correction pass and a separate evaluation pass, with before/after records —
  not a single unverifiable pass.
- **Three translation layers.** A structure-preserving *literal* translation, a
  polished *scholarly* translation, and a plain-language *narrative* companion
  that tells each document's story for the general reader — all three cite back
  to the same page numbers.
- **Page-level citations throughout.** Every annotation, every uncertain
  reading, every historical term points to the scan page it came from.
- **Cross-checked against other translations.** Where other English
  translations exist (e.g., the AI-assisted versions published by Source
  Library in July 2026, or older partial translations by Robison, Barruel, and
  Melanson), this project checks against them — and cites them. They are a
  baseline for comparison, never a source to copy. The Anhang has no such
  baseline: this translation is the first.
- **Honest about its method.** This is an AI-assisted, human-verified project:
  every correction and translation pass is logged, reviewable, and reproducible
  from the public artifacts in this repository. Nothing is hidden behind a
  black box.

## The method: every word traceable

Each document moves through the same pipeline, and every stage is published:

1. **Acquire** — original scans from the Internet Archive (Duke University
   copy) and the Bavarian State Library (MDZ), with provenance recorded.
2. **Normalize** — deterministic cleanup of the raw OCR (dehyphenation,
   paragraph reflow). No guessing, no spelling changes.
3. **Correct** — page-by-page correction against 300 DPI page images, with a
   citable change record: `page — raw OCR → corrected — reason`. Original
   18th-century spelling (long ſ, etc.) is preserved as printed.
4. **Translate** — context extraction pass, then literal → scholarly →
   narrative translations.
5. **Annotate** — people, institutions, historical terminology, and uncertain
   readings, each cited to scan pages.
6. **Publish** — everything released here, in a reusable format.

## Status

| Document | Transcription | Correction | Translation | Annotations |
|---|---|---|---|---|
| *Einige Originalschriften* (1787) | done | not started | not started | not started |
| *Nachtrag* (1787) | done | **in progress** (73 of 436 pages) | not started | not started |
| *Anhang* (1787) | done | **done** | **done** (literal + scholarly + narrative) | **done** |

The *Anhang* — Zwack's 1787 defense letter from Wetzlar — is complete
end-to-end and is the project's flagship artifact: corrected transcription,
full correction log, literal, scholarly, and narrative translations, and
annotations, all page-cited.

## Repository layout

| Path | Contents |
|---|---|
| `scans/` | Original page scans (PDF), one folder per document |
| `ocr_raw/` | Raw OCR output (German, Fraktur), unedited, with provenance notes |
| `transcriptions/` | Corrected German transcriptions + correction logs + evaluation samples |
| `translations/literal/` | Structure-preserving literal English translation |
| `translations/scholarly/` | Polished scholarly English translation |
| `translations/narrative/` | Plain-language narrative companion, page-cited |
| `annotations/` | Notes on people, institutions, terms, uncertain readings |
| `metadata/document_index.csv` | Master index of the documents |
| `research/source_documents/` | Surveys of related publications and existing translations |
| `src/` | Pipeline tooling (e.g., `normalize_ocr.py`) |

## License

The source documents (1787) and the scans are public domain. The corrected
transcriptions, translations, and annotations in this repository are original
works published under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

---

*This project is historical scholarship. It translates and publishes the
primary sources — it does not speculate about secret societies.*
