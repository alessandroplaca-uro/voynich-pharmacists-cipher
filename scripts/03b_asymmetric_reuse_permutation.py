#!/usr/bin/env python3
"""
Permutation test for Result 3 — Asymmetric Cross-Section Reuse.
Supplementary robustness analysis for Placa (2026) v1.2.

Null hypothesis: the 26:0 asymmetry between Pharma->Stars and Stars->Pharma
could arise by chance given vocabulary sizes and token counts.

Three approaches tested:
  A) Random vocabulary sampling (preserves token counts, not position structure)
  B) Random position within first line (tests if first-token is special)
  C) Section-label shuffle — THE PRIMARY TEST (preserves folio structure,
     shuffles which folios are assigned to Pharma vs Stars)

Result reported in paper (footnote to Table 3):
  Approach C: p = 0.0002 (21/100,000 permutations)

Usage:
  python 03b_asymmetric_reuse_permutation.py IT2a-n.txt

Seed: 42 (reproducible)
"""
import re
import sys
import random

random.seed(42)

# ── PARSE ────────────────────────────────────────────────────────

def parse_ivtff(filepath):
    lines = []
    seen_first = {}
    with open(filepath, encoding='latin-1') as f:
        for raw in f:
            raw = raw.strip()
            if not raw or raw.startswith('#'):
                continue
            if re.match(r'^<f\d+[rv]\d?>', raw) and '.' not in raw.split('>')[0]:
                continue
            line_match = re.match(r'^<(f\d+[rv]\d?)\.(\d+),([^>]+)>\s+(.*)', raw)
            if not line_match:
                continue
            folio = line_match.group(1)
            content = line_match.group(4)
            content = re.sub(r'<[^>]*>', '', content)
            content = content.replace('!', '').replace('?', '')
            content = re.sub(r'@\d+;', '', content)
            tokens = [t.strip() for t in re.split(r'[.,]', content)
                      if t.strip() and t.strip() != '-']
            if tokens:
                is_first = folio not in seen_first
                if is_first:
                    seen_first[folio] = True
                lines.append({'folio': folio, 'tokens': tokens, 'is_first': is_first})
    return lines


def get_fnum(f):
    m = re.match(r'f(\d+)', f)
    return int(m.group(1)) if m else 0


def section(f):
    n = get_fnum(f)
    if 87 <= n <= 102:
        return 'Pharma'
    if 103 <= n <= 116:
        return 'Stars'
    return None


# ── LOAD ─────────────────────────────────────────────────────────

corpus_file = sys.argv[1] if len(sys.argv) > 1 else 'IT2a-n.txt'
print(f"Loading corpus: {corpus_file}")
lines = parse_ivtff(corpus_file)

pharma_headers = {}
stars_headers = {}
pharma_all_tokens = set()
stars_all_tokens = set()
pharma_token_list = []
stars_token_list = []

for line in lines:
    s = section(line['folio'])
    if s == 'Pharma':
        if line['is_first']:
            pharma_headers[line['folio']] = line['tokens'][0]
        pharma_all_tokens.update(line['tokens'])
        pharma_token_list.extend(line['tokens'])
    elif s == 'Stars':
        if line['is_first']:
            stars_headers[line['folio']] = line['tokens'][0]
        stars_all_tokens.update(line['tokens'])
        stars_token_list.extend(line['tokens'])

ph_set = set(pharma_headers.values())
st_set = set(stars_headers.values())

obs_A = sum(1 for t in stars_token_list if t in ph_set)
obs_B = sum(1 for t in pharma_token_list if t in st_set)
obs_asym = obs_A - obs_B

print(f"\nOBSERVED:")
print(f"  Pharma: {len(pharma_headers)} folios, {len(ph_set)} distinct headers")
print(f"  Stars:  {len(stars_headers)} folios, {len(st_set)} distinct headers")
print(f"  A (Pharma->Stars): {obs_A}")
print(f"  B (Stars->Pharma): {obs_B}")
print(f"  Asymmetry (A-B):   {obs_asym}")

# ── APPROACH C: Section-label shuffle (PRIMARY TEST) ─────────────

print(f"\n{'='*60}")
print("APPROACH C — Section-label shuffle (PRIMARY TEST)")
print(f"{'='*60}")

