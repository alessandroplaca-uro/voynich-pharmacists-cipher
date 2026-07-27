#!/usr/bin/env python3
"""
07_v2_canonical_recompute.py - Preprint v2.0 canonical recomputation.

Recomputes every count-level table of:

    Placa, A. (2026). The Pharmacist's Cipher: Five Statistical Tests
    Supporting a Pharmaceutical Encoding of the Voynich Manuscript (MS 408).
    Preprint v2.0. https://doi.org/10.5281/zenodo.21629904

on the CANONICAL corpus extraction (37,967 Takahashi tokens), which
supersedes the 37,036-token extraction used by v1.1-v1.3 and by scripts
01-06 in this repository (see ERRATA.md, E3). The earlier extraction did
not split tokens at the bare space characters that the transcription uses
as intra-line layout markers.

Canonical extraction rules (embedded below, self-contained):
  - Takahashi transcription only (lines containing ';H>')
  - token separator = DOT ('.'); bare whitespace is ALSO a token boundary
  - encoding latin-1; inline {comments} and <tags> stripped; !?* stripped
  - non-alphabetic characters stripped from tokens
  - word-boundary matching only, never substring

Extraction invariants (assert the corpus file is the expected one):
  - total tokens = 37,967 across 5,207 lines
  - tokens containing substring 'kl' = 37
  - occurrences of substring 'lk'   = 1,080

Covers: Table 1 (cross-transcriber, H vs C), Table 2 (s-/sh- gap),
Result 3 (Pharma/Stars header asymmetry, 27:0), Table 5 (section
profiles), and Appendix A (withdrawn ee% volume hierarchy, with the two
additional refuting checks reported in v2.0).

Usage:
    python3 07_v2_canonical_recompute.py [path/to/LSI_ivtff_0d.txt]

Standard library only.
"""

import re
import sys
import itertools
from collections import Counter

CORPUS = sys.argv[1] if len(sys.argv) > 1 else 'LSI_ivtff_0d.txt'


# ----------------------------------------------------------------------
# Canonical loader (self-contained)
# ----------------------------------------------------------------------

def clean_line(text):
    text = re.sub(r'\{[^}]*\}', ' ', text)      # {comments}
    text = re.sub(r'<[^>]*>', ' ', text)        # <inline tags> incl. <$>
    text = re.sub(r'[!?*]', '', text)           # uncertain / unreadable marks
    return text


def tokenize(text):
    out = []
    for chunk in re.split(r'\s+', text):
        for tok in chunk.split('.'):
            tok = tok.strip('-').strip(',').strip()
            tok = re.sub(r'[^a-zA-Z]', '', tok)
            if tok:
                out.append(tok)
    return out


def load_lines(code):
    """Lines for transcriber `code` ('H' or 'C') -> dicts folio/locus/tokens."""
    line_re = re.compile(r'^<(f[^.,]+)[.,]([^,;]*)[^;]*;' + code + r'>\s*(.*)')
    lines = []
    with open(CORPUS, encoding='latin-1') as fh:
        for raw in fh:
            if (';' + code + '>') not in raw or raw.startswith('#'):
                continue
            m = line_re.match(raw.strip())
            if not m:
                continue
            toks = tokenize(clean_line(m.group(3)))
            if toks:
                lines.append({'folio': m.group(1), 'locus': m.group(2),
                              'tokens': toks})
    return lines


def paper_section(folio):
    m = re.match(r'f(\d+)', folio)
    if not m:
        return None
    n = int(m.group(1))
    if 1 <= n <= 57:
        return 'Herbal A'
    if 58 <= n <= 66:
        return 'Herbal B'
    if 67 <= n <= 73:
        return 'Zodiac'
    if 75 <= n <= 84:
        return 'Balneo'
    if 85 <= n <= 86:
        return 'Cosmo'
    if 87 <= n <= 102:
        return 'Pharma'
    if 103 <= n <= 116:
        return 'Stars'
    return None


def pref_count(toks, pref, excl=None):
    n = 0
    for t in toks:
        if t.startswith(pref) and not (excl and t.startswith(excl)):
            n += 1
    return n


def spearman_exact(expected, observed_values, larger_is_rank1=True):
    """Exact-permutation Spearman on untied ranks.

    expected: list of expected ranks. observed_values: raw values; observed
    ranks are derived (rank 1 = largest value). Returns (rho, one_tailed_p).
    """
    n = len(expected)
    order = sorted(range(n), key=lambda i: -observed_values[i]) \
        if larger_is_rank1 else sorted(range(n), key=lambda i: observed_values[i])
    obs_rank = [0] * n
    for r, i in enumerate(order, 1):
        obs_rank[i] = r

    def rho_of(a, b):
        d2 = sum((x - y) ** 2 for x, y in zip(a, b))
        return 1 - 6 * d2 / (n * (n * n - 1))

    rho = rho_of(expected, obs_rank)
    perms = list(itertools.permutations(range(1, n + 1)))
    ge = sum(1 for pm in perms if rho_of(expected, list(pm)) >= rho - 1e-12)
    return rho, obs_rank, ge / len(perms), ge, len(perms)


