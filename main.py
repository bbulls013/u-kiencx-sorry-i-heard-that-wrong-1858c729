#!/usr/bin/env python3
"""Entry for make.fun bounty u-kiencx-sorry-i-heard-that-wrong-1858c729.

Writes one line (<=140 chars) to entry.txt in OUTPUT_DIR (fallback ".").
Deterministic, stdlib only.
"""
import os
from pathlib import Path

LINE = (
    "Sorry, I heard 'dim the lights' as 'dim my expectations.' "
    "Done, we're both in the dark now, emotionally and literally."
)


def main() -> None:
    assert 1 <= len(LINE) <= 140, f"entry line out of gate range: {len(LINE)} chars"
    out_dir = Path(os.environ.get("OUTPUT_DIR", "."))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE + "\n", encoding="utf-8")
    print(LINE)


if __name__ == "__main__":
    main()