combined_folios = {}
for line in lines:
    s = section(line['folio'])
    if s in ('Pharma', 'Stars'):
        if line['folio'] not in combined_folios:
            combined_folios[line['folio']] = {'first_token': None, 'all_tokens': []}
        combined_folios[line['folio']]['all_tokens'].extend(line['tokens'])
        if line['is_first']:
            combined_folios[line['folio']]['first_token'] = line['tokens'][0]

all_folios = list(combined_folios.keys())
n_pharma = len(pharma_headers)
n_stars = len(stars_headers)

N_PERM = 100_000
count_c = 0

for _ in range(N_PERM):
    random.shuffle(all_folios)
    fake_pharma = all_folios[:n_pharma]
    fake_stars = all_folios[n_pharma:n_pharma + n_stars]

    fp_hdrs = set(combined_folios[f]['first_token'] for f in fake_pharma
                  if combined_folios[f]['first_token'])
    fs_hdrs = set(combined_folios[f]['first_token'] for f in fake_stars
                  if combined_folios[f]['first_token'])

    fake_stars_toks = [t for f in fake_stars for t in combined_folios[f]['all_tokens']]
    fake_pharma_toks = [t for f in fake_pharma for t in combined_folios[f]['all_tokens']]

    pA = sum(1 for t in fake_stars_toks if t in fp_hdrs)
    pB = sum(1 for t in fake_pharma_toks if t in fs_hdrs)

    if (pA - pB) >= obs_asym:
        count_c += 1

p_c = count_c / N_PERM
print(f"  {N_PERM} permutations, seed=42")
print(f"  P(asymmetry >= {obs_asym}): {count_c}/{N_PERM} = {p_c:.4f}")

# ── APPROACH A: Random vocabulary sampling ────────────────────────

print(f"\n{'='*60}")
print("APPROACH A — Random vocabulary sampling")
print(f"{'='*60}")

pharma_vocab = list(pharma_all_tokens)
stars_vocab = list(stars_all_tokens)
count_a = 0

for _ in range(N_PERM):
    fake_ph = set(random.sample(pharma_vocab, min(n_pharma, len(pharma_vocab))))
    fake_st = set(random.sample(stars_vocab, min(n_stars, len(stars_vocab))))
    pA = sum(1 for t in stars_token_list if t in fake_ph)
    pB = sum(1 for t in pharma_token_list if t in fake_st)
    if (pA - pB) >= obs_asym:
        count_a += 1

print(f"  P(asymmetry >= {obs_asym}): {count_a}/{N_PERM} = {count_a/N_PERM:.4f}")
print(f"  (Note: this approach ignores positional structure; not used in paper)")

# ── APPROACH B: Random position within first line ─────────────────

print(f"\n{'='*60}")
print("APPROACH B — Random position within first line")
print(f"{'='*60}")

pharma_first_lines = {line['folio']: line['tokens']
                      for line in lines if section(line['folio']) == 'Pharma' and line['is_first']}
stars_first_lines = {line['folio']: line['tokens']
                     for line in lines if section(line['folio']) == 'Stars' and line['is_first']}

count_b = 0
for _ in range(N_PERM):
    fake_ph2 = set(random.choice(toks) for toks in pharma_first_lines.values())
    fake_st2 = set(random.choice(toks) for toks in stars_first_lines.values())
    pA = sum(1 for t in stars_token_list if t in fake_ph2)
    pB = sum(1 for t in pharma_token_list if t in fake_st2)
    if (pA - pB) >= obs_asym:
        count_b += 1

print(f"  P(asymmetry >= {obs_asym}): {count_b}/{N_PERM} = {count_b/N_PERM:.4f}")
print(f"  (Tests whether first-token position is special within the first line)")

# ── SUMMARY ──────────────────────────────────────────────────────

print(f"\n{'='*60}")
print("SUMMARY")
print(f"{'='*60}")
print(f"  Observed asymmetry: A={obs_A}, B={obs_B}, A-B={obs_asym}")
print(f"  Approach A (random vocab):    p = {count_a/N_PERM:.4f}  [not used in paper]")
print(f"  Approach B (random position): p = {count_b/N_PERM:.4f}")
print(f"  Approach C (section shuffle): p = {p_c:.4f}  [PRIMARY — reported in footnote]")
print(f"\n  Paper footnote value: p = 0.0002 (21/100,000, seed=42)")
