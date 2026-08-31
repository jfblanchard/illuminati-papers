# Glossary — People, Code Names, and Recurring Conventions

Cross-document glossary (unlike the per-document `<doc>_annotations.md` files) for
entries that recur across the corpus. Every entry cites where it was found and how
confident the claim is — nothing here is settled scholarly fact until
independently verified; see each per-document annotations file for the source
context.

## Illuminati code names

| Code name | Real identity | Source in this corpus | Confidence |
|---|---|---|---|
| Spartacus | Adam Weishaupt (order's founder) | Main volume, p.5 epigraph "Spartacus in Ep. ad Caton."; editorial gloss "Spartacus (Weishaupt...)" found in the second (Joseph Lentner) printing of the main volume — see `research/source_documents/related_publications_survey.md`. **Now also explicit in the Nachtrag itself**, PDF p.9: "Weitere Original-Briefe vom Spartacus (Weishaupt.)" heading the letter series that opens the document. | High — corroborated by an in-corpus editorial gloss in two independent places now (main volume's second printing and the Nachtrag's own section heading), not just general historical knowledge; still independently verify before publication |
| Philo | Adolph Freiherr von Knigge | Nachtrag, p.6 epigraph "Philo im Circulari an die Logen." | Medium-high — corrected after an initial mix-up with Spartacus/Weishaupt (see `lessons_learned.md`); rests on the corrector's general historical knowledge, not an in-corpus confirmation. Independently verify before publication. |
| Muſæus | Not yet identified | Nachtrag, PDF p.73: "Muſæus den Ill. Major" (proposed for the Illuminatus Major grade), grouped with Brutus, Diomedes, and other named Capitulars. | Low — first appearance, name only, no further identifying detail yet. Watch for recurrences. |

## Recurring conventions

### Name redaction via dashes
The main volume, the Anhang, and now the Nachtrag all use one or more
em-dashes in place of a name, e.g. main volume: "unſem — —, —, und —"; Anhang
p.6: "an den Grafen St— und C—". The Nachtrag alone has at least **eight**
instances in its first 29 PDF pages: p.15 "Alfred und E⸗ ==="; p.19 "den B.
W=="; p.27 "V==="; p.28 "B.==", "A==", "D==", "G==", "S===" (a cluster of
five in one sentence, a mailing address routed through intermediaries — see
correction log). This document redacts names far more heavily than the other
two so far — worth tracking as a running count rather than itemizing each
one at length going forward.

### Edeſſa — a code name for a place
Nachtrag PDF p.18-19: "Edeſſa" (OCR'd as "Edefla"/"Edella") appears to be a
code name standing in for a real city, used the way "Athen" appears to stand
in for Munich elsewhere in Weishaupt's letters (per the Nachtrag's opening
letters generally using Greek/Roman code names for people, and apparently also
for places). Not yet cross-referenced against secondary scholarship for which
real city this is.
Appears to be a deliberate editorial/printing convention protecting identities
(possibly of people not yet publicly implicated, or still living/in a position to
be harmed), not an OCR artifact — confirmed by checking that real punctuation
dashes in the same documents are always space-separated, while these redaction
dashes sit tight against a partial letter or stand alone between commas. Worth
watching for throughout the rest of the corpus; a full inventory of redacted-name
occurrences (with surrounding context, to aid any future identification attempt)
would be a good Phase 5 task.

### The Anhang interleaves a second (sympathetic) editorial voice into a reprinted letter
**Corrected 2026-08-08** — first read as a hostile government editor (see the
correction note in `annotations/anhang_1787/anhang_1787_annotations.md` for the
full story); confirmed by pages 14-16 to actually be an Illuminati-aligned voice
(likely the Anhang's compiler), fact-checking specific claims in the reprinted
letter rather than attacking the defense generally — e.g. p.15's footnote argues
"auf das Verzeichniß **unſerer** Mitglieder" (our members) while disputing one of
the letter-writer's claims. Two distinct voices either way (the original letter,
and the footnote commentary), referring to the letter's own writer in the third
person ("der Verfaſſer dieſes Schreibens"). Apply this when reading the rest of
the Anhang (and check whether the same pattern appears in the other two
documents): don't assume every first-person "I" is the same voice throughout a
document just because it's presented as continuous text — and don't lock in a
reading of an ambiguous passage from a single occurrence, as this one shows.

