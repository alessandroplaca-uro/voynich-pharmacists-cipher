# AI Verification Guide — Placa (2026)

**Version 1.1 — 2026-03-23**

This guide provides structured prompts for AI-assisted replication of the six
morphological results reported in:

> Placa, A. (2026). *The Pharmacist's Cipher: Morphological Evidence for a
> Pharmaceutical Register in Voynich Manuscript MS 408*. Preprint.
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
|--------|-----------|
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
Report the nominal/processual ratio for s- and the processual/nominal
ratio for sh-.
```

### Expected ranges

- `sedy` count: **0** (zero)
- `shedy` count: **299–425**
- s- processual rate: < 2%
- sh- processual rate: > 40%
- s- nominal/processual ratio: **≥ 80×** (paper reports 108×)
- sh- processual/nominal ratio: **≥ 3×** (paper reports 3.8×)

### Interpretation

The binary gap (sedy = 0, shedy ≫ 0) is the strongest single piece of
evidence that s- and sh- are functionally distinct morphemes, not
orthographic variants. A purely scribal origin would predict gradual
variation, not a binary cliff.

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

### Expected ranges

- A (Pharma → Stars): **6–15 total occurrences**
- B (Stars → Pharma): **0**
- Asymmetry ratio A/B: **≥ 6×** (effectively infinite if B = 0)
- Line-initial rate of A tokens in Stars: **≥ 80%**

### Interpretation

The asymmetry shows that Stars reuses Pharma identifiers as line openers
(cross-references), while Pharma does not reuse Stars identifiers. This
suggests a directional dependency: Stars draws on Pharma as a source
section, not vice versa.

---

## Result 4 — Positional Ordering Constraint

### Verification prompt

```
Using the Takahashi transcription, restrict to procedural sections:
Herbal_A, Herbal_B, Pharma, Balneo.

Classify each token into one of four functional categories:
  OPER  : starts with ch-, sh-, ot-, or y-
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

### Expected ranges

- COMPL mean position: **0.75–0.80** (near end of line)
- COMPL in final 20%: **> 60%**
- OPER before MAT: **> 52%**
- VEIC before MAT: **> 55%**
- MAT before COMPL: **> 65%**
- OPER before COMPL: **> 65%**

### Interpretation

Completion markers cluster at the end of lines (consistent with a
phrasing-final role), while operational and vehicle tokens tend to precede
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
```

### Expected key checks

| Section | Marker       | Expected enrichment |
|---------|--------------|---------------------|
| Stars   | l-           | ~3.4×               |
| Stars   | -edy         | ~1.5×               |
| Zodiac  | ot-          | ~2.4×               |
| Zodiac  | qok-         | ~0.16×  (depleted)  |
| Balneo  | ch/sh ratio  | ~1.07   (near-parity) |

### Interpretation

Each section has a distinct morphological fingerprint. Stars is the most
alcohol-heavy section (l- enriched), consistent with tincture formulae.
Zodiac uses the passive marker ot- heavily (descriptive register) while
depleting process-action markers. Balneo is the only section where
hot-process (ch-) and cold-process (sh-) markers reach near-parity,
consistent with therapeutic baths that apply both thermal modalities.

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

### Expected ranges

- WATER ee%: **20–28%**
- OIL ee%: **12–18%**
- SPIRIT ee%: **12–18%**
- VINEGAR ee%: **3–7%**
- MEDICINE ee%: **< 2%**
- Spearman ρ: **≥ 0.90**
- p-value (exact, one-tailed): **< 0.05**
- Expected rank order: WATER > OIL ≈ SPIRIT > VINEGAR > MEDICINE

### Interpretation

The ee-marker frequency mirrors the expected volume rank of solvents in
medieval pharmacy. The exact permutation test has only 120 equally likely
outcomes under the null, so ρ ≥ 0.90 yields a genuine p < 0.05 without
asymptotic approximations.

---

## Troubleshooting Checklist

If your numbers differ from the expected ranges above:

- [ ] **Token separator**: are you splitting on `.` (dot), not on spaces?
- [ ] **Transcriber filter**: are you filtering for `;H>` (Takahashi)?
- [ ] **s- / sh- confusion**: does your s- filter explicitly exclude tokens
  starting with `sh`?
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

---

Replication materials and analysis scripts are provided in the repository
accompanying the preprint.
