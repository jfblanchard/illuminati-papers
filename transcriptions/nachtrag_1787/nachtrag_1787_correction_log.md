# Nachtrag — Correction Log

Full-document Phase 3 correction, page by page. Lighter-weight companion to
`nachtrag_1787_eval_sample.md` (the detailed pilot record for PDF pages 5, 6, 11 —
not repeated here). One line per correction: page — raw OCR → corrected — reason.
The actual corrected German text is in `nachtrag_1787_corrected.txt`; this file is
the citable change record for it. Page numbers below are the PDF's own physical
page numbers (this document's OCR has no printed page markers), not the
book's own printed page numbers.

## Methodology & status
Same as `nachtrag_1787_eval_sample.md`: corrections made by Claude (Sonnet 5) by
direct visual inspection of page images (`pdftoppm`, 300 DPI) against the raw OCR
(`nachtrag_1787_transcription.txt`, Phase 2 output). AI-assisted first pass, not a
final scholarly correction — pending human review. Spelling preserved as printed
(long ſ, combining-e uͤ/aͤ/oͤ convention, etc.); the extremely common f/ſ
confusion is fixed throughout but not itemized per instance below to keep this
log readable — only content-level fixes (misreads, dropped/garbled words, spurious
noise, page-transition artifacts) are itemized in full. Per the project's pacing
decision (2026-08-08), annotation/narration depth is lighter here than the
Anhang's: only genuinely notable findings are called out.

## PDF pages 1-4 (front matter, before the printed text begins)
Not part of `nachtrag_1787_transcription.txt` — no OCR exists for these pages, so
nothing to correct. Noted here for completeness of the page-by-page record:
- Page 1: blank pastedown (paper texture only).
- Page 2: blank.
- Page 3: handwritten ownership inscription in French cursive ink: "Ce Livre
  appartient a Moi Fidel Loë [Attia?] d'Eichstaett 1805", plus a separate later
  signature in a different hand/ink ("Bergmau[?]... n Kyrle" or similar — partly
  illegible). Genuine provenance evidence for this physical copy — a named owner
  in Eichstätt in 1805 — worth a note in `annotations/nachtrag_1787/` even though
  it predates and is unrelated to the 1787 printed content itself.
- Page 4: a faint ink library/collection stamp, mostly illegible at this
  resolution (something like "17798" or a shelf mark) plus scattered foxing.

## PDF page 5 (title page)
Already fully corrected in `nachtrag_1787_eval_sample.md` (2026-08-04 pilot) —
carried forward unchanged into `nachtrag_1787_corrected.txt`. See that file for
the itemized correction table. Headline items: removed a handwritten
ownership-mark line at the top (pure noise, not print), `Wetshaupt`→`Weishaupt`,
`Baron Bellusiſchen`→`Baron Baſſuſiſchen`, `3 wo`→`Zwo`, garbled decorative rule
and "München, 1787." line reconstructed.

## PDF page 6 (epigraph)
Already fully corrected in `nachtrag_1787_eval_sample.md` — carried forward
unchanged. Headline items: several f/ſ fixes, a Phase 2 dehyphenation bug found
and fixed here (`Grundſaͤ⸗ tzen`→`Grundſaͤtzen`),
trailing page-number noise removed. Epigraph is signed "Philo" — Knigge's
Illuminati code-name, not Weishaupt's (his was "Spartacus") — flagged for Phase 5,
unverified beyond general knowledge.

## PDF page 7
- `ſchon eben fo, wie fie find` → `ſchon eben ſo, wie ſie ſind` — f/ſ confusion (x2)
- `meines Abſter ns` → `meines Abſterbens` — a gap in the printed/scanned text
  where "be" should be; restored on lexical grounds ("Absterben" = death/passing,
  no such word as "Abſterns"). **Flagged**: the gap is real on the page image, not
  just an OCR dropout — worth a second look at higher resolution if this matters
  for a citation.

## PDF page 8
Entire page is a modern Internet Archive digitization-artifact page ("Digitized
by the Internet Archive in 2015" + the archive.org URL, watermarked over a faint
architectural graphic), not part of the 1787 original. Raw OCR captured this as
`Digitized by the Internet Archive : 1 in 9` / `g https://archive.org/details/...`
/ stray `\ =` / `—`. Omitted entirely from `nachtrag_1787_corrected.txt` — same
treatment as other pure-noise artifacts (decorative rules, ownership stamps) on
other pages.

## PDF page 9 (printed page "1")
- `CORRESPON DEN.` → `CORRESPONDENZ.` — badly garbled
- `L. Sp⸗ E. S. d.` → `I. / Sp. C. S. d.` — the "I." is a Roman numeral (this is
  letter 1 of the collection); "Sp. C. S. d." is a header abbreviation printed
  as-is, not expanded (uncertain what it stands for — possibly sender/recipient
  code initials — flagged for Phase 5, not guessed at)
- `Och habe nun alle Communicate geleſen, N und werde` → `Ich habe nun alle
  Communicata geleſen, und werde` — stylized drop-cap "I" misread as "O";
  "Communicate" → "Communicata" (Latin plural, misread); stray "N" is noise
- `Donners ag` → `Donnerſtag` — gap where "t" belongs
- `daß fie ſich` → `daß ſie ſich` — f/ſ
- `alles in Orb: nung` → `alles in Ordnung` — misread + spurious mid-word colon,
  the same "stray mid-word punctuation" OCR failure mode seen throughout this
  corpus (this is at least the fourth instance)
- `gegen den ( hat` → `gegen den ☉ hat` — this document's "order" symbol (a
  circle, likely meant as ☉/an alchemical-style glyph standing in for "der Orden")
  is consistently misread by the OCR as a bare `(` or `(O`; recurs often later in
  this document (see raw-text grep hits for "(O") — standardizing to ☉ throughout
  for legibility, worth confirming against a few more page images as correction
  continues
- trailing `; A` and the following stray `| Ich` line → removed from body text;
  these are the page's signature mark ("A") and catchword ("Ich", the first word
  of the next page) printed in the bottom margin, not body text — same
  page-transition-noise pattern already documented for PDF page 11 in the pilot

## PDF page 10 (printed page "2")
- leading `2` → page number, not body text (removed, same as page 11's leading
  `3` in the pilot)
- `thäs tigen` → `thaͤtigen` — spurious mid-word split
- `Männern` → `Maͤnnern`, `Köpfe` → `Koͤpfe` — normalized to this document's own
  combining-e convention for consistency (same reasoning as `überlegt`→`uͤberlegt`
  on PDF page 6 in the pilot)
- `Celfus` → `Celſus`, `werden fie.` → `werden ſie`, `verftehen` → `verſtehen` — f/ſ
  (plus a stray period removed on the second)
- `In den W wollte ich Leute` → `In den Verſammlungen wollte ich Leute` — a whole
  word collapsed to a single stray capital "W"; confirmed against the image
  ("Versammlungen" = assemblies/meetings, makes full sense here) — another
  instance of the whole-word-omission failure mode already catalogued
