"""
02_paradigm_gap.py
Result 2 – Binary morphological gap between s- and sh- prefix families.

Method
------
1. Load Takahashi (H) transcription.
2. Separate tokens into s- family (starts with 's' but NOT 'sh') and
   sh- family (starts with 'sh').
3. Classify each token by suffix type: processual (-edy, -eedy, -ey, -eey)
   vs nominal (-aiin, -ain, -ar, -al).
4. Compare the processual/nominal ratio for s- vs sh-.
5. Count exact occurrences of 'sedy' and 'shedy'.

Expected output (paper):
  sedy = 0, shedy ≈ 299–425.
  s- takes nominal suffixes at 108× the rate it takes processual suffixes;
  sh- takes processual suffixes at 3.8× the rate it takes nominal suffixes.
"""

import sys
from pathlib import Path
from collections import Counter

sys.path.insert(0, str(Path(__file__).parent))
from corpus_utils import parse_corpus, starts_with

PROCESSUAL_SUFFIXES = ('-edy', '-eedy', '-ey', '-eey')
NOMINAL_SUFFIXES    = ('-aiin', '-ain', '-ar', '-al')


def classify_token(token: str) -> str:
    for sfx in PROCESSUAL_SUFFIXES:
        if token.endswith(sfx.lstrip('-')):
            return 'processual'
    for sfx in NOMINAL_SUFFIXES:
        if token.endswith(sfx.lstrip('-')):
            return 'nominal'
    return 'other'


def run(corpus_path: str) -> None:
    print("Loading Takahashi transcription…")
    records = parse_corpus(corpus_path, transcriber='H')
    total_tokens = sum(len(r['tokens']) for r in records)
    print(f"Total tokens: {total_tokens:,}\n")

    s_tokens:  list[str] = []
    sh_tokens: list[str] = []
    for rec in records:
        for tok in rec['tokens']:
            if starts_with(tok, 'sh', []):
                sh_tokens.append(tok)
            elif starts_with(tok, 's', []):
                s_tokens.append(tok)

    s_exact  = Counter(s_tokens)
    sh_exact = Counter(sh_tokens)

    print("=== Key exact token counts ===")
    print(f"  sedy   : {s_exact.get('sedy', 0)}")
    print(f"  shedy  : {sh_exact.get('shedy', 0)}")
    print(f"  seo    : {s_exact.get('seo', 0)}")
    print(f"  sheo   : {sh_exact.get('sheo', 0)}")

    s_class  = Counter(classify_token(t) for t in s_tokens)
    sh_class = Counter(classify_token(t) for t in sh_tokens)
    n_s  = len(s_tokens)
    n_sh = len(sh_tokens)

    print(f"\n=== Suffix distribution ===")
    print(f"{'Category':<15}  {'s- (N)':>8}  {'s- (%)':>8}  "
          f"{'sh- (N)':>8}  {'sh- (%)':>8}  {'Ratio sh/s':>11}")
    print("-" * 70)
    for cat in ('processual', 'nominal', 'other'):
        s_n  = s_class[cat]
        sh_n = sh_class[cat]
        s_p  = s_n  / n_s  * 100 if n_s  else 0
        sh_p = sh_n / n_sh * 100 if n_sh else 0
        ratio = (sh_p / s_p) if s_p else float('inf')
        print(f"{cat:<15}  {s_n:>8}  {s_p:>7.1f}%  {sh_n:>8}  {sh_p:>7.1f}%  {ratio:>11.2f}×")

    print(f"\nTotal s-  tokens : {n_s:,}")
    print(f"Total sh- tokens : {n_sh:,}")
    if n_s:
        print(f"Ratio sh/s       : {n_sh / n_s:.2f}×")

    # Show any processual s- tokens (should be near zero for pure s-)
    compound_processual = [
        t for t in s_tokens
        if classify_token(t) == 'processual' and not t.startswith('sh')
    ]
    print(f"\nProcessual s- tokens (compound or direct): {len(compound_processual)}")
    top_compound = Counter(compound_processual).most_common(10)
    for tok, cnt in top_compound:
        print(f"  {tok:20s}  {cnt}")


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python 02_paradigm_gap.py <path_to_ivtff_corpus.txt>")
        sys.exit(1)
    run(sys.argv[1])
