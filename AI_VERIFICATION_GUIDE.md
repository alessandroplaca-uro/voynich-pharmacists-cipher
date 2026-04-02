# AI Verification Guide — Placa (2026)

**Version 1.5 — 2026-04-02**

This guide provides structured prompts for AI-assisted replication of the six
morphological results reported in:

> Placa, A. (2026). *The Pharmacist's Cipher: Six Statistical Tests Supporting
> a Pharmaceutical Reading of the Voynich Manuscript (MS 408)*. Preprint v1.2.
> https://doi.org/10.5281/zenodo.19197846

---

## Before You Begin: Corpus Parsing Rules

Before running any verification, confirm the following with your AI assistant:

1. **Token separator is a dot (`.`), not a space.**
   Each IVTFF line has the form `<locator> token.token.token...`
   Splitting on spaces will produce concatenated garbage.

2. **Filter by transcriber tag.**
   - Takahashi: lines containing `;H>`
   - Currier: lines containing `;C>`
   All six results use Takahashi (H) as the primary transcription.

3. **Use standalone word-boundary matching.**
   A prefix match means the *full token* starts with the prefix.
   Never use substring matching across token boundaries.

4. **Strip `!` markers before analysis.**
   The `!` character marks uncertain readings within tokens; remove it before
   any prefix, suffix, or exact-match test.

5. **Omit illegible tokens.**
   Tokens equal to `-` (single dash) represent unreadable glyphs; skip them.

6. **Encoding is latin-1.** Open the corpus file with `encoding='latin-1'`.

7. **`ch` and `sh` are unitary glyphs.**
   These are "bench characters" — single graphemic units, NOT sequences of
   `c` + `h` or `s` + `h`. They share 76.5% suffix overlap with each other,
   but only 11.1% with bare `s-`. Do not decompose them morphemically.

---

## Result 1 — Cross-transcriber Stability

### Verification prompt

```
Using the IVTFF corpus file provided, load both the Takahashi (;H>) and
Currier (;C>) transcriptions. Find all lines that appear in both
transcriptions (matched by folio + line number, e.g. "f1r.1"). On those
common lines only, compute prefix densities in tokens per thousand (‰) for
the following 11 prefixes:

  ch-, sh-, da-, ok-, qok-, qot-, ot-, l-, y-, s- (exclude sh-), t- (exclude th-)

Report the ratio C/H for each prefix. Flag any ratio outside [0.97, 1.03].
Also report the ch/sh count ratio per section for both transcribers, for
sections: Herbal_A, Balneo, Pharma, Zodiac, Stars.
```

### Expected ranges

| Prefix | Ratio C/H |
|--------|-----------:|
| ch-    | 0.97–1.03 |
| sh-    | 0.97–1.03 |
| da-    | ~1.00     |
| ok-    | 0.97–1.03 |
| qok-   | 0.97–1.03 |
| qot-   | 0.97–1.03 |
| ot-    | 0.97–1.03 |
| l-     | 0.97–1.03 |
| y-     | 0.97–1.03 |
| s-     | 0.97–1.03 |
| t-     | 0.97–1.03 |

**Key check:** ch/sh ratio per section is stable across transcribers
(drift < 5% for Herbal_A, Balneo, Pharma; Zodiac and Stars may show
slightly higher drift due to smaller sample sizes).

### Interpretation

If all 11 prefixes fall within the 0.97–1.03 band, the morphological
structure is not a transcription artefact. The two transcribers worked
independently ~20 years apart; agreement at this level is non-trivial.

---

## Result 2 — Binary Morphological Gap

### Verification prompt

```
Using the Takahashi transcription, count:
  (a) exact occurrences of the token "sedy" (standalone, word-boundary match)
  (b) exact occurrences of the token "shedy"

Then classify all s- tokens (excluding sh-) and all sh- tokens by suffix type:
  - processual: token ends in edy, eedy, ey, or eey
  - nominal:    token ends in aiin, ain, ar, or al
  - other:      everything else

Report counts and percentages for each category × prefix family.
Report the ratio sh/s for processual suffixes and for nominal suffixes.

Note: sh is a unitary glyph (bench character), not s + h. The morphological
gap reflects two distinct graphemic classes.
```

### Expected ranges (from paper Table 2)

- `sedy` count: **0** (zero)
- `shedy` count: **~424**
- s- total tokens: **~1,250**
- sh- total tokens: **~3,175**
- s- processual rate: **~7.4%** (93 tokens; mostly compound forms like solchedy)
- sh- processual rate: **~33.7%** (1,070 tokens)
- Processual ratio sh/s: **~4.6×**
- s- nominal rate: **~36.5%** (456 tokens)
- sh- nominal rate: **~10.5%** (333 tokens)
- Nominal ratio sh/s: **~0.29×**

### Interpretation

