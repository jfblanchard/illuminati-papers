# Related Publications Survey (Phase 1 open item)

Resolves the "survey 1786-1794 related/adjacent publications" item from the
project's working checklist.
Covers the three original candidates plus a much larger list found via a scholarly
aggregator. Written 2026-08-07.

## The three original candidates — resolved

### 1. Second Internet Archive item for the main volume — NOT a duplicate scan
`archive.org/details/EinigeOriginalschriftenDesIlluminatenOrdens1787` (identifier
prefix `39494071...`, a Scribd-style re-upload, not a library digitization).

Confirmed by direct text comparison (searched both djvu.txt files for distinctive
content): this is the **same underlying text** as our Duke/Anton Franz copy — it
opens with the same "Spartacus in Ep. ad Caton." epigraph and contains an editorial
gloss "Spartacus (Weishaupt...)" — but its imprint line reads "München, bey Joseph
Lentner, 1787" rather than the Duke copy's "gedruckt bey Anton Franz... und zu haben
in den drey Buchhandlungen". Joseph Lentner is the same bookseller who published the
Nachtrag. This looks like **a second printing/issue of the main volume**, not a
duplicate — a real bibliographic fact worth recording, not just noise. Its scan/OCR
quality is markedly worse than the Duke copy (heavily garbled djvu.txt).
**Recommendation:** don't do a full parallel correction pass on this copy — the
Duke copy is the better source — but log it in `metadata/document_index.csv` as a
known alternate printing, useful for cross-checking specific passages if the Duke
scan ever has a damaged or illegible page.

### 2. Bemerkungen über einige Originalschriften des Illuminatenordens (1787) — commentary, confirmed
`archive.org/details/BemerkungenberEinigeOriginalschriftenDesIlluminatenOrdens1787`
(Google Books scan). Read the actual Vorrede (preface) directly: opens "Viele Jahre
lang verfolgt schon die bairische Regierung die Illuminaten-Geſellſchaft..." ("For
many years now the Bavarian government has persecuted the Illuminati society...") —
unambiguously a **polemical work defending the Illuminati** against the Bavarian
government, analyzing and reacting to the "Einige Originalschriften" publication.
Frankfurt und Leipzig, 1787. **Confirmed: secondary commentary, not a primary seized
document** — this directly contradicts how the FactGrid list below categorizes it
(see caveat there).

### 3. System und Folgen des Illuminatenordens aus den gedruckten Originalschriften desselben gezogen. In Briefen (München, 1787) — commentary, confirmed
Digitized at MDZ (`digitale-sammlungen.de/de/details/bsb11689767`) and listed in
Deutsche Digitale Bibliothek. Not yet read directly (only checked via search
results and the FactGrid summary below), but title and every secondary description
found agree: an analytical work "drawn from" (gezogen aus) the published primary
materials, presented "in Briefen" (in letters) — i.e. a secondary systematic
analysis built on top of the primary documents, not itself one of the seized
papers.

## A much larger candidate list — FactGrid

`database.factgrid.de/wiki/Contemporary_publications_on_the_Illuminati` — FactGrid
is a real, established collaborative history-research Wikibase (affiliated with
German academic history-of-science infrastructure), not a random blog. Retrieved via
WebFetch, which summarizes fetched pages through an intermediate model rather than
giving raw HTML — **treat every detail below (page counts, dates, and especially the
primary/secondary classification) as a lead to independently verify against the
actual source before relying on it**, not as settled fact. The page's own classification
of *Bemerkungen* as "primary" already conflicts with what direct reading confirmed
above, which is a concrete demonstration of why.

Roughly 25 titles, 1786-1794, organized by year. Highlights beyond what we'd already
found:
- Several **Weishaupt-authored defense works** (1786-1788): *Vollständige Geschichte
  der Verfolgung der Illuminaten in Bayern*, *Apologie der Illuminaten*, *Kurze
  Rechtfertigung meiner Absichten*, *Einleitung zu meiner Apologie*, and others —
  Weishaupt's own voice, responding to the seizures, not part of the seized corpus
  itself.
- *Vorstellung* by Thomas Franz Maria Frhr. von Bassus (1787/1788) — Bassus's own
  official report on the Sandersdorf raid to the Grisons Republic. Directly relevant
  given the Nachtrag is literally the documents seized *from* Bassus's castle — this
  is the other side of that same event, from Bassus himself.
- *Philos endliche Erklärung und Antwort* by Adolf Frhr. von Knigge (1788) — Knigge
  (the real "Philo" — see `nachtrag_1787_eval_sample.md`) defending his own
  involvement, in his own words.
- *Die neuesten Arbeiten des Spartacus und Philo in dem Illuminaten-Orden*
  (Frankfurt, 1793) — described as original order communications published for the
  first time, edited by Grolman. If accurate, this could be closer to a genuine
  primary source than most of the list, published years after the initial wave.
- Full list is long (defense works, critiques, an alleged-insider narrative in 3
  volumes, grade-level ritual documents) — see the FactGrid page directly rather
  than duplicating the whole table here.

## Decision (2026-08-07)

Phased, not narrowed: finish the pipeline (Phases 2-6) on the 3 core seized-document
publications first — that stays the immediate focus. But the project's eventual
target is **the full corpus**: all ~25 publications identified via FactGrid (pending
per-title verification, per the caveat above), plus anything else that surfaces
during that verification. Goal stated by the user: as complete a public reference
corpus as possible for the scientific/scholarly community, not just the 3 seized-document
publications.

Practical consequence: `metadata/document_index.csv` should eventually carry a row
for every title on the FactGrid list (and whatever else turns up), each independently
verified (existence, digitized source, primary-vs-commentary classification —
don't trust FactGrid's own tagging, per the Bemerkungen discrepancy above) before
acquisition. This is real, large future work, tracked as an explicit
later phase rather than folded into or blocking the current Phase 2-6 work on the
core 3.
