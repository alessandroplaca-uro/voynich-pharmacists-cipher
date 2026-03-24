"""
06_volume_hierarchy.py
Result 6 – ee-suffix frequency hierarchy mirrors expected solvent volume.

Method
------
1. Load Takahashi (H) transcription.
2. Assign each token to one of five solvent families by prefix:
     WATER    : ok-, qok-
     OIL      : t- (excl. th-), qot-
     SPIRIT   : l-
     VINEGAR  : s- (excl. sh-)
     MEDICINE : da-
3. Compute the fraction of each family's tokens that contain 'ee' (ee%).
4. Rank families by ee% (descending) and compare with the expected
   volume rank: WATER > OIL ≈ SPIRIT > VINEGAR > MEDICINE.
5. Compute Spearman rho and an exact permutation p-value (5! = 120 perms).

Expected output (paper):
  Spearman ρ ≥ 0.90, p < 0.05 (exact permutation, n=5, 120 permutations).
  Expected rank: WATER > OIL ≈ SPIRIT > VINEGAR > MEDICINE.
"""

import sys
from pathlib import Path
from itertools import permutations
from math import factorial

sys.path.insert(0, str(Path(__file__).parent))
from corpus_utils import parse_corpus, starts_with

EXPECTED_VOLUME_RANK = {
    'WATER':    1,
    'OIL':      2,
    'SPIRIT':   3,
    'VINEGAR':  4,
    'MEDICINE': 5,
}
FAMILY_LABELS = ['WATER', 'OIL', 'SPIRIT', 'VINEGAR', 'MEDICINE']


def family_of(tok: str) -> str | None:
    if starts_with(tok, 'qok', []):  return 'WATER'
    if starts_with(tok, 'ok',  []):  return 'WATER'
    if starts_with(tok, 'qot', []):  return 'OIL'
    if starts_with(tok, 't',   ['th']): return 'OIL'
    if starts_with(tok, 'l',   []):  return 'SPIRIT'
    if starts_with(tok, 's',   ['sh']): return 'VINEGAR'
    if starts_with(tok, 'da',  []):  return 'MEDICINE'
    return None


def has_ee(tok: str) -> bool:
    return 'ee' in tok


def spearman_rho(rank_a, rank_b):
    n = len(rank_a)
    d2 = sum((a - b) ** 2 for a, b in zip(rank_a, rank_b))
    return 1 - (6 * d2) / (n * (n ** 2 - 1))


def permutation_p_value(observed_rho, expected_ranks, n_families):
    base_obs = list(range(1, n_families + 1))
    count = 0
    total = factorial(n_families)
    for perm in permutations(base_obs):
        rho = spearman_rho(list(perm), expected_ranks)
        if rho >= observed_rho:
            count += 1
    return count, total, count / total


def run(corpus_path: str) -> None:
    print("Loading Takahashi transcription…")
    records = parse_corpus(corpus_path, transcriber='H')
    total_tokens = sum(len(r['tokens']) for r in records)
    print(f"Total tokens: {total_tokens:,}\n")

    family_total = {f: 0 for f in FAMILY_LABELS}
    family_ee    = {f: 0 for f in FAMILY_LABELS}

    for rec in records:
        for tok in rec['tokens']:
            fam = family_of(tok)
            if fam is None:
                continue
            family_total[fam] += 1
            if has_ee(tok):
                family_ee[fam] += 1

    ee_pct = {
        fam: (family_ee[fam] / family_total[fam] * 100
              if family_total[fam] else 0.0)
        for fam in FAMILY_LABELS
    }

    sorted_by_ee   = sorted(FAMILY_LABELS, key=lambda f: ee_pct[f], reverse=True)
    observed_rank  = {fam: i + 1 for i, fam in enumerate(sorted_by_ee)}

    print("=== Volume hierarchy: ee-suffix frequency by solvent family ===")
    print(f"{'Family':<12}  {'Total tok':>10}  {'ee tok':>8}  {'ee%':>8}  "
          f"{'Obs rank':>10}  {'Exp rank':>10}")
    print("-" * 66)
    for fam in FAMILY_LABELS:
        print(f"{fam:<12}  {family_total[fam]:>10,}  {family_ee[fam]:>8,}  "
              f"{ee_pct[fam]:>7.1f}%  {observed_rank[fam]:>10}  "
              f"{EXPECTED_VOLUME_RANK[fam]:>10}")

    obs_ranks_ordered = [observed_rank[f]          for f in FAMILY_LABELS]
    exp_ranks_ordered = [EXPECTED_VOLUME_RANK[f]   for f in FAMILY_LABELS]
    rho = spearman_rho(obs_ranks_ordered, exp_ranks_ordered)
    print(f"\nSpearman ρ (observed vs expected volume rank): {rho:.3f}")

    n = len(FAMILY_LABELS)
    count_extreme, total_perms, p_val = permutation_p_value(rho, exp_ranks_ordered, n)
    print(f"Permutation test: {count_extreme} / {total_perms} permutations "
          f"have ρ ≥ {rho:.3f}")
    print(f"p-value (exact, one-tailed): {p_val:.4f}")
    if p_val < 0.05:
        print("→ Statistically significant at α = 0.05")
    else:
        print("→ Not significant at α = 0.05")

    # Per-section breakdown for WATER
    print("\n=== ee% for WATER family by section ===")
    sections = ['Herbal_A', 'Herbal_B', 'Zodiac', 'Balneo', 'Pharma', 'Stars']
    print(f"{'Section':<12}  {'Total':>8}  {'ee tok':>8}  {'ee%':>8}")
    print("-" * 42)
    for sec in sections:
        sec_total = 0
        sec_ee    = 0
        for rec in records:
            if rec['section'] != sec:
                continue
            for tok in rec['tokens']:
                fam = family_of(tok)
                if fam == 'WATER':
                    sec_total += 1
                    if has_ee(tok):
                        sec_ee += 1
        pct = sec_ee / sec_total * 100 if sec_total else 0.0
        print(f"{sec:<12}  {sec_total:>8,}  {sec_ee:>8,}  {pct:>7.1f}%")

    # Spot-check key forms
    print("\n=== Specific high-frequency forms with ee ===")
    key_forms = [
        'qokeey', 'qokeedy', 'okeey', 'okeedy',
        'cheey', 'sheey', 'qoteeey', 'lkeey', 'lkeedy',
    ]
    print(f"{'Form':<15}  {'Count':>8}")
    print("-" * 26)
    form_counts: dict[str, int] = {}
    for rec in records:
        for tok in rec['tokens']:
            if tok in key_forms:
                form_counts[tok] = form_counts.get(tok, 0) + 1
    for form in key_forms:
        cnt = form_counts.get(form, 0)
        print(f"{form:<15}  {cnt:>8,}")


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python 06_volume_hierarchy.py <path_to_ivtff_corpus.txt>")
        sys.exit(1)
    run(sys.argv[1])
