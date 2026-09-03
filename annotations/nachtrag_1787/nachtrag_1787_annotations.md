# Nachtrag — Annotations

Scholarly notes on names, institutions, ambiguous phrases, and interpretive
inferences, per document page. Per the project's pacing decision (2026-08-08),
this is kept lighter than the Anhang's annotation file: only genuinely notable
findings are recorded here, not every historical cross-reference. Nothing here
should be treated as settled without independent scholarly verification.

## PDF page 3: physical-copy provenance (predates and is separate from the 1787
printed content)

A handwritten ownership inscription in French cursive, on the blank leaf before
the title page:

> Ce Livre appartient a Moi Fidel Loë [Attia?] d'Eichstaett 1805

("This book belongs to me, Fidel Loë [surname uncertain], of Eichstätt, 1805")
— plus a separate, later signature in different ink/hand below it, partly
illegible (something like "Bergmau[?]... n Kyrle"). This documents a real chain
of ownership for *this specific physical copy* of the Nachtrag, 18 years after
its 1787 printing, by someone in Eichstätt (a Bavarian town). Not part of the
original publication and not corrected as body text (see
`nachtrag_1787_correction_log.md`), but worth keeping as provenance metadata —
useful if this copy is ever compared against other surviving exemplars, and
mildly interesting in its own right (a French-language ownership note in a
German book, in Bavaria, in the Napoleonic era). Surname and second signature
need a closer look at higher image resolution before treating either as
confirmed.

## PDF page 9: this document's "Order" symbol

The Illuminati "Order" (der Orden) is referred to in-text with a circular
glyph, rendered here as ☉, that the OCR consistently misreads as a bare `(` or
`(O` (e.g. "gegen den ( hat", "vom (O", "für den O" — see raw-text grep hits).
Standardizing all instances to ☉ during correction for legibility. Same symbol
convention likely continues throughout the rest of the document — worth
double-checking against a few more page images as correction proceeds, in case
it turns out to be a different glyph than assumed here.

## Letter header abbreviations: "C." = Celsus, confirmed PDF p.64

The recurring letter header format "Sp. [X]. S. d." (Spartacus to [X], S.
d. — likely a Latin epistolary formula, still not expanded) uses single
letters for the recipient. PDF p.64 spells one out in full: "13. Sp. Celſo
S. d." — confirming "C." elsewhere in this series stands for **Celsus**,
not just an abbreviation guess. Worth checking future single-letter
headers against this now-confirmed pattern.

## PDF pages 22-25: the "Marius" letter — a ciphered family matter, and the
Nachtrag's editorial accusation against Weishaupt (sensitive content,
documented factually per this project's standard — see the Anhang's Aqua
Toffana/Ajax handling for precedent)

Letter 3, addressed to "Beßter Marius!", contains two ciphered numeral
sequences that a footnote in this same document decodes:

1. (PDF p.22) "meine [cipher]" = "meine [cipher]" → per the footnote, "meine
   Schwaͤgerinn iſt ſchwanger" ("my sister-in-law is pregnant"). **The
   footnote states the cipher key itself is given in the first volume of the
   Originalſchriften** (the main volume of this same corpus) — worth checking
   when that volume is corrected, as a genuine cross-document link, not yet
   verified.
2. (PDF p.23) a second cipher, decoded by its own footnote as "das Kind
   abzutreiben" ("to abort the child").

**What the letter itself says** is only this oblique, ciphered reference,
plus a great deal of anxious, coded discussion of arranging a "Diſpenſation"
(dispensation, likely from a marriage-impediment rule) and a "Heyraths-Licenz"
(marriage license) through intermediaries, and a direct statement that the
matter is "ſogar criminaliſch" (even criminal) and that he is only in "the
4th month," urgently asking for help.

**What the Nachtrag's own editorial commentary adds** (a footnote,
interleaved with the letter — see correction log for the exact structure) is
a direct, hostile accusation: that Weishaupt committed "Blutſchande"
(incest) and "attentierter Kindesabtreibung" (attempted abortion), and that
this connects to the "Ajax" poison/abortifacient recipe material — **the same
"Ajax" code name and recipe thread already documented in the Anhang**
(`annotations/anhang_1787/anhang_1787_annotations.md`) — a real cross-document
link between the two source documents in this corpus. The footnote then
quotes Weishaupt's own later published "Apologie" (his defense), page 6,
where he swears under oath he never heard of, saw, or condoned "Vergiftung"
(poisoning) in his life — juxtaposed by the editor as proof of hypocrisy.

