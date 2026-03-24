"""
04_positional_constraint.py
Result 4 – Positional ordering constraint in procedural lines.

Method
------
1. Load Takahashi (H) transcription.
2. Restrict to procedural sections: Herbal_A, Herbal_B, Pharma, Balneo.
3. Classify each token into one of four functional categories:
     OPER  – operational / process tokens (ch-, sh-, ot-, y-)
     VEIC  – vehicle / solvent tokens (qok-, qot-, ok-, sol)
     MAT   – material / ingredient tokens (da-, k+quadripolo, gallows ornate)
     COMPL – completion / closure tokens (dam, sam, dy, *am)
4. For each line with at least two distinct categories, record whether
   category A precedes category B (by mean intra-line position).
5. Report mean normalised position per category and pairwise ordering rates.

Expected output (paper):
  COMPL tokens are in the final 20 % of lines > 60 % of the time.
  OPER and VEIC tend to precede MAT; MAT tends to precede COMPL.
"""

import sys
from pathlib import Path
from collections import Counter, defaultdict
from math import sqrt

sys.path.insert(0, str(Path(__file__).parent))
from corpus_utils import parse_corpus, starts_with, normalised_position

PROCEDURAL_SECTIONS = {'Herbal_A', 'Herbal_B', 'Pharma', 'Balneo'}
GALLOWS_ORNATE = {'cth', 'ckh', 'cfh', 'cph'}
K_QUAD = {'kol', 'kor', 'kal', 'kar'}
COMPL_EXACT = {'dam', 'sam', 'dy'}


def classify_token(tok: str) -> str | None:
    # COMPL first (most specific)
    if tok in COMPL_EXACT:
        return 'COMPL'
    if tok.endswith('am') and len(tok) > 2:
        return 'COMPL'
    # VEIC
    if starts_with(tok, 'qok', []) or starts_with(tok, 'qot', []):
        return 'VEIC'
    if tok == 'sol' or tok.startswith('sol'):
        return 'VEIC'
    if starts_with(tok, 'ok', []) and not starts_with(tok, 'qok', []):
        return 'VEIC'
    # OPER
    if starts_with(tok, 'ch', []) or starts_with(tok, 'sh', []):
        return 'OPER'
    if starts_with(tok, 'ot', []):
        return 'OPER'
    if starts_with(tok, 'y', []):
        return 'OPER'
    # MAT
    if starts_with(tok, 'da', []):
        return 'MAT'
    if tok in K_QUAD or tok in GALLOWS_ORNATE:
        return 'MAT'
    return None


def run(corpus_path: str) -> None:
    print("Loading Takahashi transcription…")
    records = parse_corpus(corpus_path, transcriber='H')

    proc_records = [r for r in records if r['section'] in PROCEDURAL_SECTIONS]
    total_lines  = len(proc_records)
    total_tokens = sum(len(r['tokens']) for r in proc_records)
    print(f"Procedural lines: {total_lines:,}  |  tokens: {total_tokens:,}\n")

    positions: dict[str, list[float]] = defaultdict(list)
    pair_counts: dict[tuple[str, str], list[bool]] = defaultdict(list)
    cats = ('OPER', 'VEIC', 'MAT', 'COMPL')

    for rec in proc_records:
        toks = rec['tokens']
        n = len(toks)
        if n < 2:
            continue

        cat_pos: dict[str, list[float]] = defaultdict(list)
        for idx, tok in enumerate(toks):
            cat = classify_token(tok)
            if cat:
                pos = normalised_position(idx, n)
                cat_pos[cat].append(pos)
                positions[cat].append(pos)

        present_cats = [c for c in cats if c in cat_pos]
        if len(present_cats) < 2:
            continue

        for i, ca in enumerate(cats):
            if ca not in cat_pos:
                continue
            for cb in cats[i+1:]:
                if cb not in cat_pos:
                    continue
                mean_a = sum(cat_pos[ca]) / len(cat_pos[ca])
                mean_b = sum(cat_pos[cb]) / len(cat_pos[cb])
                pair_counts[(ca, cb)].append(mean_a < mean_b)

    print("=== Mean normalised position by category ===")
    print(f"{'Category':<8}  {'N':>6}  {'Mean pos':>10}  {'StdDev':>10}")
    print("-" * 42)
    for cat in cats:
        ps = positions[cat]
        if not ps:
            print(f"{cat:<8}  {'0':>6}")
            continue
        mean = sum(ps) / len(ps)
        var  = sum((p - mean)**2 for p in ps) / len(ps)
        print(f"{cat:<8}  {len(ps):>6}  {mean:>10.3f}  {sqrt(var):>10.3f}")

    compl_ps = positions['COMPL']
    if compl_ps:
        final_20 = sum(1 for p in compl_ps if p >= 0.80) / len(compl_ps)
        print(f"\n{'COMPL in final 20% of line':>30}: {final_20:.1%}")

    print("\n=== Pairwise ordering: A before B ===")
    print(f"{'Pair':<15}  {'A→B %':>7}  {'B→A %':>7}  {'N lines':>8}")
    print("-" * 45)
    ordered_pairs = [
        ('OPER', 'VEIC'), ('OPER', 'MAT'), ('OPER', 'COMPL'),
        ('VEIC', 'MAT'),  ('VEIC', 'COMPL'), ('MAT', 'COMPL'),
    ]
    for ca, cb in ordered_pairs:
        key = (ca, cb)
        if key not in pair_counts or not pair_counts[key]:
            print(f"{ca}→{cb:<10}  {'N/A':>7}  {'N/A':>7}  {'0':>8}")
            continue
        results = pair_counts[key]
        n = len(results)
        a_before = sum(results) / n
        b_before = 1 - a_before
        pair_str = f"{ca}→{cb}"
        print(f"{pair_str:<15}  {a_before:>6.1%}  {b_before:>6.1%}  {n:>8,}")

    print("\n=== COMPL final position detail ===")
    compl_last_pairs = [('OPER', 'COMPL'), ('VEIC', 'COMPL'), ('MAT', 'COMPL')]
    for ca, cb in compl_last_pairs:
        key = (ca, cb)
        if key in pair_counts and pair_counts[key]:
            results = pair_counts[key]
            pct = sum(results) / len(results)
            print(f"  {ca} before COMPL: {pct:.1%}  (n={len(results):,})")


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python 04_positional_constraint.py <path_to_ivtff_corpus.txt>")
        sys.exit(1)
    run(sys.argv[1])
