# The Pharmacist's Cipher — Companion Code

Replication scripts for:

> Placa, A. (2026). *The Pharmacist's Cipher: Morphological Evidence for a
> Pharmaceutical Register in Voynich Manuscript MS 408*.
> Preprint. https://doi.org/10.5281/zenodo.19197846

---

## Repository layout

```
voynich-pharmacists-cipher/
├── scripts/
│   ├── 00_corpus_utils.py          # Shared IVTFF parser & helpers
│   ├── 01_cross_transcriber.py     # Result 1 – Cross-transcriber stability
│   ├── 02_paradigm_gap.py          # Result 2 – Binary morphological gap
│   ├── 03_asymmetric_reuse.py      # Result 3 – Asymmetric cross-section reuse
│   ├── 04_positional_constraint.py # Result 4 – Positional ordering constraint
│   ├── 05_section_profiles.py      # Result 5 – Section morphological profiles
│   ├── 06_volume_hierarchy.py      # Result 6 – ee-frequency volume hierarchy
│   └── run_all.py                  # Run all six scripts in sequence
├── data/
│   ├── folio_section_mapping.csv   # Folio-to-section boundaries
│   ├── prefix_definitions.json     # Prefix families and exclusion rules
│   ├── functional_categories.json  # Functional categories for Result 4
│   └── solvent_families.json       # Solvent families for Result 6
├── requirements.txt                # No third-party dependencies
└── README.md
```

---

## Requirements

- Python 3.9 or later
- No third-party packages — all scripts use the standard library only

---

## Corpus

The scripts require the **IVTFF interlinear transcription** of Voynich MS 408.
The standard file is `LSI_ivtff_0d.txt` (or any IVTFF-format corpus file).

The corpus is not distributed here. It can be obtained from:

- Landini, G., & Zandbergen, R. (1998–2024). *Voynich Manuscript Transcription
  Files (IVTFF)*. http://www.voynich.nu/

**Format notes:**
- Each line: `<fNNv.LL,@LAYOUT;T> token.token.token…`
- Token separator: **dot (`.`)**, not space
- Encoding: **latin-1**
- Transcriber codes: `H` = Takahashi, `C` = Currier
- Illegible marker: `-` (omitted from analysis)

---

## Usage

### Run a single script

```bash
python scripts/01_cross_transcriber.py /path/to/LSI_ivtff_0d.txt
```

### Run all six scripts

```bash
python scripts/run_all.py /path/to/LSI_ivtff_0d.txt
```

Output is written to stdout. Redirect to a file to save:

```bash
python scripts/run_all.py /path/to/LSI_ivtff_0d.txt > results.txt
```

---

## Scripts and expected outputs

### Result 1 — Cross-transcriber stability (`01_cross_transcriber.py`)

Compares prefix densities (‰) between the Takahashi (H) and Currier (C)
transcriptions on the lines they share. All 11 prefixes should show < 4 %
drift (ratio C/H between 0.97 and 1.03).

**Key check:** `ch/sh` ratio per section is stable across transcribers.

### Result 2 — Binary morphological gap (`02_paradigm_gap.py`)

Counts occurrences of `sedy` and `shedy` in the Takahashi transcription.

**Key check:** `sedy = 0`, `shedy ≈ 299–425`.
The s- prefix (excluding sh-) takes nominal suffixes at 108× the rate it
takes processual suffixes; sh- takes processual suffixes at 3.8× the rate
it takes nominal suffixes.

### Result 3 — Asymmetric cross-section reuse (`03_asymmetric_reuse.py`)

Checks whether first-tokens of Pharma lines appear in Stars vocabulary,
and vice versa.

**Key check:** Pharma→Stars links >> 0; Stars→Pharma links = 0.
86.7 % of linked tokens appear at position 0 in Stars lines (line-initial).

### Result 4 — Positional ordering constraint (`04_positional_constraint.py`)

Classifies tokens in procedural sections into OPER / VEIC / MAT / COMPL
and tests pairwise ordering.

**Key check:** COMPL tokens are in the final 20 % of lines > 60 % of the
time. OPER and VEIC tend to precede MAT; MAT tends to precede COMPL.

### Result 5 — Section morphological profiles (`05_section_profiles.py`)

Reports prefix densities across the six major sections and enrichment ratios
vs corpus baseline.

**Key checks:**
- Stars: `l-` enriched ~3.4×; `-edy` enriched ~1.5×; `qok-/qot-` present
- Zodiac: `ot-` enriched ~2.4×; `qok-/qot-` depleted ~0.16×
- Balneo: `ch-/sh-` near-parity (ch/sh ≈ 1.07)

### Result 6 — Volume hierarchy (`06_volume_hierarchy.py`)

Computes the ee-suffix frequency for five solvent families and tests whether
the rank matches the expected volume rank.

**Key check:** Spearman ρ should be high (≥ 0.90) with p < 0.05 (exact
permutation test, n=5, 120 permutations).
Expected rank: WATER > OIL ≈ SPIRIT > VINEGAR > MEDICINE.

---

## Standalone token matching

All prefix and suffix counts use **standalone word-boundary matching**:
tokens are the dot-delimited units of the IVTFF line. Substring matching is
never used. The helper `starts_with(token, prefix, exclude)` in
`00_corpus_utils.py` enforces this by operating on full tokens only.

---

## Licence

Code: MIT.
The Voynich manuscript images are the property of the Beinecke Rare Book and
Manuscript Library, Yale University, and are made available under a Creative
Commons licence. The corpus transcription files have their own terms of use
(see voynich.nu).

---

## Citation

```bibtex
@unpublished{Placa2026,
  author = {Placa, Alessandro},
  title  = {The Pharmacist's Cipher: Morphological Evidence for a
            Pharmaceutical Register in Voynich Manuscript {MS} 408},
  year   = {2026},
  note   = {Preprint. \doi{10.5281/zenodo.19197846}},
  doi    = {10.5281/zenodo.19197846},
  url    = {https://github.com/alessandroplaca-uro/voynich-pharmacists-cipher}
}
```
