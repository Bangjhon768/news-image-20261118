#!/usr/bin/env python3
"""Write this entry's image to the output directory.

The image (entry.png) is a one-page newspaper front page summing up
Wednesday 18 November 2026, and it ships in this repository. The program
only copies it to the output path, so both runs write identical bytes.

Run locally:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""
import os
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "entry.png"
OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
TARGET = OUTPUT_DIR / "entry.png"


PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"
PNG_IEND = b"IEND\xaeB`\x82"


def read_image():
    """Read the image, refusing a file that is not a whole PNG."""
    data = SOURCE.read_bytes()
    if not data.startswith(PNG_SIGNATURE) or not data.endswith(PNG_IEND):
        print("entry.png is not a whole PNG", file=sys.stderr)
        return None
    return data


def main():
    if not SOURCE.is_file():
        print(f"missing image: {SOURCE}", file=sys.stderr)
        return 1
    data = read_image()
    if data is None:
        return 1
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    TARGET.write_bytes(data)
    print(f"wrote {TARGET} ({len(data)} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