### The "☉" Order symbol (Nachtrag)
A circle-with-dot glyph (☉, visually an astrological Sun symbol) is used
throughout the Nachtrag's letters to mean "der Orden" (the Order) — e.g.
"Auslagen fuͤr den ☉", "die traurigen Lage des ☉s" (genitive "-s" attached
directly to the symbol). Confirmed by direct image inspection **37 times** so far (PDF pages 1-73;
exact count verified by grepping the corrected text rather than
hand-tracking, to avoid a running-tally error) — the OCR mangles it
differently almost every time (`(`, `(O`, `Q`, plain `O`, `Z`, or drops it
entirely), which is why it took several independent confirmations to be
confident this is one consistent printed glyph rather than several
different OCR failures. New usage found on PDF p.72: the symbol can also
stand in for "Orden-" **inside a compound word** ("☉sſachen" =
"Ordensſachen"), not just as a standalone word — worth watching for more
compound uses. Not yet checked in the Anhang or main volume — worth
watching for there too once correction reaches them. Note: PDF p.40 also has
an unrelated diagram built from plain "O" circles (a recruitment-pyramid
chart, see correction log) — don't confuse that with this symbol; it's a
different, purely illustrative use of a circle shape, not the Order symbol.

### A second symbol: hollow square(s), "▢" / "▢▢" (Nachtrag)
Distinct from the ☉ symbol above — a hollow square glyph, sometimes doubled,
appears repeatedly (PDF p.17, 20, 37, 38, 44, 47, 73 so far; **17 individual
box glyphs counted** by grepping the corrected text through PDF page 73, some
single, some paired). **Hypothesis, strengthened but still not certain**: the
grammar around every occurrence fits a feminine singular noun standing in the
▢ slot and its plural in the ▢▢ slot — "Loge" (lodge) fits cleanly each time
("die ganze Loge", "zwey Logen", "die andere Loge", "eine eigene Loge", "wegen
der Loge", "die Logen-Sachen", "in die Loge aufgenommen"). PDF p.73 adds the
cleanest instance yet: "...auffodere, ▢▢ zu errichten" reads directly as
"...urging him... to establish a [Loge]" — an ordinary, unforced sentence
under the Loge reading. Still flagged as a hypothesis rather than silently
resolved, per this project's uncertain-reading standard, but confidence is
now high.

### Printer's catchwords and signature marks
This era's printing repeats the next page's first word ("catchword") and a
gathering/signature mark (e.g. "A 2", "A 3") at the bottom of each page — both
show up as noise in the raw OCR since there's no page-break marker to signal them.
See `lessons_learned.md` and each document's correction log for examples. Not
unique to this corpus — a standard 18th-century typesetting convention — but worth
documenting here since it's the single most common source of OCR noise found so
far.

### List/enumeration markers are an OCR weak point
Two confirmed cases of OCR corrupting a list's numbering/lettering in a way that
would change what a citation means if uncorrected: main volume (a numbered rule
list, "9." misread for "8.") and Anhang p.6 (a lettered list, "a)"/"c)" misread
for "d)"/"e)"). Worth extra scrutiny whenever a numbered or lettered list appears
anywhere in the corpus, not just spot-checking prose.

## People not yet identified (Nachtrag code names, PDF p.9-33)
The Nachtrag's opening letters name a large cast of code names, mostly
without enough context yet to identify or even guess at real-world
referents: **Diomedes**, **Epictet**, **Cato** (also "Cato Censorius" —
possibly two different people, or one person named more fully once; not yet
resolved), **Celſus**, **Euriphon**, **Alfred**, **Hannibal**/**Annibal**
(spelled both ways), **Tiberius**, **Mahomet**, **Cronwell**, **Scipio**,
**Uliſſes** (Ulysses), **Demophilus**, **Marcellus**, **Lycurgus**,
**Trebonius**. "Philo" (Knigge, see code-names table above) and "Spartacus"
(Weishaupt) are the only two confirmed so far. Not attempting to match these
against secondary scholarship yet — flagging the full cast here so it's
findable later, per this document's lighter-annotation pacing.

## People not yet identified
- **Graf Coſtanza** — named in Anhang p.6-7 as a correspondent on Illuminati
  organizational matters (1784, 1786). Not yet cross-referenced against secondary
  scholarship. Likely either a real name or another order code name.
- **Pylades** — Anhang p.15-18: an order member who became "geiſtlicher
  Raths-Fiſcal" (an ecclesiastical council legal/financial officer), managing
  church-fund loans; deceased by May 1787 ("des verſtorbenen Pylades", p.18). Not
  yet cross-referenced against secondary scholarship for a real-name match.
- **Coriolan** — Anhang p.19: "einer der erſten untergebenen Mitglieder des
  Ordens," raised in merchant/trade business. Not yet identified.
- **Ajax** — Anhang p.22-23: code name attached to a "Handſchrift" (manuscript/
  collection) containing machine descriptions and recipes, including material
  associated with poison and abortifacients (see the detailed, carefully-worded
  entry in `annotations/anhang_1787/anhang_1787_annotations.md`). **Also named
  in the Nachtrag** (PDF p.19 letter list, p.23-24 footnote) as the source of a
  "Recept" connected to the Nachtrag editor's accusation that Weishaupt
  attempted to procure an abortion for his pregnant sister-in-law — see
  `annotations/nachtrag_1787/nachtrag_1787_annotations.md` (PDF p.22-25 entry).
  A real cross-document link between the two source documents' handling of the
  same code name and recipe thread. Not yet identified against secondary
  scholarship.

## Real named (non-code-name) figures

- **Franz Xaver von Zwack (Zwackh)** — **the Anhang letter-writer's identity,
  confirmed at p.35-36**: the letter is explicitly signed "Zwackh" and followed
  by a certificate naming him in full, "Franz Xav. v. Zwackh," and titling him
  "Regierungsrath zu Landshutt" — matching the main volume's own title page
  exactly ("Regierungsrath Zwack"). This is now a confirmed identification, not
  an inference — see `annotations/anhang_1787/anhang_1787_annotations.md`
  (p.35-36 entry) for full detail. Specific biographical claims *within* the
  letter (the suicidal period at 19, brother "Philipp Zwackhius," etc.) remain
  only as reliable as Zwack's own self-report in a document written as his own
  defense — worth independent verification before treating as settled.
- **von Maßenhauſen** — Anhang p.22-25: named as the "dermahligen Baieriſchen
  Hofkammerrath" (then Bavarian Court Chamber Councilor), imprisoned by the time
  of writing (May 1787); described as the source of a scientific/technical
  materials collection discussed at length on these pages. Appears to be a real
  historical individual, not a code name — not yet cross-referenced against
  secondary scholarship for confirmation.
- **Philipp Zwackhius** — Anhang p.27: named directly as "meines Bruders" (the
  Anhang letter-writer's brother), a student, owner of a heraldry collection
  found in the search. **This is the strongest identity clue so far for the
  letter-writer himself** — see the dedicated entry in
  `annotations/anhang_1787/anhang_1787_annotations.md` (p.27) for the full
  reasoning tying this toward Xaver von Zwack. Not yet independently confirmed.
- **Archenholz** — Anhang p.26: likely Johann Wilhelm von Archenholz, a real
  18th-century German historian/writer, cited (not yet independently verified)
  as having given a more plausible account of the "Aqua Toffana" poison's real
  composition elsewhere.
- **Kanonikus Hertel** — Anhang p.33 (resolving a name split across the p.7/8
  page break — see the correction log): a Canon named Hertel, imprisoned
  alongside von Maßenhauſen. Not yet independently identified.
- **Melchior Graf von Preysing, Carl Freyherr von Pauli, Carl Albrecht Edler
  von Vacchieri** — Anhang p.36: three real, named Bavarian court officials
  (Electoral Court Vice-President, Privy Councilor/Court Chancellor, and Court
  Vice-Director respectively) who signed and sealed a certificate attesting to
  Zwack's honest conduct in office, dated 29 November 1786 — after the Landshut
  search. Not yet cross-referenced against secondary scholarship.
- **Freyherr von Dachsberg** — Anhang p.37-39: Regierungspräsident and Vicedom
  (Vice-Domain administrator) at Landshut, author of a real dated letter
  (20 July 1786) to Zwack, reproduced as Beylage B. Not yet independently
  identified.

## Other terms flagged for verification (not yet cross-checked against secondary sources)
- **Mopsorden** ("Order of the Pug/Mops") — named in Anhang p.9 as the acknowledged
  inspiration for a rejected "Weiberorden" proposal. Real 18th-century mixed-gender
  quasi-masonic society if the reference is accurate — not yet independently
  verified. See `annotations/anhang_1787/anhang_1787_annotations.md`.
- **Maltheſer Orden** (Order of Malta) — Anhang p.11 footnote claims Jesuit schools
  passed to this order, not the Illuminati, after the Jesuits' 1773 suppression.
  Plausible, not yet verified.
