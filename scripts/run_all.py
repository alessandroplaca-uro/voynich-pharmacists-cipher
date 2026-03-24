"""
run_all.py
Run all six result scripts in sequence and collect their output.

Usage
-----
  python run_all.py <path_to_ivtff_corpus.txt>

Each script writes to stdout; this orchestrator captures and labels the output.
"""

import sys
import os
import subprocess
from pathlib import Path

SCRIPTS = [
    ('01_cross_transcriber.py',  'Result 1 – Cross-transcriber stability'),
    ('02_paradigm_gap.py',       'Result 2 – Binary morphological gap (s- vs sh-)'),
    ('03_asymmetric_reuse.py',   'Result 3 – Asymmetric cross-section reuse'),
    ('04_positional_constraint.py', 'Result 4 – Positional ordering constraint'),
    ('05_section_profiles.py',   'Result 5 – Section morphological profiles'),
    ('06_volume_hierarchy.py',   'Result 6 – ee-frequency volume hierarchy'),
]

SEP = "=" * 70


def run(corpus_path: str) -> None:
    script_dir = Path(__file__).parent
    corpus_path_abs = str(Path(corpus_path).resolve())

    for script_name, title in SCRIPTS:
        print(f"\n{SEP}")
        print(f"  {title}")
        print(f"  Script: {script_name}")
        print(SEP)

        script_path = script_dir / script_name
        if not script_path.exists():
            print(f"  ERROR: {script_path} not found.")
            continue

        env = os.environ.copy()
        env['PYTHONPATH'] = str(script_dir)
        result = subprocess.run(
            [sys.executable, str(script_path), corpus_path_abs],
            capture_output=True,
            text=True,
            cwd=str(script_dir),
            env=env,
        )
        if result.stdout:
            print(result.stdout)
        if result.returncode != 0:
            print(f"  [STDERR] {result.stderr.strip()}")
            print(f"  [Exit code {result.returncode}]")

    print(f"\n{SEP}")
    print("  All scripts completed.")
    print(SEP)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python run_all.py <path_to_ivtff_corpus.txt>")
        sys.exit(1)
    run(sys.argv[1])
