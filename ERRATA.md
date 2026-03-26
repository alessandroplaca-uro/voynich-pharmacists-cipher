# Errata — Placa (2026) v1.1

Known errors in:

> Placa, A. (2026). *The Pharmacist's Cipher: Six Statistical Tests Supporting
> a Pharmaceutical Reading of the Voynich Manuscript (MS 408)*.
> Preprint v1.1. https://doi.org/10.5281/zenodo.19197846

---

## E1. Result 6 — Two-tailed p-value

**Location:** Section 6.3, Results, final paragraph.

**Published text:** "Exact permutation test: p = 0.042 one-tailed, p = 0.050
two-tailed."

**Error:** The two-tailed p-value is incorrect.

**Correct values:**
- One-tailed: p = 5/120 = **0.042** (correct as published)
- Two-tailed: p = 10/120 = **0.083** (not 0.050)

**Derivation:** With n = 5 and observed ρ = 0.900 (Σd² = 2), the
two-tailed test counts all permutations where |ρ| ≥ 0.900:

- Permutations with ρ ≥ 0.9 (Σd² ≤ 2): the identity permutation (Σd²=0)
  plus the 4 adjacent transpositions (Σd²=2 each). Total: **5**.
- Permutations with ρ ≤ −0.9 (Σd² ≥ 38): the reverse permutation (Σd²=40)
  plus its 4 adjacent transpositions (Σd²=38 each). Total: **5**.
- Combined: 10/120 = 0.0833.

**Impact:** The one-tailed p = 0.042 is unaffected and remains significant
at α = 0.05. The directional hypothesis (higher solvent volume → higher
ee-frequency) was specified before the rank comparison, making the one-tailed
test the appropriate primary statistic. The sentence in section 6.4
(Important caveats) stating "The two-tailed p = 0.050 is at the conventional
significance boundary" should read "The two-tailed p = 0.083 does not reach
conventional significance, though the one-tailed p = 0.042 does."

**This error does not change any of the paper's conclusions.** Result 6 was
already flagged as exploratory, and the one-tailed test (the primary statistic
for a directional hypothesis) is correct.

---

## E2. Result 3 — Line-initial rate in AI Verification Guide

**Location:** AI_VERIFICATION_GUIDE.md, Result 3 expected ranges.

**Published text (Guide v1.3):** "Line-initial rate of A tokens in Stars:
~86.7%"

**Error:** The 86.7% line-initial rate is incorrect.

**Correct value:** ~59% (16 of 27 occurrences at position 0).

**Replication method:** Independent replication on `IT2a-n.txt` (Takahashi
transcription, IVTFF 2.0), performed 2026-03-26. The replication finds
27 total occurrences of Pharma folio identifiers in Stars (vs 26 in the
paper — a difference of 1, likely due to minor parsing edge cases with
`?`/`!` stripping). Of these 27 occurrences, 16 appear at position 0
(first token of their IVTFF line), yielding a line-initial rate of 59.3%.

**Detail of non-position-0 matches:**

| Token   | Location    | Position |
|---------|-------------|----------|
| kshedy  | f104r.18    | 6/7      |
| pcheey  | f105r.24    | 9/13     |
| tor     | f105v.29    | 1/11     |
| tchedy  | f106r.15    | 3/9      |
| kshedy  | f106v.11    | 4/12     |
| tor     | f111v.37    | 6/11     |
| tchedy  | f112v.45    | 4/11     |
| pcheol  | f113v.15    | 7/12     |
| pcheol  | f113v.25    | 4/12     |
| tshedy  | f113v.36    | 4/9      |
| tchedy  | f115v.25    | 7/10     |

**Impact on the paper:** The paper itself (Section 4, preprint v1.1) does
not cite a specific line-initial percentage. It states that "header tokens
from Pharma folios appear as standalone words in Stars" and interprets this
as asymmetric lexical reuse. The core claim — the 26–27 vs 0 asymmetry —
is fully confirmed. The ~59% line-initial rate still indicates a tendency
for reused tokens to appear at line boundaries, but it is not as dominant as
the 86.7% previously stated in the guide. The term "line openers" in the
guide interpretation has been softened accordingly.

**This error does not change any of the paper's conclusions.** It affects
only the AI Verification Guide, not the preprint text.

---

*Last updated: 2026-03-26*