# ----------------------------------------------------------------------
# Corpus + invariants
# ----------------------------------------------------------------------

H = load_lines('H')
C = load_lines('C')
htoks = [t for ln in H for t in ln['tokens']]
cnt = Counter(htoks)

print('== CANONICAL EXTRACTION ==')
print(f'H lines {len(H)}  H tokens {len(htoks)}')
kl = sum(1 for t in htoks if 'kl' in t)
lk = sum(t.count('lk') for t in htoks)
print(f'invariants: kl-tokens {kl} (expected 37), lk-occurrences {lk} (expected 1,080)')
for got, want, name in [(len(htoks), 37967, 'tokens'), (len(H), 5207, 'lines'),
                        (kl, 37, 'kl'), (lk, 1080, 'lk')]:
    if got != want:
        print(f'WARNING: {name} = {got}, expected {want}: '
              f'corpus file differs from the canonical LSI_ivtff_0d.txt')

# ----------------------------------------------------------------------
# Table 1: cross-transcriber stability
# ----------------------------------------------------------------------

print('\n== TABLE 1: cross-transcriber (common folio+locus lines) ==')
hidx = {(l['folio'], l['locus']): l['tokens'] for l in H}
cidx = {(l['folio'], l['locus']): l['tokens'] for l in C}
common = sorted(set(hidx) & set(cidx))
h_common = [t for k in common for t in hidx[k]]
c_common = [t for k in common for t in cidx[k]]
print(f'common lines {len(common)}  H tokens {len(h_common)}  C tokens {len(c_common)}')
PREFIXES = [('ch-', 'ch', None), ('sh-', 'sh', None), ('da-', 'da', None),
            ('ok-', 'ok', None), ('qok-', 'qok', None), ('qot-', 'qot', None),
            ('ot-', 'ot', None), ('l-', 'l', None), ('y-', 'y', None),
            ('s-', 's', 'sh'), ('t-', 't', 'th')]
print(f'{"prefix":6} {"H permil":>9} {"C permil":>9} {"C/H":>6} {"drift":>6}')
for name, pref, excl in PREFIXES:
    hd = 1000 * pref_count(h_common, pref, excl) / len(h_common)
    cd = 1000 * pref_count(c_common, pref, excl) / len(c_common)
    print(f'{name:6} {hd:9.1f} {cd:9.1f} {cd/hd:6.3f} {abs(cd/hd-1)*100:5.1f}%')
for sec in ['Herbal A', 'Balneo']:
    hs = [t for k in common for t in hidx[k] if paper_section(k[0]) == sec]
    cs = [t for k in common for t in cidx[k] if paper_section(k[0]) == sec]
    hr = pref_count(hs, 'ch') / max(1, pref_count(hs, 'sh'))
    cr = pref_count(cs, 'ch') / max(1, pref_count(cs, 'sh'))
    print(f'ch/sh {sec}: H={hr:.2f} C={cr:.2f} drift {abs(cr/hr-1)*100:.1f}%')

# ----------------------------------------------------------------------
# Table 2: s- vs sh- categorical gap
# ----------------------------------------------------------------------

print('\n== TABLE 2: s- vs sh- ==')
s_toks = [t for t in htoks if t.startswith('s') and not t.startswith('sh')]
sh_toks = [t for t in htoks if t.startswith('sh')]
print(f's- total {len(s_toks)}  sh- total {len(sh_toks)}  '
      f'ratio {len(sh_toks)/len(s_toks):.2f}')
print(f"sedy {cnt['sedy']}  shedy {cnt['shedy']}  "
      f"seo {cnt['seo']}  sheo {cnt['sheo']}")
PROC = ('edy', 'eedy', 'ey', 'eey')
NOM = ('aiin', 'ain', 'ar', 'al')
for name, fam in [('s-', s_toks), ('sh-', sh_toks)]:
    pr = sum(1 for t in fam if t.endswith(PROC))
    no = sum(1 for t in fam if t.endswith(NOM))
    print(f'{name}: processual {pr} ({100*pr/len(fam):.1f}%)  '
          f'nominal {no} ({100*no/len(fam):.1f}%)')
sproc = Counter(t for t in s_toks if t.endswith(PROC))
print('top s- processual compounds:', sproc.most_common(5))

# ----------------------------------------------------------------------
# Result 3: Pharma/Stars header asymmetry
# ----------------------------------------------------------------------

print('\n== RESULT 3: Pharma/Stars header asymmetry ==')
first_tok = {}
for ln in H:
    first_tok.setdefault(ln['folio'], ln['tokens'][0])
ph_folios = sorted(f for f in first_tok if paper_section(f) == 'Pharma')
st_folios = sorted(f for f in first_tok if paper_section(f) == 'Stars')
ph_all = [t for ln in H if paper_section(ln['folio']) == 'Pharma'
          for t in ln['tokens']]
st_all = [t for ln in H if paper_section(ln['folio']) == 'Stars'
          for t in ln['tokens']]