- `Rekrutiruug` → `Rekrutirung` — misread
- `zu ſeuchte Köpfe` → `zu feuchte Koͤpfe` — a reverse f/ſ error (OCR put a long-s
  where a plain "f" belongs); "feuchte Köpfe" (damp/muddled heads) is the correct
  idiom, "ſeuchte" isn't a word
- `unter eben fo nach⸗` [paragraph break] `laͤßigen Superioren` → `unter eben ſo
  nachlaͤßigen Superioren` — f/ſ, and this word's hyphenation wasn't rejoined by
  Phase 2 because the raw OCR inserted a spurious paragraph break exactly at the
  hyphen (no blank-line-delimited block boundary to trigger the script's rejoin
  logic) — manually rejoined here; worth checking whether this recurs elsewhere,
  since it's a Phase 2 edge case distinct from the combining-mark bug already fixed

## PDF page 11 (printed page "3")
Already fully corrected in `nachtrag_1787_eval_sample.md` — carried forward
unchanged (see that file for the full itemized table, including the flagged
`Sache`/`Sachen` ambiguity and the `verſaͤumen` diacritic-confidence note).

## PDF page 12 (printed page "4")
- `nicht übereinfommen` → `nicht uͤbereinkommen` — k/f misread (a Fraktur k and f
  look visually similar; this is a different failure mode than the usual f/ſ
  confusion)
- `Meuſch` → `Menſch` — misread (u/n)
- `Chimzere` → `Chimære` — the æ ligature misread as "z"
- `Sitten: Regiment` → `Sitten-Regiment` — this one is a **real hyphenated
  compound misread as a colon**, not spurious punctuation like the "Ordnung"/
  "Grundſätzen" cases elsewhere — worth distinguishing from the "OCR inserts a
  meaningless mid-word period/colon" bug, since here the punctuation mark itself
  is wrong (should be a hyphen), not merely misplaced
- `fie muͤßen`, `fie ſich`, `ſetzen fie`, `Glauben fie` → `ſie` (f/ſ, x4 on this
  page alone)

## PDF page 13 (printed page "5")
Clean page, only minor fixes:
- `Warum ſol` → `Warum ſoll` — missing second "l"
- `Ill min,` → `Ill min.` — comma should be period; likely an abbreviation for
  an Illuminati grade name ("Illuminatus minor") — flagged for Phase 5, not
  expanded here since the abbreviation itself isn't fully certain
- `Nam` (for "Namen"/name) — confirmed as printed, not an OCR error; kept as-is
  per this project's preserve-as-printed convention

## PDF page 14 (printed page "6")
- `meinen Nager zu verbergen` → `meinen Namen zu verbergen` — misread, "Nager"
  isn't a real word in context
- `has. ben` → `haben` — spurious mid-word period + split (recurring OCR bug)
- `Caefar` → `Cæſar` — æ ligature + missing long-s
- `wuͤnſche, a alle` → `wuͤnſche, daß alle` — misread ("a" for "daß")
- `mit 20000 fl,` → `mit 20000 fl.` — comma should be period (abbreviation mark)
- `Sie find freylich`, `was fie ſeyn`, `fed Spiritus` → `ſind`/`ſie`/`ſed` (f/ſ)
- Raw OCR ran letter 1's closing signature ("...ganz eigener Spartacus.") and
  letter 2's heading numeral ("2.") together on one line with no separation;
  split them in the corrected text to match how the page image actually lays
  them out (signature block, then a numbered heading, then "Sp. A. A. S. d.")

## PDF page 15 (printed page "7")
- Leading `1` / `ri` → removed — page-transition noise (a signature-mark
  fragment plus the catchword "wenig" duplicated from the bottom of page 14);
  the real text picks up mid-sentence, "...ſonſt iſt wenig damit geholfen"
  (continuing across the page break)
- `Unterſtuͤtzen fie`, `fo muß er` → `ſie`/`ſo` (f/ſ)
- `E⸗ ==` → `E⸗ ===` — a **redacted name** (dash-for-name convention already
  documented in `annotations/glossary_people_and_terms.md` "Name redaction via
  dashes" — this is the first confirmed instance of that convention in the
  Nachtrag specifically, extending a pattern previously only seen in the main
  volume and Anhang). **Flagged**: the exact dash count is hard to pin down
  precisely at this resolution, kept as read.
- `60ofl.` → `600 fl.` — misread zero as lowercase "o" + missing space
- `Pretenlionen` → `Praͤtenſionen`, `Profeflor` → `Profeſſor` — garbled
- `im ganzen Q kein einzigen` → `im ganzen ☉ kein einzigen` — **confirms** the
  Order-symbol theory flagged on PDF page 9: the image here clearly shows the
  same circle-with-dot glyph, misOCR'd as a capital "Q" this time instead of
  "(" or "(O" — the OCR is inconsistent about how it mangles this symbol, but
  the underlying printed glyph is the same each time

## PDF page 16 (printed page "8")
- `Anfänger` → `Anfaͤnger`, `Ehren = Grade` → `Ehren-Grade`, `um zuarbeiten` →
  `umzuarbeiten` — consistency / spurious spacing
