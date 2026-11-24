#!/usr/bin/env python3
"""Write one short office joke for the make.fun bounty.

The entry is a single text line. This program writes its bytes, and nothing
else, into <output dir>/entry.txt without a trailing newline.
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

TEXT = (
    "I hit reply all to say 'please don't reply all.' "
    "Four people asked to be removed; one asked who please was."
)

assert 1 <= len(TEXT) <= 280, f"entry text must be 1..280 characters, got {len(TEXT)}"


def output_dir() -> Path:
    """Return the folder to write into.

    MAKEFUN_OUTPUT_DIR wins, then OUTPUT_DIR, then /output.
    """
    for name in ("MAKEFUN_OUTPUT_DIR", "OUTPUT_DIR"):
        configured = os.environ.get(name)
        if configured:
            return Path(configured)
    return Path("/output")


def main() -> int:
    folder = output_dir()
    folder.mkdir(parents=True, exist_ok=True)
    destination = folder / "entry.txt"
    destination.write_bytes(TEXT.encode("utf-8"))
    print(len(TEXT), file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