stc, phc = Counter(st_all), Counter(ph_all)
p2s = {first_tok[f]: stc[first_tok[f]] for f in ph_folios
       if stc[first_tok[f]] > 0}
s2p = {first_tok[f]: phc[first_tok[f]] for f in st_folios
       if phc[first_tok[f]] > 0}
print(f'Pharma folios {len(ph_folios)} ({len(ph_all)} tokens)  '
      f'Stars folios {len(st_folios)} ({len(st_all)} tokens)')
print(f'Pharma headers found in Stars: {sum(p2s.values())} occurrences, '
      f'{len(p2s)} of {len(ph_folios)} types -> '
      f'{dict(sorted(p2s.items(), key=lambda x: -x[1]))}')
print(f'Stars headers found in Pharma: {sum(s2p.values())} occurrences, '
      f'{len(s2p)} of {len(st_folios)} types')

# ----------------------------------------------------------------------
# Table 5: section-specific prefix profiles
# ----------------------------------------------------------------------

print('\n== TABLE 5: section prefix densities (permil) ==')
SECS = ['Herbal A', 'Herbal B', 'Zodiac', 'Balneo', 'Pharma', 'Stars']
sec_toks = {s: [] for s in SECS}
cosmo = []
for ln in H:
    s = paper_section(ln['folio'])
    if s in sec_toks:
        sec_toks[s].extend(ln['tokens'])
    elif s == 'Cosmo':
        cosmo.extend(ln['tokens'])
ROWS = [('ch-', 'ch', None), ('sh-', 'sh', None), ('qok-', 'qok', None),
        ('qot-', 'qot', None), ('da-', 'da', None), ('ot-', 'ot', None),
        ('l-', 'l', None), ('y-', 'y', None)]
print(f'{"prefix":6}' + ''.join(f'{s:>10}' for s in SECS) + f'{"Corpus":>10}')
for name, pref, excl in ROWS:
    row = f'{name:6}'
    for s in SECS:
        row += f'{1000*pref_count(sec_toks[s], pref, excl)/len(sec_toks[s]):10.1f}'
    row += f'{1000*pref_count(htoks, pref, excl)/len(htoks):10.1f}'
    print(row)
row = f'{"ch/sh":6}'
for s in SECS:
    row += f'{pref_count(sec_toks[s], "ch")/pref_count(sec_toks[s], "sh"):10.2f}'
row += f'{pref_count(htoks, "ch")/pref_count(htoks, "sh"):10.2f}'
print(row)
row = f'{"N":6}'
for s in SECS:
    row += f'{len(sec_toks[s]):10}'
row += f'{len(htoks):10}'
print(row)
print(f'Cosmo tokens (in corpus column, not shown separately): {len(cosmo)}')

# ----------------------------------------------------------------------
# Appendix A: withdrawn ee% volume hierarchy + the two refuting checks
# ----------------------------------------------------------------------

print('\n== APPENDIX A: ee% by family (WITHDRAWN as evidence in v2.0) ==')
FAMS = [('WATER (ok+qok)',
         lambda t: t.startswith('ok') or t.startswith('qok'), 1),
        ('SPIRIT (l)', lambda t: t.startswith('l'), 3),
        ('OIL (t+qot)',
         lambda t: (t.startswith('t') and not t.startswith('th'))
         or t.startswith('qot'), 2),
        ('VINEGAR (s)',
         lambda t: t.startswith('s') and not t.startswith('sh'), 4),
        ('MEDICINE (da)', lambda t: t.startswith('da'), 5)]
obs, lens = [], []
for name, f, exp in FAMS:
    sub = [t for t in htoks if f(t)]
    ee = sum(1 for t in sub if 'ee' in t)
    obs.append(100 * ee / len(sub))
    lens.append(sum(len(t) for t in sub) / len(sub))
    print(f'{name:16} N={len(sub):5} ee={ee:5} ee%={obs[-1]:5.1f} '
          f'exp_rank={exp} mean_len={lens[-1]:.2f}')
expected = [f[2] for f in FAMS]
rho, ranks, p1, ge, tot = spearman_exact(expected, obs)
print(f'n=5: rho={rho:.3f}  exact one-tailed p={p1:.4f} ({ge}/{tot})')

# Refuting check 1: drop the MEDICINE (da-) family (not a solvent family:
# d is an anaphoric pointer, P081) -> the test does not survive.
rho4, _, p4, ge4, tot4 = spearman_exact(expected[:4], obs[:4])
print(f'check 1, n=4 without MEDICINE: rho={rho4:.3f}  '
      f'exact one-tailed p={p4:.3f} ({ge4}/{tot4})')

# Refuting check 2: ee% correlates with mean token length (longer tokens
# contain any fixed bigram more often) -> length confound.
rhoL, _, _, _, _ = spearman_exact(
    [sorted(range(5), key=lambda i: -lens[i]).index(i) + 1 for i in range(5)],
    obs)
print(f'check 2, ee% vs mean token length: rho={rhoL:.3f} '
      f'(mean lengths: {", ".join(f"{x:.2f}" for x in lens)})')

print('\nDone. Compare against the tables of preprint v2.0.')