**Update (PDF p.26-29)**: the situation isn't confined to letter 3. Letter 4
(also to Marius) continues arranging lodging for the sister-in-law near
Sandersdorf; letter 5 (to a different, unidentified recipient, header "Sp. C.
S. d.") continues asking for help and explicitly requests "das ſtrengſte
Stillſchweigen" (the strictest silence) about "meiner Sch." (his
sister-in-law) — confirming this matter runs across at least four
consecutive letters (3-5, with letter 6 changing subject to his mother's
death and the Order's finances instead).

**How to treat this**: the ciphered content in Weishaupt's own letter is
primary-source evidence of *something* he wanted to keep secret and
considered criminal — the letter alone does not specify whose child, or
whether "incest" is an accurate characterization (that framing comes only
from the hostile editorial voice, in a publication explicitly designed to
discredit him and the Order). This is a real, historically attested
controversy (Weishaupt's sister-in-law's pregnancy is documented in
secondary Illuminati scholarship), but the specific accusatory framing here
is the *publisher's* interpretation, not an independently established fact
from this letter alone. Treat the cipher-decoded content as reliable (it's
the document's own footnote, and the numerals were independently confirmed
at 600 DPI), and treat the "Blutſchande"/incest characterization as a
contested claim needing secondary-source verification before being repeated
as settled fact in any translation or summary.

## PDF pages 44, 55: "Armenium" and "Arminius" — possibly the same person,
not merged

Two names appear with near-identical hostile descriptions ("unertraͤglich,
eigenſinnig, eitel..."): "Armenium" (PDF p.44, an "ehrgeitziger, eitler,
ruhmſichtiger Pedant") and "Arminius" (PDF p.55, an "unertraͤglicher,
eigenſinniger, hochmuͤthiger, eitler Narr"). Re-checked PDF p.44 at 600 DPI
to rule out a simple misread — it genuinely says "Armenium," a different
spelling from "Arminius." Could be the same person under two spellings (not
uncommon in this era's printing) or two different people who happen to get
similar stock insults. Not merged in the corrected text; flagged here for a
future pass, since resolving it matters for tracking a real historical
identity through the letters.

## PDF pages 56-57: the Nachtrag names Weishaupt a "Verführer" (corrupter)
of university students

A footnote, anchored to Weishaupt's own worry (in his letter) that being
known to direct these young recruits could get him branded "einen Verführer
junger Leute" (a corrupter of young people), has the Nachtrag's editor reply
directly: "Weishaupt will nie fuͤr das angeſehen werden, was er wirklich
iſt. Verdient er nicht mit Recht ein Verfuͤhrer genannt zu werden: indem er
eine Menge junger Leute auf der Univerſitæt durch ſeine Heucheley und
vorgeſpiegelte Moralitæt... in ſein Garn gebracht, und verfuͤhret hat." —
"Weishaupt never wants to be seen for what he really is. Doesn't he deserve
to be rightly called a corrupter, in that he lured and corrupted a great
many young people at the university through his hypocrisy and feigned
morality?" This is the editorial voice again, not Weishaupt's own words —
same interleaved-commentary pattern documented elsewhere in this corpus
(see glossary). A serious accusation, presented without independent
evidence in the footnote itself; not treated as established fact here.

## PDF pages 16-19: Weishaupt's own outline of the Order's grade/degree structure

A short numbered list (PDF p.17) in Weishaupt's own words, planning to
consolidate the Order's degrees: Novitiate (mostly unchanged), Junior +
Minerval (merged into one grade), Illuminatus minor + Gesell, Meister + großer
Illuminat, Illuminatus dirigens + Baumeister/Architect, and finally
"Mysteria" as a capstone. Useful primary evidence for how the degree system
was actually structured/reorganized, in the founder's own planning
correspondence rather than a published or secondhand account. Also on these
pages: two more redacted names via dashes (see glossary) and a recurring code
name for a place, "Edeſſa" (see glossary) — the letters' code-name convention
extends to places, not just people.

## PDF pages 9-11: Letter 1, "Spartacus" to an unnamed correspondent

The document opens with a numbered letter series ("I.", header "Sp. C. S. d.")
from Spartacus
(Weishaupt's own Illuminati code-name, confirmed by this document's own
page-9 heading "vom Spartacus (Weishaupt.)" — no inference needed here, unlike
the Anhang's identity question). The letter is organizational/procedural: nine
numbered recruiting and leadership tactics (recruit only capable, respected
men; put respected figures at the head of assemblies; avoid direct expulsion of
unsuitable members, instead overload them with work until they resign
voluntarily; lead by personal example rather than command). Useful primary
material for understanding how the Order actually recruited and managed
members, in Weishaupt's own words — distinct in register from the Anhang's
personal defense letter, as expected going in.
