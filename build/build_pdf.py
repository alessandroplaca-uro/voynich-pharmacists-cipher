#!/usr/bin/env python3
"""
Build PDF of The Pharmacists' Cipher vt1.7
from THE_PHARMACISTS_CIPHER_FINAL_PAPER.md using pandoc + WeasyPrint.
Matches vt1.6 Italian working paper style.

Requirements:
    pip install weasyprint
    apt install pandoc (or brew install pandoc)

Usage (from repo root):
    python3 build/build_pdf.py
"""

import subprocess
import re
import sys
import os

REPO_ROOT   = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INPUT_MD    = os.path.join(REPO_ROOT, "THE_PHARMACISTS_CIPHER_FINAL_PAPER.md")
CSS_FILE    = os.path.join(REPO_ROOT, "build", "paper_style.css")
OUTPUT_HTML = os.path.join(REPO_ROOT, "build", "paper_vt1.7.html")
OUTPUT_PDF  = os.path.join(REPO_ROOT, "Placa_2026_Pharmacists_Cipher_vt1.7.pdf")

# ── 1. Read source markdown ────────────────────────────────────────────────
with open(INPUT_MD, "r", encoding="utf-8") as f:
    md = f.read()

# ── 2. Extract title block info from first lines ───────────────────────────
lines = md.split("\n")
title      = ""
subtitle   = ""
date_str   = ""
author_str = ""
body_start = 0

for i, line in enumerate(lines):
    stripped = line.strip()
    if stripped.startswith("# ") and not title:
        title = stripped[2:]
    elif stripped.startswith("## ") and not subtitle and title:
        subtitle = stripped[3:]
    elif stripped.startswith("*Working draft") and not date_str:
        date_str = stripped.strip("*")
    elif stripped.startswith("*Alessandro") and not author_str:
        author_str = stripped.strip("*")
    elif stripped == "---" and date_str and author_str:
        body_start = i + 1
        break

body_md = "\n".join(lines[body_start:])

# ── 3. Convert markdown body to HTML with pandoc ──────────────────────────
print("Running pandoc...", flush=True)
result = subprocess.run(
    [
        "pandoc",
        "-f", "markdown+smart+pipe_tables+fenced_divs+inline_code_attributes",
        "-t", "html5",
        "--no-highlight",
        "--wrap=none",
    ],
    input=body_md,
    capture_output=True,
    text=True,
    encoding="utf-8",
)

if result.returncode != 0:
    print("Pandoc error:", result.stderr)
    sys.exit(1)

html_body = result.stdout
print(f"Pandoc done: {len(html_body)} chars of HTML", flush=True)

# ── 4. Post-process HTML ───────────────────────────────────────────────────
replacements = [
    ("🟢 SOLIDA",           '<span class="status-solid">&#x2713; SOLIDA</span>'),
    ("🟡 APERTA FORTE",     '<span class="status-open">&#x25CB; APERTA FORTE</span>'),
    ("🔵 STRUTTURA SOLIDA", '<span class="status-struct">&#x2022; STRUTTURA SOLIDA</span>'),
    ("❌",                   '<span class="status-falsified">&#x2717;</span>'),
    ("⚠️",                  '<span style="color:#996600">&#x26A0;</span>'),
    ("✘",                   '<span class="status-falsified">&#x2717;</span>'),
    ("→", "&rarr;"), ("←", "&larr;"), ("↑", "&uarr;"), ("↓", "&darr;"), ("↔", "&harr;"),
    ("≈", "&asymp;"), ("≤", "&le;"), ("≥", "&ge;"), ("≠", "&ne;"),
    ("×", "&times;"), ("−", "&minus;"), ("‰", "&#8240;"), ("…", "&hellip;"),
    ("\u2018", "&lsquo;"), ("\u2019", "&rsquo;"), ("\u201c", "&ldquo;"), ("\u201d", "&rdquo;"),
    ("—", "&mdash;"), ("–", "&ndash;"),
    ("ρ", "&rho;"), ("χ", "&chi;"), ("α", "&alpha;"), ("β", "&beta;"), ("γ", "&gamma;"), ("σ", "&sigma;"),
    ("⁻", "<sup>-</sup>"),
    ("⁰", "<sup>0</sup>"), ("¹", "<sup>1</sup>"), ("²", "<sup>2</sup>"), ("³", "<sup>3</sup>"),
    ("⁴", "<sup>4</sup>"), ("⁵", "<sup>5</sup>"), ("⁶", "<sup>6</sup>"),
    ("⁷", "<sup>7</sup>"), ("⁸", "<sup>8</sup>"), ("⁹", "<sup>9</sup>"),
    ("₀", "<sub>0</sub>"), ("₁", "<sub>1</sub>"), ("₂", "<sub>2</sub>"), ("₃", "<sub>3</sub>"),
]

for src, dst in replacements:
    html_body = html_body.replace(src, dst)

# ── 5. Build full HTML document ───────────────────────────────────────────
with open(CSS_FILE, "r", encoding="utf-8") as f:
    css = f.read()

# Remove @import (weasyprint can't load Google Fonts online)
css = re.sub(r'@import url\([^)]+\);?\s*', '', css)

title_html = f"""
<div class="title-block">
  <h1 class="title">{title}</h1>
  <h2 class="subtitle">{subtitle}</h2>
  <hr class="title-rule">
  <p class="author-date">{date_str}</p>
  <p class="author-date">{author_str}</p>
</div>
"""

full_html = f"""<!DOCTYPE html>
<html lang="it">
<head>
  <meta charset="utf-8">
  <title>The Pharmacists&rsquo; Cipher &mdash; vt1.7</title>
  <style>
{css}
  </style>
</head>
<body>
{title_html}
{html_body}
</body>
</html>"""

with open(OUTPUT_HTML, "w", encoding="utf-8") as f:
    f.write(full_html)
print(f"HTML written: {OUTPUT_HTML}", flush=True)

# ── 6. Convert HTML to PDF with WeasyPrint ────────────────────────────────
print("Running WeasyPrint...", flush=True)
try:
    from weasyprint import HTML
    from weasyprint.text.fonts import FontConfiguration
    font_config = FontConfiguration()
    HTML(filename=OUTPUT_HTML).write_pdf(OUTPUT_PDF, font_config=font_config)
    size = os.path.getsize(OUTPUT_PDF)
    print(f"PDF written: {OUTPUT_PDF} ({size/1024:.0f} KB)", flush=True)
except ImportError:
    result = subprocess.run(["weasyprint", OUTPUT_HTML, OUTPUT_PDF], capture_output=True, text=True)
    if result.returncode == 0:
        size = os.path.getsize(OUTPUT_PDF)
        print(f"PDF written: {OUTPUT_PDF} ({size/1024:.0f} KB)", flush=True)
    else:
        print("WeasyPrint error:", result.stderr[:500])
        sys.exit(1)

print("Done!", flush=True)