- `ans getroffen` → `angetroffen` — spurious split
- `Hinc ille iræ` → `Hinc illæ iræ` — misread (this is a real Latin tag, "hence
  those angers," quoting Terence/Juvenal; "ille" should be "illæ")
- `find keine`, `fie muͤßen`, `à la Jefuite` → `ſind`/`ſie`/`Jeſuite` (f/ſ)
- `M. x. x.` kept as printed — an abbreviation, likely for a grade name;
  **flagged**, not expanded, since I'm not confident what it stands for

## PDF page 17 (printed page "9")
- `ift folsgender` → `iſt folgender` — spurious mid-word split
- isolated `.` before `Novitiat` → `1.` — the first list item's number was
  dropped entirely, leaving only a stray period; restored from context (items
  2-5 all present and numbered)
- `IIluminat` (x1) / `Iluminat` (x1) → `Illuminat` — doubled-capital and
  missing-double-l misreads, same word misread two different ways twice on one
  page
- `Gmiliter` → `ſimiliter` — badly garbled Latin ("likewise")
- `Baumeifter` → `Baumeiſter` (f/ſ)
- `der Mü werth` → `der Muͤhe werth` — truncated word ("Mühe" cut to "Mü")
- `Hoc nondum ef :` → `Hoc nondum eſt:` — missing "t" (Latin: "this is not yet
  [the case]")
- `hätte, Die Grade müßen` → `haͤtte. Die Grade muͤßen` — comma should be a
  period (sentence boundary), plus umlaut consistency
- **Flagged, not resolved**: `in den ▢▢ austheilen` — the printed page itself
  shows two small hollow squares here, not an OCR gap (raw OCR rendered them as
  `[JI]`, which was its own garbled attempt at the same glyphs). Could be a
  typesetter's placeholder for a missing/foreign character, or an intentional
  visual redaction of a plural noun (the grammar wants something like "the
  lodges" or "the provinces" here). Kept as ▢▢ rather than guessing; worth a
  second look at the original if this sentence matters for a citation.

## PDF page 18 (printed page "10")
- `niederzus laſſen` → `niederzulaſſen`, `Frey heit` (p.19, related pattern) —
  spurious splits
- `konnen` → `koͤnnen`, `unmöglich` → `unmoͤglich`, `ſtatutenmäßig` →
  `ſtatutenmaͤßig` — consistency
- `Edefla` → `Edeſſa` — f/ſ; this is a recurring **code name for a place**
  (city), also appears on PDF p.19 as `Edella`/`Edeſſa` — same code name, two
  different OCR corruptions of it
- `fie ſuchen`, `fie aufgenommen` → `ſie` (f/ſ)
- `Ceeremonien` → `Cæremonien` — æ ligature doubled as "ee"
- `Stolze` → `Stolz` — the raw's trailing "e" doesn't fit this noun list's
  parallelism ("Unwiſſenheit, Stolz, Geiſt der Unabhaͤngigkeit..."); **flagged**
  as a judgment call based on grammar/parallelism, not a fully certain visual
  read at this resolution
- `proftituiert` → `proſtituiert` (f/ſ)
- `atqui hoc non a` → `atqui hoc non faciunt.` — the raw OCR fragmented this
  Latin closing phrase ("and yet they do not do this") right at the page break;
  the full phrase is legible on the page image itself, followed by the
  catchword "Sie" (removed from body text, same page-transition-noise pattern
  as elsewhere)

## PDF page 19 (printed page "11")
- `Edella` → `Edeſſa` — see PDF p.18 note above, same code name
- `werth ind,` → `werth ſind.` — missing ſ + comma should be period
- `So‚crates` → `Socrates` — stray comma-like OCR mark
- `B. W = =` → `B. W==` — **another redacted name** (the second one found so
  far in this document, after PDF p.15's `E⸗ ===` — see
  `annotations/glossary_people_and_terms.md`)
- `daß fie die Achten Freymaͤurer find` → `daß ſie die aͤchten Freymaͤurer
  ſind` — f/ſ (x2) + `Achten`→`aͤchten` (capitalization/umlaut; "aͤchte" here
  means "genuine/true," not the ordinal "eighth")
- `der fol ſich` → `der ſoll ſich` — missing "l"
- `vermus then` → `vermuthen` — spurious split
- `Mau muß` → `Man muß` — misread (u/n)

## PDF page 20 (printed page "12")
- `jo` → `ſo`; `fie` (x5: "wenn fie den", "bitte fie, laſſen fie", "Communiciren
  fie", "damit fie", "koͤnnen fie") → `ſie`; `find fie` → `ſind ſie` — f/ſ,
  unusually dense on this page
- `III. Maj.` → `Ill. Maj.` — misread (roman numeral for "Illuminatus", an
  abbreviation pattern already seen as "Ill. dirigens" on PDF p.17)
- `Inftructionen` → `Inſtructionen`, `diefen` → `dieſen` — f/ſ
- `geläufig` → `gelaͤufig` — consistency
- `die [] das bewußte Haus` → `die ▢ das bewußte Haus` — another instance of
  the hollow-square placeholder/redaction glyph (see PDF p.17 note); this time
  a single box, not two, and in a different grammatical slot (subject of the
  sentence, "that the ▢ bought the well-known house") — **flagged**, not
  guessed at

## PDF page 21 (printed page "13")
- `fie mich` → `ſie mich`, `find Hummeln` → `ſind Hummeln` — f/ſ
- `höre` → `hoͤre`, `können` → `koͤnnen`, `für` → `fuͤr`, `hätten` → `haͤtten` —
  consistency
- `Anh haͤnglichkeit` → `Anhaͤnglichkeit`, `Werk- Bies nen` → `Werk-Bienen`,
  `Provincial- Bes richt` → `Provincial-Bericht` — spurious mid-word splits
- `invicem; ſicut Chriſtus dilexit Ecelefiam,` → `invicem, ſicut Chriſtus
  dilexit Eccleſiam.` — a real Latin liturgical quotation ("Farewell, and love
  one another, as Christ loved the Church"), garbled punctuation and spelling
  corrected against the image
- `konnte ich i ihn auch nichs ſchicken` → `konnte ich ihn auch nichts
  ſchicken` — stray "i" (noise) + missing "t"
- `Ephefus` → `Epheſus` — f/ſ
- Trailing `Spartacus,` → `Spartacus.` — this closes the long letter that
  opened on PDF p.14 (letter "2", "Sp. A. A. S. d.") — comma should be a
  period, it's the end of the letter, not a continuation. The raw OCR's
  trailing `2` / `Ir` fragments after this are page-transition noise
  (signature mark), not decoded further here — held for the next page's
  correction since letter-numbering for what follows needs to be confirmed
  against the image directly, not inferred from OCR alone (per the project's
  pacing note on going carefully through the sensitive material starting
  around PDF p.22).

## PDF pages 22-25 (printed pages "14"-"17"): letter 3 ("Beßter Marius!") and
its footnote apparatus — sensitive content, corrected with extra care

**Structural finding, resolved by direct image inspection rather than
inferred from raw OCR order** (this is exactly the kind of thing that would
have been wrong if rushed): PDF pages 23-24 each have two zones — the main
letter text above a horizontal rule, and a footnote below it. The footnote is
a single continuous block that starts on p.23 (decoding two cipher sequences
from the letter) and continues onto p.24 (an editorial commentary paragraph
plus a block quotation) before ending; the main letter itself continues
uninterrupted across the same two pages via ordinary catchword linkage
("Freund-" at the bottom of p.24's main-text zone completes as "ſchaft
erfaͤhrt" at the top of p.25 — the footnote does not interrupt the letter's
own pagination, it just shares the same physical pages). Confirmed the raw
OCR's page-22/23 cipher-number transcription against a 600 DPI re-render
before finalizing (see below) — this stretch involves numerals, which are
exactly the kind of content where a misread has real consequences and no
lexical-plausibility check to catch it.

- PDF p.22: `14 3:` → `14` (page number) + `3.` (letter number, colon should
  be period); `unmdͤglich` → `unmoͤglich`; `Bez griff` → `Begriff` (spurious
  split); `daͤrfen` → `duͤrfen` (misread — "därfen" isn't a word, "dürfen" is);
  trailing stray `\` removed (noise); `nach | Alen` → `nach [catchword] Athen`
  (misread + stray pipe noise). **Cipher numbers**: raw OCR badly mangled
  `Denken fie, meine 18. 10.5. 2 1. d L9.1Q,.5.27.12, 138.0, 8.17.)` — restored
  by direct visual reading as `Denken ſie, meine 18.10.5.21.12.6.8.17.4.13.
  iſt 18.10.5.21.12.13.6.8.17.*)`, **then independently re-confirmed against a
  600 DPI crop** (see `crop_022_ciphers_big.png` in this session's scratch
  directory, not saved to the repo) — both readings matched exactly. High
  confidence on the digits themselves; no attempt made to decode what they
  numerically encode beyond what the document's own footnote states.
- Footnote (p.22-23 boundary): `angeführten` → `angefuͤhrten` (consistency);
  `ſchwange b.` → `ſchwanger.` (misread, split across the OCR's own line
  break). This footnote states the cipher decodes to "meine Schwägerinn iſt
  ſchwanger" ("my sister-in-law is pregnant") **per a cipher key the Nachtrag
  says is given in the first volume of the Originalſchriften** (the main
  volume of this same seized-document corpus) — worth checking the main
  volume for that key when it's corrected, as a genuine cross-document link.
- PDF p.23: cipher sequence `3.4.13.9. — 12.11.24.20.19.17.8.4.11.8.13.*)` —
  same treatment as above, visually read then confirmed at 600 DPI
  (`crop_023_ciphers_big.png`). Footnote states this decodes to "das Kind
  abzutreiben" ("to abort the child").
- The paragraph beginning `Da ſehe nun die Welt den moraliſch edlen Mann
  Spartacus (Weishaupt.)...` is **not part of Weishaupt's letter** — it is the
  Nachtrag's own editorial voice, continuing the same footnote, accusing
  Weishaupt directly of incest ("Blutſchande") and attempted abortion
  ("Kindesabtreibung"), and linking this to the "Ajax" poison/abortifacient
  recipe material already documented in the Anhang (see annotations). This is
  the second confirmed instance in this corpus of a footnote/editorial voice
  interleaved with a reprinted primary letter — same pattern as the Anhang
  (see `annotations/glossary_people_and_terms.md`).
- The footnote continues on p.24 with a direct block quotation from
  Weishaupt's own later published "Apologie" (his defense/apology), page 6,
  in which he swears he never heard of, saw, or condoned any poisoning. Minor
  fixes only in this quoted block: `weis` kept as printed (period-appropriate
  spelling variant, not modernized); no misreads of substance found — this
  portion of the raw OCR was comparatively clean.
- PDF p.24 main-text portion (`Euriphon iſt zu timid...`): minor f/ſ and
  consistency fixes only (`waͤre`, `ſie`, `koͤnnte`, `ſey`), nothing
  structurally notable.
- PDF p.25: `Wo nicht, ſo ſage ich ihnen` and similar — minor f/ſ throughout;
  `Praefecturen` kept as printed (Latin-influenced spelling, not modernized to
  "Präfekturen"). Letter 3 closes here ("Ihr Spartacus.") and letter 4 begins
  immediately ("4. Sp. M. S. d.", opening with a Latin proverb: "Facile cum
  valemus, ægrotis conſilia damus" — "It is easy to give advice to the sick
  when we ourselves are well").

**Handling note**: per this project's standing practice (see the Anhang's
handling of the Aqua Toffana/Ajax material), this is documented factually —
what the letter itself says (an oblique, ciphered reference, decoded by the
Nachtrag's own footnote), and what the surrounding editorial commentary
explicitly accuses Weishaupt of, are kept clearly distinct rather than
merged into a single narrative. The accusation itself (incest, attempted
abortion) is the *publisher's* hostile framing in a document explicitly
designed to discredit Weishaupt — a real, historically attested controversy,
but its specifics (whose child, exact circumstances) are not established by
this letter alone and should not be treated as settled without independent
secondary-source verification. See
`annotations/nachtrag_1787/nachtrag_1787_annotations.md` for the full
annotation.

## PDF pages 26-29 (printed "18"-"21"): letters 4-6 continue, all still to
correspondents about the same family matter

**Structural note**: letter 4 ("4. Sp. M. S. d.", opened on PDF p.21) closes
on PDF p.26 addressed to "Marius" — so letters 3 and 4 are *both* to Marius;
"M" in the header abbreviation is very likely his initial (matching "C" for
a different, not-yet-identified recipient in letter 5's "Sp. C. S. d."
header). Letters 4, 5, and 6 all continue discussing the sister-in-law
situation in some way (arranging lodging for her in Sandersdorf, asking a
correspondent to keep "das ſtrengſte Stillſchweigen" — the strictest silence
— about "meiner Sch." [Schwägerin]), confirming this isn't confined to one
letter — see updated annotation.

- PDF p.26: `ficht: bar` → `ſichtbar` (spurious colon + split, same recurring
  bug pattern); `thäte` → `thaͤte`; `fie ſich` → `ſie ſich`; `ndthig` →
  `noͤthig` (misread)
- PDF p.27: `1783+` → `1783.` (misread); `für` → `fuͤr`; `V= ==` → `V===` —
  another redacted name (third so far, after p.15 and p.19 — see glossary);
  `feine Verzögerung` → `ſeine Verzoͤgerung`; `bieffe Wohnung` → `bloſſe
  Wohnung` (misread — "bare/mere lodging")
- PDF p.28: `weiß", von wem fie find` → `weiß, von wem ſie ſind` (stray quote
  mark + f/ſ x2); `B.= =` → `B.==` — another redacted name (**flagged**,
  exact dash count uncertain at this resolution, as with the earlier ones);
  `Bücher` → `Buͤcher`; `A = =` → `A==`, `DO ==: G =: von S = =` → `D== G==
  von S===` — a cluster of **three more redacted initials in one sentence**
  (a mailing address routed through intermediaries) — **flagged**, dash
  counts read as carefully as possible but not fully certain
- PDF p.29: `Septb:` → `Septb.` (colon should be period); `if Ergebenſter` →
  `Ergebenſter` (stray "if" noise); `den O` → `den ☉` — **third confirmed
  instance** of this document's Order symbol (after PDF p.9 and p.15),
  strengthening confidence this is a real, consistent glyph rather than a
  one-off OCR artifact
- Letter 6 opens with a Latin epigraph, `Qui fit, ut voluptatem dolor comes
  ſequatur?` ("How does it happen that pain follows as pleasure's
  companion?") — a real classical quotation (Horace), transcribed as printed,
  not independently verified against a source edition

## PDF pages 30-33 (printed "22"-"25"): letter 6 closes, a short unlabeled
paragraph, then letter 7 begins

**Structural note**: letter 6 closes on PDF p.30 with just "Sp." (no
"ganz eigner" flourish this time). Immediately after, a short
**unlabeled/unnumbered paragraph** appears ("Ich wuͤnſchte mit ihnen
muͤndlich zu ſprechen...") before letter 7's heading — confirmed by direct
image inspection, not a page-break artifact. Unlike every other letter in
this document so far, it carries no number and no "Sp. X. S. d." header.
Kept as its own paragraph rather than merged into letter 6 or 7, since the
page image shows it standing alone between them.

- PDF p.30: `fällig` → `faͤllig`; `wo ich fie am` → `wo ich ſie am`; `des Os`
  → `des ☉s` — **fourth confirmed instance** of the Order symbol; `ha be` →
  `habe` (spurious split); `fie wohl` → `ſie wohl`
- PDF p.31: `ss wuͤnſchte` → `Ich wuͤnſchte` (drop-cap "I" doubly misread);
  `mündlich` → `muͤndlich`; `(Os` → `☉s` — fifth instance; `verſtehen fie` →
  `verſtehen ſie`; `Præefectur` → `Præfectur` (doubled "e", OCR artifact of
  the æ ligature). **Flagged, not resolved**: this document's Latin loanword
  for "prefecture" appears as `Praefecturen` (no æ ligature) on PDF p.25 but
  `Præfectur` (with æ ligature) here — could be genuine print inconsistency
  or my own transcription inconsistency between sessions; not worth a
  retroactive fix but worth a second look if this word matters for a
  citation.
- PDF p.32: `Cenforius` → `Censorius` (f/ſ confusion on a Latin/Roman proper
  name set in antiqua type, not Fraktur — same misread pattern, different
  typeface); `Czremonien` → `Cæremonien` (æ misread as z, same pattern as
  PDF p.18's "Ceeremonien"); `téte à tete` → `tête à tête` (French accents,
  read as carefully as the image allows); `III. minor` → `Ill. minor`
  (roman-numeral misread, same pattern as PDF p.9/17/20); `Progreſlen` →
  `Progreſſen`
- PDF p.33: `feinigen`, `fie werden fehen`, `fie koͤnnen` → `ſeinigen`/`ſie
  werden ſehen`/`ſie koͤnnen` (f/ſ); `ers halte` → `erhalte` (spurious
  split); `IIl. major` → `Ill. major`; `Uliſles` → `Uliſſes` — **a new code
  name** ("Ulysses"), not yet in the glossary (see update)

## PDF pages 34-37 (printed "26"-"29"): letter 7 continues and closes, letter
8 begins; two passages under physical wax-seal damage

**Physical damage note**: PDF pages 35-36 have a real red wax seal stamped
on the physical page (visible in the scan itself, not a scanning artifact),
partially obscuring the text under and around it. Two reconstructions were
needed:
- p.35: raw OCR had `Wenn mir Marius ſeinen ganzen — phon ſchicken wollte`,
  which looks like a redacted name (em-dash) but **is not** — direct image
  inspection shows this is "Xenophon" (the classical Greek historian), with
  an ornate/historiated capital "X" that the OCR mistook for a dash and
  "eno" lost entirely. Corrected to `ſeinen ganzen Xenophon ſchicken wollte`
  — makes full sense in context (he's asking Marius to lend him a copy of
  Xenophon's works, right before mentioning he's cramming Greek). **This
  page also has red wax-seal staining directly over `Güte` in "auf die
  [Güte] der Sache erwecket"** — reconstructed from partially visible
  letters plus lexical fit; flagged, not fully certain.
- p.36: raw OCR had `Ich hoffe, wir ſollen an ih n er gut geleitet und
  erhalten wird, einen der erſten Enthuflaſten erhalten` — the gap between
  "ih" and "n er" sits exactly under the wax seal in the image. Reconstructed
  as `an ihn, wenn er gut geleitet und erhalten wird` — "wenn" (if) fills the
  grammar cleanly and fits the sentence's conditional structure. **Flagged**:
  a genuine physical-damage reconstruction, not a plain misread; worth a
  second look at higher resolution or against another exemplar of this
  printing if this sentence is ever quoted directly. Also `Enthuflaſten` →
  `Enthuſiaſten` on the same page (ordinary f/ſ, unrelated to the seal).

- PDF p.34: `K F` → `R†` (misread; a small dagger/cross mark after "R",
  appears twice identically — **flagged**, not clear what it denotes,
  possibly an abbreviation for "Rosenkreuzer" or similar, not guessed at
  further); `Difcours` → `Discours`; `Ber: faſſung` → `Verfaſſung` (misread +
  spurious colon); `fimulieren` → `ſimulieren`; `Reformiften` →
  `Reformiſten`; `würde, Was` → `wuͤrde. Was` (comma should be period);
  `fie?` → `ſie?`; `fagen fie` → `ſagen ſie`
- PDF p.36 (continued): `eingeſchoſfen` → `eingeſchoſſen`; `beym O` → `beym
  ☉` (7th confirmed instance); `einen O` → `einen ☉` (8th); `den O; denn` →
  `den ☉; denn`
- PDF p.37: `Muſus` → `Musæus` (æ ligature misread as plain u); `III. major`
  / `III. maj.` → `Ill. major` / `Ill. maj.` (recurring roman-numeral
  misread, now seen many times); `[ unter ihrer Direction` → `▢ unter ihrer
  Direction` and `zwey [I theilen` → `zwey ▢▢ theilen` — the same hollow-box
  glyph from PDF p.17 and p.20, now with enough repetition (singular box
  with "die ganze ▢", paired boxes with "zwey ▢▢") to **hypothesize** it
  stands for a feminine singular noun like "Loge" (lodge) — grammar fits
  cleanly each time, but this is a hypothesis, not a confirmed reading; see
  updated annotation. `Ulyfles` → `Ulyſſes` — note this document spells the
  same code name two different ways (`Uliſſes` on PDF p.33, `Ulyſſes` here);
  kept both as printed rather than forced to one spelling, per this
  project's preserve-as-printed convention.

## PDF pages 38-41 (printed "30"-"33"): letter 8 continues, letter 9 begins;
a recruitment-pyramid diagram

**PDF p.40 finding**: the raw OCR's `O N . PAS O 0 O 8 / e „ FE o 0 2 O / [u
/ O 50 SAD Den) / O / 0000 00 00 00 00 00` noise block is not corrupted text
at all — it's a **pyramid/tree diagram** (circles connected by lines, one
circle at top, doubling to two, four, eight, sixteen across five levels),
illustrating the exact recruitment structure the very next paragraph
describes in words ("Ich habe zwey unmittelbar unter mir... und von dieſen
zweyen hat wieder jeder zwey andere, und ſo fort"). Described in the
corrected text rather than transcribed as garbage, consistent with how
non-text elements are handled elsewhere in this corpus.

- PDF p.38: `dem O ein und derſelbe Korper` → `dem ☉ ein und derſelbe
  Koͤrper` (9th ☉ instance); `zwey []` → `zwey ▢▢`, `andere [I hinunter` →
  `andere ▢ hinunter`, `eigene [J` → `eigene ▢` — **three more instances**
  of the hollow-box glyph, all fitting the "Loge" (lodge) hypothesis exactly
  ("zwey Logen wäre das Beste", "in die andere Loge hinunter", "eine eigene
  Loge errichten"); `Rofe croix` → `Roſe croix`; `fo weiter` → `ſo weiter`;
  `Receptiong= Geldern` → `Receptions-Geldern`; `können`/`fie find noch
  keine Macons: fie muͤßen` → `koͤnnen`/`ſie ſind noch keine Maçons: ſie
  muͤßen` (f/ſ, missing cedilla); `III. maj.` → `Ill. maj.`; `Ulyfies` →
  `Ulyſſes`
- PDF p.39: `Reprochengettln` → `Reprochenzettln` (uncertain word, not a
  standard term I recognize — kept as read, flagged, not interpreted);
  `verweifen fie` → `verweiſen ſie`; `von Os Mitgliedern` → `von ☉s
  Mitgliedern` (10th instance); `ift davon der Cheff` → `iſt davon der
  Cheff`
- PDF p.40 (below diagram): `III. min.` → `Ill. min.`; `des Os: beym O` →
  `des ☉s: beym ☉` (11th and 12th instances); `um ſie nicht zu Pre)` → `um
  ſie nicht zu profaniren,` (badly garbled, restored from image); `Borfällen`
  → `Vorfaͤllen` (misread B/V)
- PDF p.41: `Ser überführt` → `Wer uͤberfuͤhrt` (misread); `fälfchlich` →
  `faͤlſchlich`; `durch den ganzen als Infam` → `durch den ganzen ☉ als
  Infam` (13th instance — **this time the OCR dropped the symbol entirely**
  rather than mangling it into a character, a new failure mode for this
  glyph worth noting); `Korper` → `Koͤrper`; `im O ungleich` → `im ☉
  ungleich` (14th instance); `9 88e Gelehrte` → `groͤßere Gelehrte` (heavily
  garbled); `Aber ſie 5 es gewiß nicht,` → `Aber ſie ſind es gewiß nicht,`

With 14 confirmed ☉ instances and 6 confirmed ▢/▢▢ instances now, both
symbols are firmly established as real, recurring printed conventions in
this document rather than one-off OCR noise.

## PDF pages 42-45 (printed "34"-"37"): letter 8 closes, letter 9 begins

- PDF p.42: `auch findet nicht, wenn er ganz verrathen` → `auch ſchadet
  nicht, wenn er ganz verrathen` — a real misread, not just f/ſ (`findet`
  doesn't fit the sentence, `ſchadet` — "it also doesn't hurt/matter" —
  does); `der ganze O` → `der ganze ☉`; `Refourcen` → `Reſourcen`;
  `ſchopfen` → `ſchoͤpfen`
- PDF p.43: `beym (O` → `beym ☉` (15th instance); `wenn ſie ſich im durch`
  → `wenn ſie ſich im ☉ durch` — **another full omission** of the symbol
  (16th instance, third time it's been dropped rather than mangled — see
  glossary); `Scipio mein .` → `Scipio mein Compliment.` — a whole word
  ("Compliment") dropped by the OCR, only caught by checking the image
- PDF p.44: `9 Sp. . 8. d:` → `9.` / `Sp. C. S. d.` (badly garbled letter
  heading, restored from image); `find III. min,` → `ſind Ill. min.`;
  `Derſammlung` → `Verſammlung`; `wegen der [` / `bis die []` → `wegen der
  ▢` / `bis die ▢` — two more hollow-box instances (7th, 8th)
- PDF p.45: `bis A =` → `bis A==` — another redacted name; `feparatim` →
  `ſeparatim`; `Diefer`/`Enthufiafmus` → `Dieſer`/`Enthuſiaſmus`;
  `Ceremonien geführt` → `Cæremonien gefuͤhrt`; `Ul. Verſammlung` → `Ill.
  Verſammlung` (yet another spelling of the same recurring roman-numeral
  misread — "Ul." here instead of "III."); `hätten...fo ſehr diftrahiert
  wären` → `haͤtten...ſo ſehr diſtrahiert waͤren`

## PDF pages 46-49 (printed "38"-"41"): letter 9 closes, letter 10 begins

- PDF p.46: `konnen` (x2) → `koͤnnen`; `Ul. Verſammlung` → `Ill. Verſammlung`
  (recurring roman-numeral misread); `Alkred` → `Alfred`; `Sphere` →
  `Sphære`; `dulden fie` → `dulden ſie`; `größte Männer,` → `groͤßte
  Maͤnner.` (comma should be period); `Gottingen` → `Goͤttingen`
- PDF p.47: `in die [J aufgenommen` → `in die ▢ aufgenommen` (9th hollow-box
  instance); `fol D = =` → `ſoll D==` (f/ſ, redacted name); `Capital Mann`
  → `Capital-Mann`; `übel: ſten Ruf` → `uͤbelſten Ruf` (spurious colon);
  `find das für` → `ſind das fuͤr`; `opferen dem O zu lieb` → `opferen dem
  ☉ zu lieb` (17th ☉ instance); footnote `fo feine Schuler` → `ſo ſeine
  Schuͤler`
- PDF p.48: `A = =` → `A==` (redacted name); `ware` → `waͤre`; `dazu ger
  macht` → `dazu gemacht` (spurious split); `f e mir` → `ſie mir` (garbled)
- PDF p.49: `uͤberſaudten` → `uͤberſandten`; `fein Syſtem, feine Gedanken
  Reihe` → `ſein Syſtem, ſeine Gedanken-Reihe`; `Manufeript von III. minor`
  → `Manuſcript von Ill. minor`; `Too Schlöffern` → `100 Schloͤſſern`
  (misread "100" as "Too"); `erhalten Tonnen` → `erhalten koͤnnen` (heavily
  garbled); `zu Vinculieren` → `zu vinculieren`. **Heavier reconstruction,
  independently verified at 600 DPI before committing**: raw OCR's `noch
  zwey eigene 0 durch welche Athen u ift,` → `noch zwey eigene ſind, durch
  welche Athen verfallen iſt.` — two separate misreads in one short
  sentence (`0`→`ſind`, dropped word `verfallen` replaced by stray `u`);
  confirmed by cropping and zooming the specific region rather than trusting
  the 300 DPI first pass, since this was a multi-word reconstruction, not a
  single-character fix. `Daß fie niemalen 1 gefehlt` → `Daß ſie niemalen
  wollen gefehlt` (f/ſ + misread); `Sottile` → `Sottiſe` (French loanword,
  "blunder/folly")

## PDF pages 50-53 (printed "42"-"45"): letter 10 continues — a long
polemical passage on Order discipline and finances

- PDF p.50: `dem edlen 5 = =` → `dem edlen F==` (misread "F" as "5" —
  another redacted name); `Leſen fie` → `Leſen ſie`; `aller groſſer Maͤnner
  im O.` → `...im ☉.`
- PDF p.51: `wihdigen` → `wuͤrdigen` (misread); `mit ſchuldigen und
  unſchuldigen — — — als` — a triple-dash redaction applied to a
  description/category rather than a single name (different usage than the
  usual single-name redactions catalogued in the glossary — worth noting as
  a variant of the same convention); `den randigen Fuß` → `den brandigen
  Fuß` (misread — "brandig" [gangrenous] fits the surgical metaphor,
  "randig" isn't a word); `fo unbillig ſeyn` → `ſo unbillig ſeyn`;
  `IIlluminat` → `Illuminat` (doubled-capital misread, recurring pattern)
- PDF p.52: `mein Hände` → `meine Haͤnde` (agreement + consistency);
  `Lumperleute find` → `Lumperleute ſind`; `Sind keiner Diſciplin fähig`
  → `ſind keiner Diſciplin faͤhig` (wrongly capitalized mid-sentence,
  lowercased; consistency)
- PDF p.53: `zum O in der Pr&parations = Klayfe` → `zum ☉ in der
  Præparations-Klaſſe`; `der O nach` → `der ☉ nach`; `Das waͤre kein O,`
  → `Das waͤre kein ☉,` — three more ☉ confirmations on one page.
  Standardized "Praeparations-" to "Præparations-" (æ ligature) to match
  this document's own spelling of the same ligature elsewhere
  (Præfectur, Cæremonien).

## PDF pages 54-57 (printed "46"-"49"): letter 10 closes, an unlabeled
paragraph, letter 11 begins

- PDF p.54: `über eine General- Beicht` → `uͤber eine General-Beicht`;
  `Iluminat. mat.` → `Illuminat. maj.`; `pon der Gemaͤchlichkeit` → `von
  der Gemaͤchlichkeit` (misread p/v); `laſd ſen` → `laſ-` (hyphenated
  word split across the page break)
- PDF p.55: `III. minor` → `Ill. minor`. Letter 10 signs off `Sparcacus.`
  — kept as printed (both the raw OCR and my own image read agree on this
  spelling, likely a genuine printer's typo for "Spartacus" rather than a
  misread, since two independent processes converged on it). **Checked and
  ruled out a false lead**: "Arminius" (this page) initially looked like it
  might be the same person as "Armenium" (PDF p.44, same hostile
  description pattern — "unerträglich, eigensinnig, eitel") — re-examined
  PDF p.44 at 600 DPI and confirmed it does say "Armenium," not a misread
  of "Arminius." Could still be the same person under two spellings, or two
  different people — flagged in annotations, not merged. `Fleéti neſeius`
  → `Flecti neſcius` (Latin, "not knowing how to bend/yield" — misread);
  `ſeynd der O.` → `ſeynd der ☉.`
- PDF p.56: `fey der O ſchon zu Ende` → `ſey der ☉ ſchon zu Ende`; `beym
  OO meldet, fo laſſen` → `beym ☉ meldet, ſo laſſen`; `gehdren` →
  `gehoͤren`. Footnote: `Univerfitzt` → `Univerſitæt`. This footnote is
  another instance of the Nachtrag's hostile editorial voice, this time
  directly calling Weishaupt a "Verführer" (corrupter/seducer) of young
  university men through hypocrisy — see updated annotation.
- PDF p.57: `gewöhnen fie` → `gewoͤhnen ſie`; `des Os am beßten` → `des
  ☉s am beßten`; `können einen nicht Lügen` → `koͤnnen einen nicht
  Luͤgen`; `III. minor.` → `Ill. minor.`; footnote continuation `Fund zu
  verkleiſtern` → `und zu verkleiſtern` (misread), `in fein Garn` → `in
  ſein Garn`. A stray `D` before the catchword `ter-` is page-transition
  noise (likely a gathering/signature mark), not body text.

## PDF pages 58-61 (printed "50"-"53"): a French block quotation from
Machiavelli, and further ☉/▢ confirmations

- PDF p.58: `ich kaun keine` → `ich kann keine` (misread); `M. X. X.`
  (capitalized) → `M. x. x.` (lowercase, matching the image); `als O Grad`
  → `als ☉ Grad`; `III. minor M. x.` → `Ill. minor M. x.`; `Graden des O:`
  → `Graden des ☉:`; `fie haben` → `ſie haben`
- PDF p.59: `Syſtemso.` → `Syſtems.` (stray "o" noise). **The French block
  quotation from Machiavelli was substantially reconstructed from the
  image** — raw OCR mangled nearly every word of it (e.g. `n'eft` for
  `n'eſt`, `afiez` for `aſſez`, `fans` for `ſans`, `fi` for `ſi`). Read
  directly from a clean antiqua-type block on the page and transcribed in
  full, preserving this print's own long-s usage in French too. **Not
  independently verified against a critical edition of Machiavelli's French
  translation** (Discours sur la première décade de Tite-Live, Book 1,
  Chapter 9, per the citation) — transcribed as legible, flagged as
  unverified for anyone using this as a citable quotation. `erhalten
  konnen` → `erhalten koͤnnen`
- PDF p.60: `arbreiten` — kept as printed; doesn't obviously resolve to a
  standard German word in context, but both the raw OCR and my own image
  read agree on this spelling, so likely a genuine period print oddity
  rather than a misread — **flagged**, not silently corrected to "arbeiten"
  since I can't confirm that's actually what's printed. `Gebäude` →
  `Gebaͤude` (consistency); `L= = =` → `L===`, `S= =` → `S==` (two more
  redacted names)
- PDF p.61: stray `n` in `wo man n ſo wenige` removed (noise); `des (Os
  hören` → `des ☉s hoͤren`; `Beförderung` → `Befoͤrderung`; `Os
  Verfaſſung` → `☉s Verfaſſung`; `die [ mit Leuten` → `die ▢ mit Leuten`

## PDF pages 62-65 (printed "54"-"57"): letter 11 closes, letters 12-13
begin; a second French block quotation (Raynal on Cortez)

- PDF p.62: `fie denn bishero D= = =` → `ſie denn bishero D===`;
  `Beneftziat` → `Beneficiat` (a church-benefice term, misread); `fit
  altiflimus` → `fit altiſſimus` (Latin, kept "fit" as printed — genuine
  Latin word, not an f/ſ error); `ſpecidſen` → `ſpecioͤſen`; `Univerfität`
  → `Univerſitaͤt`; `Sr = Der` → `S=== Der` (garbled redacted name);
  `unmoglich` → `unmoͤglich`; `Ulyffes` → `Ulyſſes`
- PDF p.63: `folche wieder` → `ſolche wieder`. Note: raw OCR's fragment `ca
  au thun` (seen in an earlier, noisier scan of this region) resolved
  cleanly to `Meldung zu thun` once read directly from the image — the
  earlier fragment was apparently a badly garbled OCR pass, not something
  genuinely present on the page.
- PDF p.64: letter 13's header spells out `Sp. Celſo S. d.` instead of the
  usual abbreviated `Sp. C. S. d.` — **confirms "C." elsewhere in this
  letter series stands for Celsus**, resolving an open question from
  earlier in the correction log (see glossary update). `Bavarie` →
  `Bavariæ` (æ ligature)
- PDF p.65: **second French block quotation, from Raynal on Cortez**,
  reconstructed from a clean antiqua-type block (raw OCR had mangled it
  almost completely, e.g. `defpote` for `deſpote`, `eruel` for `cruel`,
  `fuccés` for `ſuccés`). Transcribed as legible; **not independently
  verified against a critical edition of Raynal's *Histoire des deux
  Indes*** (the likely source, given the subject and era) — flagged as
  unverified, same caveat as the Machiavelli quotation on PDF p.59.

## PDF pages 66-69 (printed "58"-"61"): Raynal quote concludes, a second
diagram, and the "daͤrfen"/"Prærogativ" spelling notes

- PDF p.66: French quote conclusion cleaned up against the image
  (`qualites`→`qualités`, `heroigues`→`héroïques`, `fa memoire fera fans
  reproche`→`ſa mémoire ſera ſans reproche`, `Ceſur nè`→`Céſar né` [a
  significant misread — "Caesar", not a garbled non-word], `quinzieme
  fiecle`→`quinzieme ſiécle`, `eut ete`→`eut été`). German portion:
  `leſuiten` → `Jeſuiten` (misread capital J).
- PDF p.67: `des O` → `des ☉` (another confirmation); `gnt ausgefuͤhrt` →
  `gut ausgefuͤhrt`; `Enthuflaſten` → `Enthuſiaſten`.
- PDF p.68: **a second diagram**, this one a labeled hierarchy tree (a
  top circle branching to "a" circles, then "b"/"c" circles, then a row
  of individual circles) illustrating the "a, b, c" chain-of-command
  explanation in the following paragraph — raw OCR turned it into letter
  noise, described instead of transcribed, same treatment as the PDF
  p.40 pyramid diagram. `Flügel-Adjutanten` → `Fluͤgel-Adjutanten`
  (consistency).
- PDF p.69: `A- -` → `A--` (redacted name). **Resolved, not flagged
  further**: "daͤrfen" (seen here and earlier, e.g. PDF p.22) is this
  print's own consistent spelling of "dürfen" (ä for ü) — recurring
  enough now to treat as a genuine period spelling variant rather than a
  misread, no longer worth individually flagging each instance.
  `Prærogativ` and `Canditaten` kept as printed (the latter likely a
  printer's typo for "Candidaten," but both the raw OCR and my own image
  read agree on it, so not silently "corrected" to the expected word).

---

## PDF pages 70-73 (printed "62"-"65"): end of letter 13, a new "Notanda"
list, and the first appearance of "Muſæus"

- PDF p.70: `Has ben` → `haben` (OCR corrupted the line-final "ha-/ben"
  hyphen break into a spurious capital "H" + "s"); `gewis` → `gewiß`;
  `DO! es` → `O! es` (stray leading "D"); `iftis` → `iſtis`; `im Z.` →
  `im ☉.` (another Order-symbol misread, this time as "Z"); `Nuancen` →
  `Nüancen` (umlaut per the image); `dieſes 1 gewußt` → `dieſes beſſer
  gewußt` (whole-word misread as the digit "1" — same failure pattern
  as the main volume's dropped "des" and Anhang's dropped "Dero");
  `Jefuiten` → `Jeſuiten`; trailing `O.` →
  `☉.` ("der Jeſuiten ☉" — the Order symbol used to mean "the Jesuits'
  order," not just this Order, a usage worth noting).
- PDF p.70/71 boundary: raw OCR shows a stray `glau⁃` fragment plus a
  bare `63` between "...der Jeſuiten ☉. Ich" and "glaube auch, daß...".
  Confirmed against both page images this is a printer's catchword
  (previewing the next page's opening, here in abbreviated/hyphenated
  form) plus the page number, not real body text — dropped, matching
  how the PDF p.69 transition's `da`/`C` fragments and the Anhang's
  catchword noise were already handled. Same pattern recurred at the
  p.71/72 boundary (`Ge⁃` / `ſchmack` / `64` / `ſchmack ſind...` — here
  the catchword happens to equal the true hyphen continuation, since
  "Geſchmack" itself was mid-word at the page break) and p.72/73
  (`2.0` / `65` / `2.) Das Schreiben...` — even a numbered-list marker
  can be echoed as a catchword). Worth remembering as a general rule for
  the rest of this document: **any short fragment + bare number sitting
  between two page markers is almost certainly catchword + page-number
  noise, not missing text** — verify against both adjacent page images
  before treating it as content.
- PDF p.71: `Mx x` → `M x x` (spacing only; same unresolved coded
  abbreviation flagged before as "M. x. x." — not yet decoded); `Iluminatus`
  → `Illuminatus` (missing "l"); `der O lieb` → `der ☉ lieb`; `des O',` →
  `des ☉,`; `feiner Verbreitung` → `ſeiner Verbreitung`; `Delicatellen` →
  `Delicateſſen` (misread double-s as "ll" — a real word this time, not
  the nonsense "Delicatellen").
- PDF p.72: `amfrer` → `unſrer` (significant misread, not just f/ſ);
  `Geſichts⸗ Pune` → `Geſichtspuncte` (OCR both mangled "Puncte" to
  "Pune" and failed to rejoin the line-break hyphen — corrected and
  dehyphenated as one compound word, consistent with this print's
  compounding); `eis nerley` → `einerley`; `[yſtematiſch` → `ſyſtematiſch`;
  `in Osſachen` → `in ☉sſachen` (☉ standing in for "Orden-" inside a
  compound, "Ordensſachen" — a new usage pattern for the symbol, mid-word
  rather than standalone); `corri-— girt` → `corrigirt` (dehyphenated,
  stray em-dash artifact removed); `wenden will, Das haben` → `wenden
  will. Das haben` (punctuation — capital "Das" confirms a sentence
  break, not a comma splice); `beantworten:` → `beantworten.` (same
  reasoning, new paragraph follows).
- PDF p.73: **"Muſæus" appears for the first time**, badly mangled by
  OCR as `Mufzus` — corrected against the image (`Muſæus den Ill.
  Major`, another confirmed "III."→"Ill." Illuminatus misread, per the
  pattern noted since PDF p.44). `une ter` → `unter` (OCR split the word
  with a spurious "e"); `[II zu errich-ten` → `▢▢ zu errichten`
  — **this is the clearest support yet for the "▢▢ = Loge" hypothesis**:
  "worinn ich ihn nach ihrem Willen auffodere, ▢▢ zu errichten" reads
  naturally as "...urging him, per their wish, to establish a ▢▢" —
  "eine Loge zu errichten" ("to establish a lodge") is a completely
  ordinary, grammatical phrase here, more directly supportive than the
  earlier grammar-fit instances. Still keeping the hypothesis flagged
  rather than silently resolved, per the project's uncertain-reading
  standard, but confidence is now high.

---

*(Continuing from PDF page 74 in a future session. Mid-sentence: "Wenn's ſo fort geht, und noch aͤrger" — a
catchword-fragment "an=" was visible at the bottom of PDF p.73, likely
previewing something like "anwaͤchſt"; not yet confirmed against the
PDF p.74 image.)*
