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

*Last updated: 2026-03-25*