The binary gap (sedy = 0, shedy ≫ 0) is the strongest single piece of
evidence that s- and sh- are functionally distinct morphemes, not
orthographic variants. A purely scribal origin would predict gradual
variation, not a binary cliff. The suffix distributions are inverted:
s- skews nominal (36.5% vs 7.4%), sh- skews processual (33.7% vs 10.5%).
The 93 processual s- tokens are predominantly compound forms (e.g.,
solchedy, schedy) where the processual suffix attaches to an intervening
element, not directly to s-.

---

## Result 3 — Asymmetric Cross-Section Reuse

### Verification prompt

```
Using the Takahashi transcription:

1. For the Pharma section (folios f87–f102), identify the "folio identifier"
   of each folio: the first token of the first transcribed line of that folio.

2. Count total occurrences of those identifier tokens as standalone tokens
   anywhere in the Stars section (folios f103–f116). Call this count A.

3. Repeat symmetrically: identify Stars folio identifiers and count their
   occurrences in Pharma. Call this count B.

4. Report A, B, the asymmetry ratio A/B, and — for the A tokens found in
   Stars — the fraction that appear at position 0 (first token of their line).
```

### Expected ranges (from paper Table 3)

- A (Pharma → Stars): **26–27 occurrences** (7 of 32 distinct folio identifiers)
- B (Stars → Pharma): **0**
- Asymmetry ratio A/B: **infinite** (26–27 vs 0)
- Line-initial rate of A tokens in Stars: **~59%** (16 of 27)

Note: Pharma has 32 folio identifiers (not 16) because some folios have
multiple sub-pages (recto + verso, or sub-folios like f90v1/f90v2).

**⚠️ Errata note (v1.4):** Previous versions of this guide reported the
line-initial rate as ~86.7%. Independent replication on IT2a-n.txt
(2026-03-26) consistently yields ~59% (16/27). The core asymmetry
(26–27 vs 0) is unaffected. See [ERRATA.md](ERRATA.md) E2.

### Interpretation

The asymmetry shows that Stars reuses Pharma identifiers, while Pharma
does not reuse Stars identifiers. A majority (~59%) of these reused tokens
appear at position 0 (line-initial), suggesting a tendency toward
cross-referencing at line boundaries, though not as dominant as previously
stated. This is compatible with a functional dependency in which Stars
draws on Pharma as a source section, not vice versa.

---

## Result 4 — Positional Ordering Constraint

### Verification prompt

```
Using the Takahashi transcription, restrict to procedural sections:
Herbal_A, Herbal_B, Pharma, Balneo.

Classify each token into one of four functional categories:
  OPER  : starts with ch-, sh-, ot- (exclude oth-), or y-
  VEIC  : starts with qok-, qot-; or starts with ok- (but not qok-);
           or is exactly "sol" or starts with "sol"
  MAT   : starts with da-; or is one of {kol, kor, kal, kar};
           or is one of {cth, ckh, cfh, cph}
  COMPL : is exactly one of {dam, sam, dy}; or ends in "am" (len > 2)

For each line with tokens in at least two categories, record the mean
normalised position (0.0 = first token, 1.0 = last token) of each category
within that line, and whether category A precedes category B.

Report:
  1. Mean normalised position per category across all qualifying lines.
  2. For each ordered pair (A, B): fraction of lines where A precedes B.
  3. Fraction of COMPL tokens that fall in the final 20% of their line
     (normalised position ≥ 0.80).
```

### Expected ranges (from paper Table 4)

- VEIC mean position: **~0.478**
- OPER mean position: **~0.484**
- MAT mean position: **~0.582**
- COMPL mean position: **~0.819**
- COMPL in final 20%: **~68.2%** (Z = 26.6)
- OPER before MAT: **~60.0%**
- MAT before COMPL: **~78.2%**
- OPER before COMPL: **> 65%**
- OPER vs VEIC: **~49.4%** (not significant; positionally interchangeable)

### Interpretation

Completion markers cluster at the end of lines (consistent with a
phrasingfinal role), while operational and vehicle tokens tend to precede
material tokens. The ordering is probabilistic, not absolute, consistent
with agglutinative syntax allowing some flexibility.

---

## Result 5 — Section Morphological Profiles

### Verification prompt

```
Using the Takahashi transcription, compute the density (tokens per thousand,
‰) of the following 14 markers in each of the six sections:
Herbal_A, Herbal_B, Zodiac, Balneo, Pharma, Stars.

Markers (prefix unless noted):
  ch-, sh-, da-, ok-, qok-, qot-, l-, y-, ot- (exclude oth-),
  s- (exclude sh-), t- (exclude th-), -edy (suffix), -am (suffix), dy (exact)

Also compute the ch/sh ratio (raw counts) per section.

Then compute enrichment ratios (section density / corpus-wide baseline)
for: l-, -edy, qok-, ot-.

IMPORTANT: Section assignment uses folio number ranges from
data/folio_section_mapping.csv, NOT the $I/$L metadata flags in the
IVTFF file. Using $I/$L flags will produce divergent enrichment values.
```

### Expected key checks (from paper Table 5)

