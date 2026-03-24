"""
05_section_profiles.py
Result 5 – Morphological profiles of the six major sections.

Method
------
1. Load Takahashi (H) transcription.
2. For each of six sections and 14 morphological markers, compute
   density in tokens per thousand (‰).
3. Also compute the ch/sh temperature ratio per section.
4. Compute enrichment ratios (section density / corpus baseline) for
   selected markers.

Expected output (paper):
  Stars:  l- enriched ~3.4×; -edy enriched ~1.5×; qok-/qot- present
  Zodiac: ot- enriched ~2.4×; qok-/qot- depleted ~0.16×
  Balneo: ch-/sh- near-parity (ch/sh ≈ 1.07)
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from corpus_utils import parse_corpus, starts_with, token_density

SECTIONS = ['Herbal_A', 'Herbal_B', 'Zodiac', 'Balneo', 'Pharma', 'Stars']

# (label, prefix_or_suffix, exclude_list, is_suffix)
MARKERS: list[tuple[str, str, list[str], bool]] = [
    ('ch-',   'ch',   [],       False),
    ('sh-',   'sh',   [],       False),
    ('da-',   'da',   [],       False),
    ('ok-',   'ok',   [],       False),
    ('qok-',  'qok',  [],       False),
    ('qot-',  'qot',  [],       False),
    ('l-',    'l',    [],       False),
    ('y-',    'y',    [],       False),
    ('ot-',   'ot',   ['oth'],  False),
    ('s-',    's',    ['sh'],   False),
    ('t-',    't',    ['th'],   False),
    ('-edy',  'edy',  [],       True),
    ('-am',   'am',   [],       True),
    ('dy',    'dy',   [],       False),
]


def count_suffix(records, suffix, section=None):
    total = 0
    for rec in records:
        if section and rec['section'] != section:
            continue
        for tok in rec['tokens']:
            if tok.endswith(suffix):
                total += 1
    return total


def count_tokens(records, section=None):
    total = 0
    for rec in records:
        if section and rec['section'] != section:
            continue
        total += len(rec['tokens'])
    return total


def count_exact(records, token, section=None):
    total = 0
    for rec in records:
        if section and rec['section'] != section:
            continue
        total += rec['tokens'].count(token)
    return total


def run(corpus_path: str) -> None:
    print("Loading Takahashi transcription…")
    records = parse_corpus(corpus_path, transcriber='H')
    total = count_tokens(records)
    print(f"Total tokens (all sections): {total:,}\n")

    sec_n = {sec: count_tokens(records, sec) for sec in SECTIONS}

    col_w = 9
    header = f"{'Marker':<8}" + "".join(f"{s:>{col_w}}" for s in SECTIONS)
    print(header)
    print("-" * (8 + col_w * len(SECTIONS)))

    for label, pfx_or_sfx, excl, is_suffix in MARKERS:
        row = f"{label:<8}"
        densities = []
        for sec in SECTIONS:
            n = sec_n[sec]
            if n == 0:
                densities.append(0.0)
                continue
            if label == 'dy':
                hits = count_exact(records, 'dy', sec)
            elif is_suffix:
                hits = count_suffix(records, pfx_or_sfx, sec)
            else:
                hits = sum(
                    1 for rec in records
                    if rec['section'] == sec
                    for tok in rec['tokens']
                    if starts_with(tok, pfx_or_sfx, excl)
                )
            dens = hits / n * 1000
            densities.append(dens)
        row += "".join(f"{d:>{col_w}.1f}" for d in densities)
        print(row)

    # ch/sh ratio row
    print(f"\n{'ch/sh':<8}", end="")
    for sec in SECTIONS:
        ch = sum(
            1 for r in records if r['section'] == sec
            for t in r['tokens'] if starts_with(t, 'ch', [])
        )
        sh = sum(
            1 for r in records if r['section'] == sec
            for t in r['tokens'] if starts_with(t, 'sh', [])
        )
        ratio = ch / sh if sh else float('inf')
        print(f"{ratio:>{col_w}.2f}", end="")
    print()

    # Token counts
    print(f"\n{'N tok':<8}", end="")
    for sec in SECTIONS:
        print(f"{sec_n[sec]:>{col_w},}", end="")
    print()

    sec_lines = {sec: sum(1 for r in records if r['section'] == sec) for sec in SECTIONS}
    print(f"{'N lines':<8}", end="")
    for sec in SECTIONS:
        print(f"{sec_lines[sec]:>{col_w},}", end="")
    print()

    # Enrichment ratios
    print("\n=== Enrichment ratios vs corpus baseline ===")
    print(f"(ratio > 1 = enriched in that section)\n")
    key_markers = [
        ('l-',   'l',   [],       False),
        ('-edy',  'edy', [],       True),
        ('qok-',  'qok', [],       False),
        ('ot-',   'ot',  ['oth'],  False),
    ]
    for label, pfx, excl, is_sfx in key_markers:
        if is_sfx:
            baseline_hits = count_suffix(records, pfx)
        elif label == 'dy':
            baseline_hits = count_exact(records, 'dy')
        else:
            baseline_hits = sum(
                1 for rec in records for tok in rec['tokens']
                if starts_with(tok, pfx, excl)
            )
        baseline_dens = baseline_hits / total * 1000
        row = f"{label:<8}"
        for sec in SECTIONS:
            n = sec_n[sec]
            if n == 0:
                row += f"{'N/A':>{col_w}}"
                continue
            if is_sfx:
                hits = count_suffix(records, pfx, sec)
            else:
                hits = sum(
                    1 for rec in records if rec['section'] == sec
                    for tok in rec['tokens']
                    if starts_with(tok, pfx, excl)
                )
            sec_dens = hits / n * 1000
            ratio = sec_dens / baseline_dens if baseline_dens else float('inf')
            row += f"{ratio:>{col_w}.2f}×"
        print(row)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python 05_section_profiles.py <path_to_ivtff_corpus.txt>")
        sys.exit(1)
    run(sys.argv[1])
