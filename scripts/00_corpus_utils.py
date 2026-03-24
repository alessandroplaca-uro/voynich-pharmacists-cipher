"""
00_corpus_utils.py
Shared utilities for parsing the IVTFF interlinear transcription corpus.

Corpus format (IVTFF):
  Each line: <fNNv.LL,@LAYOUT;T> token.token.token...
  - fNNv   : folio identifier (e.g. f1r, f10v, f86v3)
  - LL     : line number within folio
  - @LAYOUT: layout tag (e.g. @P0, @Cc, @Ri)
  - T      : transcriber code (H = Takahashi, C = Currier, ...)
  Tokens are separated by '.' (NOT by spaces).
  '-' indicates an unreadable token (omitted in analysis).

Section boundaries (folio numbers):
  Herbal A : f1  – f57
  Herbal B : f58 – f66
  Zodiac   : f67 – f73
  Balneo   : f75 – f84
  Cosmo    : f85 – f86
  Pharma   : f87 – f102
  Stars    : f103 – f116
"""

import re
from collections import defaultdict


# ---------------------------------------------------------------------------
# Section mapping
# ---------------------------------------------------------------------------

SECTION_RANGES = {
    'Herbal_A': (1,   57),
    'Herbal_B': (58,  66),
    'Zodiac':   (67,  73),
    'Balneo':   (75,  84),
    'Cosmo':    (85,  86),
    'Pharma':   (87, 102),
    'Stars':   (103, 116),
}


def get_section(folio_num: int) -> str:
    """Return the section name for a given folio number."""
    for section, (lo, hi) in SECTION_RANGES.items():
        if lo <= folio_num <= hi:
            return section
    return 'Other'


# ---------------------------------------------------------------------------
# IVTFF parser
# ---------------------------------------------------------------------------

# Matches locator tags like: <f1r.1,@P0;H>  or  <f86v3.5,@Cc;C>
_LOCATOR_RE = re.compile(
    r'^<(f(\d+)[rv]\d*)\.\w+,([@+]\w+);([A-Z])>'
)


def parse_corpus(filepath: str, transcriber: str = 'H') -> list[dict]:
    """
    Parse an IVTFF corpus file and return a list of line records.

    Each record is a dict:
        folio        : str  – e.g. 'f1r', 'f10v'
        folio_num    : int  – e.g. 1, 10
        folio_line_id: str  – raw locator key, e.g. 'f1r.1'
        section      : str  – section name
        layout       : str  – e.g. '@P0', '@Cc'
        tokens       : list[str] – standalone tokens (dots stripped, '-' removed)

    Parameters
    ----------
    filepath    : path to the IVTFF corpus (.txt, latin-1 encoding)
    transcriber : single-letter code ('H' = Takahashi, 'C' = Currier)
    """
    filter_tag = f';{transcriber}>'
    records = []

    with open(filepath, encoding='latin-1') as fh:
        for raw in fh:
            line = raw.strip()
            if not line or line.startswith('#') or filter_tag not in line:
                continue

            m = _LOCATOR_RE.match(line)
            if not m:
                continue

            folio_str   = m.group(1)          # e.g. 'f1r' or 'f86v3'
            folio_num   = int(m.group(2))      # numeric part
            layout      = m.group(3)
            # transcriber letter confirmed by filter above

            # Derive a canonical folio id (strip sub-folio digit for numbering)
            folio_canon = re.match(r'f(\d+[rv])', folio_str).group(1)  # e.g. 'f1r'
            folio_id    = 'f' + folio_canon.lstrip('f')                 # normalise

            # Locator key for line matching across transcribers
            # Use only folio.line portion (e.g. 'f1r.1'), stripping layout+transcriber suffix
            folio_line_id = line[1 : line.index(',')]  # e.g. 'f1r.1'

            # Text after the closing '>'
            text = line[line.index('>') + 1:].strip()
            if not text:
                continue

            # Tokenise: split on '.', drop empty strings, '-' (illegible) and pure '!' markers
            # Strip '!' (uncertain-reading markers) from token interiors before analysis
            tokens = [t.replace('!', '') for t in text.split('.')
                      if t and t != '-' and t.replace('!', '')]
            if not tokens:
                continue

            records.append({
                'folio':         folio_str,
                'folio_num':     folio_num,
                'folio_line_id': folio_line_id,
                'section':       get_section(folio_num),
                'layout':        layout,
                'tokens':        tokens,
            })

    return records


# ---------------------------------------------------------------------------
# Token-level helpers
# ---------------------------------------------------------------------------

def starts_with(token: str, prefix: str, exclude: list[str] | None = None) -> bool:
    """
    Return True if *token* starts with *prefix*, optionally excluding
    tokens that start with any string in *exclude*.

    Example: starts_with('shedy', 's', exclude=['sh']) -> False
             starts_with('saiin', 's', exclude=['sh']) -> True
    """
    if not token.startswith(prefix):
        return False
    if exclude:
        for exc in exclude:
            if token.startswith(exc):
                return False
    return True


def token_density(records: list[dict],
                  prefix: str,
                  exclude: list[str] | None = None,
                  section: str | None = None) -> float:
    """
    Compute density of *prefix* in tokens per thousand (‰).

    Parameters
    ----------
    records  : output of parse_corpus()
    prefix   : prefix string to count
    exclude  : prefixes to exclude (e.g. ['sh'] when counting 's-')
    section  : if given, restrict to this section
    """
    total = 0
    hits  = 0
    for rec in records:
        if section and rec['section'] != section:
            continue
        for tok in rec['tokens']:
            total += 1
            if starts_with(tok, prefix, exclude):
                hits += 1
    return (hits / total * 1000) if total else 0.0


# ---------------------------------------------------------------------------
# Position helper
# ---------------------------------------------------------------------------

def normalised_position(idx: int, line_length: int) -> float:
    """
    Return the normalised position of token at *idx* in a line of *line_length*
    tokens.  0.0 = first token, 1.0 = last token.
    """
    if line_length == 1:
        return 0.0
    return idx / (line_length - 1)