| Section | Marker       | Expected enrichment (section/corpus baseline) |
|---------|--------------|----------------------------------------------:|
| Stars   | l-           | ~1.97×  (73.2‰ vs corpus 37.1‰)              |
| Stars   | -edy         | ~1.5×                                          |
| Zodiac  | ot-          | ~2.43×  (155.0‰ vs corpus 63.7‰)             |
| Zodiac  | qok-         | ~0.16×  (depleted)                             |
| Balneo  | ch/sh ratio  | ~1.07   (near-parity)                          |

### Interpretation

Each section has a distinct morphological fingerprint. Stars is the most
alcohol-heavy section (l- enriched 1.97× vs corpus baseline), consistent
with tincture formulae. Zodiac uses the passive marker ot- heavily
(descriptive register) while depleting process-action markers. Balneo is
the only section where hot-temperature (ch-) and cold-temperature (sh-)
bench characters reach near-parity, consistent with a pharmaceutical
processing timeline that employs multiple thermal operations across
sequential steps (P77: master multi-path workflow). The Balneo section
documents all liquid-medium processes — from cold maceration (F-gallows
opener) to digestio (F-ch variant) to distillation — not therapeutic baths.
The ch/sh near-parity reflects the alternation between heating and cooling
phases within pharmaceutical procedures.

---

## Result 6 — Volume Hierarchy (ee-frequency)

### Verification prompt

```
Using the Takahashi transcription, assign each token to one of five
solvent families based on its prefix:
  WATER    : starts with ok- or qok-
  OIL      : starts with t- (exclude th-) or qot-
  SPIRIT   : starts with l-
  VINEGAR  : starts with s- (exclude sh-)
  MEDICINE : starts with da-

For each family, compute the fraction of tokens that contain the substring
"ee" anywhere in the token (call this ee%).

Rank the five families by ee% (highest first). Then compute Spearman's rank
correlation between the observed ee% ranking and the expected volume ranking:
  WATER=1, OIL=2, SPIRIT=3, VINEGAR=4, MEDICINE=5

Also compute an exact permutation p-value: enumerate all 5! = 120
permutations of ranks 1–5, count how many achieve Spearman ρ ≥ the
observed value, divide by 120.
```

### Expected ranges (from paper Table 6)

- WATER ee%: **~23.2%** (1,278 of 5,505)
- SPIRIT ee%: **~15.3%** (210 of 1,374)
- OIL ee%: **~13.3%** (279 of 2,098)
- VINEGAR ee%: **~4.5%** (56 of 1,250)
- MEDICINE ee%: **~0.4%** (10 of 2,256)
- Spearman ρ: **0.900** (Σd² = 2, one rank swap between OIL and SPIRIT)
- p-value (exact, one-tailed): **0.042** (5 of 120 permutations)
- Expected rank order: WATER > OIL ≈ SPIRIT > VINEGAR > MEDICINE

**⚠️ Errata note:** The preprint reports p = 0.050 two-tailed. The correct
two-tailed p is 0.083 (10 of 120 permutations with |ρ| ≥ 0.9). The one-tailed
p = 0.042 is correct and remains significant. See [ERRATA.md](ERRATA.md).

### Interpretation

The ee-marker frequency mirrors the expected volume rank of solvents in
medieval pharmacy. The exact permutation test has only 120 equally likely
outcomes under the null, so ρ ≥ 0.90 yields a genuine p < 0.05 without
asymptotic approximations.

**Note on ee-suffix distribution:** The suffixes -eey/-edy/-eedy/-eol/-eody
are concentrated in ok-/ot- (water/oil) families and have near-zero
occurrence in ol-/s- families. The volume hierarchy holds as a statistical
correlation across all five families, but the underlying morphological
mechanism appears specific to the aqueous/oily context.

---

## Troubleshooting Checklist

If your numbers differ from the expected ranges above:

- [ ] **Token separator**: are you splitting on `.` (dot), not on spaces?
- [ ] **Transcriber filter**: are you filtering for `;H>` (Takahashi)?
- [ ] **s- / sh- confusion**: does your s- filter explicitly exclude tokens
  starting with `sh`? Remember: `sh` is a unitary glyph, not `s` + `h`.
- [ ] **t- / th- confusion**: does your t- filter explicitly exclude tokens
  starting with `th`?
- [ ] **ot- / oth- confusion**: does your ot- filter explicitly exclude
  tokens starting with `oth`?
- [ ] **Substring vs. standalone**: are you matching full tokens only, or
  are you doing substring search across token boundaries?
- [ ] **`!` markers**: have you stripped `!` characters before matching?
- [ ] **Encoding**: did you open the corpus with `encoding='latin-1'`?
- [ ] **Section boundaries**: folio numbers use the ranges in
  `data/folio_section_mapping.csv`. Folio f74 is absent from the manuscript.
  Do NOT use the $I/$L metadata flags from the IVTFF file — they do not
  always match the folio-range-based sections used in the paper.

---

Replication materials and analysis scripts are provided in the repository
accompanying the preprint.
