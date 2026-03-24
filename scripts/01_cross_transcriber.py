"""
01_cross_transcriber.py
Result 1 – Cross-transcriber stability of morphological prefix densities.

Method
------
1. Load both Takahashi (H) and Currier (C) transcriptions.
2. Identify lines present in both transcriptions (matched by folio_line_id).
3. Compute prefix densities (tokens per thousand, ‰) on the common lines only.
4. Report ratio C/H for each prefix; flag any ratio outside [0.97, 1.03].
5. Report ch/sh ratio per major section for both transcribers.

Expected output (paper):
  All 11 prefixes: ratio C/H between 0.97 and 1.03 (< 4 % drift).
  ch/sh ratio per section is stable across transcribers.
"""

import sys
from pathlib import Path
from collections import defaultdict

sys.path.insert(0, str(Path(__file__).parent))
from corpus_utils import parse_corpus, starts_with

PREFIXES = [
    ('ch-',  'ch',  []),
    ('sh-',  'sh',  []),
    ('da-',  'da',  []),
    ('ok-',  'ok',  []),
    ('qok-', 'qok', []),
    ('qot-', 'qot', []),
    ('ot-',  'ot',  []),
    ('l-',   'l',   []),
    ('y-',   'y',   []),
    ('s-',   's',   ['sh']),
    ('t-',   't',   ['th']),
]

SECTION_CHECK = ['Herbal_A', 'Balneo', 'Pharma', 'Zodiac', 'Stars']


def run(corpus_path: str) -> None:
    print("Loading Takahashi transcription…")
    h_records = parse_corpus(corpus_path, transcriber='H')
    print("Loading Currier transcription…")
    c_records = parse_corpus(corpus_path, transcriber='C')

    # Index by folio_line_id
    h_by_line: dict[str, list[str]] = {}
    for rec in h_records:
        h_by_line[rec['folio_line_id']] = rec['tokens']

    c_by_line: dict[str, list[str]] = {}
    for rec in c_records:
        c_by_line[rec['folio_line_id']] = rec['tokens']

    common_ids = set(h_by_line) & set(c_by_line)
    print(f"Common lines: {len(common_ids)}")

    # Pool tokens for common lines
    h_tokens_common: list[str] = []
    c_tokens_common: list[str] = []
    for lid in sorted(common_ids):
        h_tokens_common.extend(h_by_line[lid])
        c_tokens_common.extend(c_by_line[lid])

    n_h = len(h_tokens_common)
    n_c = len(c_tokens_common)
    print(f"Tokens (H common): {n_h:,}   Tokens (C common): {n_c:,}\n")

    print(f"{'Prefix':<8}  {'H (\u2030)':>7}  {'C (\u2030)':>7}  {'Ratio C/H':>10}  {'Drift':>7}")
    print("-" * 50)
    for label, pfx, excl in PREFIXES:
        h_hits = sum(1 for t in h_tokens_common if starts_with(t, pfx, excl))
        c_hits = sum(1 for t in c_tokens_common if starts_with(t, pfx, excl))
        h_dens = h_hits / n_h * 1000
        c_dens = c_hits / n_c * 1000
        ratio  = c_dens / h_dens if h_dens else float('inf')
        drift  = abs(ratio - 1) * 100
        flag   = " *** DRIFT" if drift > 4.0 else ""
        print(f"{label:<8}  {h_dens:>7.1f}  {c_dens:>7.1f}  {ratio:>10.3f}  {drift:>6.1f}%{flag}")

    # ch/sh ratio per section
    print("\n--- ch/sh ratio per section ---")
    print(f"{'Section':<12}  {'H ch/sh':>8}  {'C ch/sh':>8}  {'Drift':>7}")
    print("-" * 45)

    def section_ratio(records, section):
        ch = sum(
            1 for r in records if r['section'] == section
            for t in r['tokens'] if starts_with(t, 'ch', [])
        )
        sh = sum(
            1 for r in records if r['section'] == section
            for t in r['tokens'] if starts_with(t, 'sh', [])
        )
        return ch / sh if sh else float('inf')

    for sec in SECTION_CHECK:
        r_h = section_ratio(h_records, sec)
        r_c = section_ratio(c_records, sec)
        drift = abs(r_c / r_h - 1) * 100 if r_h else float('inf')
        print(f"{sec:<12}  {r_h:>8.2f}  {r_c:>8.2f}  {drift:>6.1f}%")


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python 01_cross_transcriber.py <path_to_ivtff_corpus.txt>")
        sys.exit(1)
    run(sys.argv[1])
