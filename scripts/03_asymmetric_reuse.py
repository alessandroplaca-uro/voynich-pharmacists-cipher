"""
03_asymmetric_reuse.py
Result 3 – Asymmetric cross-section token reuse (Stars cites Pharma, not vice versa).

Method
------
1. Load Takahashi (H) transcription (full corpus).
2. For each source section, identify folio identifiers: the first token of the
   first line of each folio in that section.  (This is the strict definition
   used in the paper – not the first token of every line.)
3. Count how many times those identifiers appear as standalone tokens anywhere
   in the target section (total occurrences = A or B).
4. Compare Pharma→Stars (A) vs Stars→Pharma (B).

Expected output (paper):
  A  ≈ 6–15  (Pharma folio identifiers found in Stars)
  B  ≈ 0     (Stars folio identifiers found in Pharma)
  Line-initial rate of A tokens in Stars ≈ 80–90 %
"""

import sys
from pathlib import Path
from collections import Counter

sys.path.insert(0, str(Path(__file__).parent))
from corpus_utils import parse_corpus


def get_folio_identifiers(records: list[dict], section: str) -> dict[str, str]:
    """
    Return a dict mapping folio → first token of its first line, for all
    folios that have at least one record in *section*.
    """
    seen: dict[str, str] = {}          # folio -> identifier token
    for rec in records:
        if rec['section'] == section and rec['tokens']:
            folio = rec['folio']
            if folio not in seen:
                seen[folio] = rec['tokens'][0]
    return seen


def get_all_tokens(records: list[dict], section: str) -> set:
    """Return set of all standalone tokens in *section*."""
    tokens: set = set()
    for rec in records:
        if rec['section'] == section:
            tokens.update(rec['tokens'])
    return tokens


def count_cross_links(
    records: list[dict],
    source_section: str,
    target_section: str,
) -> tuple[int, list[tuple[str, int]], dict[str, str]]:
    """
    Count total occurrences in target_section of tokens that are folio
    identifiers of source_section.

    Returns:
        total       – total occurrences of identifier tokens in target
        ranked      – [(token, occurrences_in_target), ...] sorted desc
        folio_map   – {folio: identifier_token} from source
    """
    folio_map = get_folio_identifiers(records, source_section)
    id_tokens  = set(folio_map.values())

    # Count occurrences of each identifier in target section
    occ: Counter = Counter()
    for rec in records:
        if rec['section'] == target_section:
            for tok in rec['tokens']:
                if tok in id_tokens:
                    occ[tok] += 1

    total  = sum(occ.values())
    ranked = sorted(occ.items(), key=lambda x: x[1], reverse=True)
    return total, ranked, folio_map


def run(corpus_path: str) -> None:
    print("Loading Takahashi transcription…")
    records = parse_corpus(corpus_path, transcriber='H')

    total_tokens = sum(len(r['tokens']) for r in records)
    print(f"Total tokens: {total_tokens:,}\n")

    # Section sizes
    from collections import Counter as _C
    section_lines  = _C(r['section'] for r in records)
    section_tokens = _C()
    for r in records:
        section_tokens[r['section']] += len(r['tokens'])

    sections = ['Herbal_A', 'Herbal_B', 'Zodiac', 'Balneo', 'Cosmo', 'Pharma', 'Stars']
    print("=== Section sizes ===")
    print(f"{'Section':<12}  {'Lines':>6}  {'Tokens':>8}")
    print("-" * 32)
    for sec in sections:
        print(f"{sec:<12}  {section_lines[sec]:>6}  {section_tokens[sec]:>8}")

    # -----------------------------------------------------------------------
    # Key result: Pharma folio identifiers → Stars (A) vs Stars → Pharma (B)
    # -----------------------------------------------------------------------
    print("\n=== Key asymmetry: Pharma ↔ Stars (folio-identifier method) ===")
    ph_total, ph_ranked, ph_folios = count_cross_links(records, 'Pharma', 'Stars')
    st_total, st_ranked, st_folios = count_cross_links(records, 'Stars',  'Pharma')

    print(f"\nPharma folio identifiers ({len(ph_folios)} folios):")
    for folio, tok in sorted(ph_folios.items()):
        print(f"  {folio}: {tok}")

    print(f"\nPharma→Stars occurrences (A): {ph_total}")
    if ph_ranked:
        print("  Token breakdown:")
        for tok, cnt in ph_ranked:
            print(f"    {tok:20s}  {cnt} occ in Stars")

    print(f"\nStars→Pharma occurrences (B): {st_total}")
    if st_ranked:
        print("  Token breakdown:")
        for tok, cnt in st_ranked[:10]:
            print(f"    {tok:20s}  {cnt} occ in Pharma")
    else:
        print("  (none)")

    asym = ph_total / max(st_total, 1)
    print(f"\nAsymmetry A/B: {asym:.1f}×")

    # -----------------------------------------------------------------------
    # Position analysis: what fraction of A-token occurrences in Stars
    # are line-initial (first token of their line)?
    # -----------------------------------------------------------------------
    print("\n=== Line-initial rate of Pharma identifiers in Stars ===")
    ph_id_set = {tok for tok, _ in ph_ranked}
    positions = []
    for rec in records:
        if rec['section'] != 'Stars':
            continue
        for idx, tok in enumerate(rec['tokens']):
            if tok in ph_id_set:
                pos = idx / (len(rec['tokens']) - 1) if len(rec['tokens']) > 1 else 0.0
                positions.append((tok, pos, idx == 0))

    if positions:
        line_init = sum(1 for _, _, li in positions if li)
        mean_pos  = sum(p for _, p, _ in positions) / len(positions)
        print(f"  Total occurrences tracked: {len(positions)}")
        print(f"  Line-initial (pos 0):       {line_init} ({line_init/len(positions)*100:.1f}%)")
        print(f"  Mean normalised position:   {mean_pos:.3f}")

    # -----------------------------------------------------------------------
    # Broader pairwise matrix for context
    # -----------------------------------------------------------------------
    print("\n=== Pairwise folio-identifier link matrix ===")
    print("Source → Target  |  A (total occ)  B folio-ids matched")
    print("-" * 60)
    pairs = [
        ('Herbal_A', 'Stars'), ('Herbal_A', 'Pharma'),
        ('Pharma',   'Stars'), ('Stars',    'Pharma'),
        ('Balneo',   'Stars'), ('Stars',    'Balneo'),
        ('Herbal_A', 'Balneo'),
    ]
    for src, tgt in pairs:
        total, ranked, fm = count_cross_links(records, src, tgt)
        unique_matched = len(ranked)
        print(f"  {src:<12} → {tgt:<12}  {total:>5} occ   {unique_matched} tokens")


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python 03_asymmetric_reuse.py <path_to_ivtff_corpus.txt>")
        sys.exit(1)
    run(sys.argv[1])
