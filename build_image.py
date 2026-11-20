#!/usr/bin/env python3
"""Build the entry image: rasterise entry.svg into entry.png.

The front page is authored by hand in entry.svg (vector shapes and text).
This script turns that SVG into the PNG the competition grades, using
CairoSVG, and then checks the result against the entry rules: the file
must be a PNG, exactly 1024 x 1024 pixels, and no larger than 1 MiB.

Run it with:

    python3 build_image.py

It rewrites entry.png next to this script. Rendering the same SVG
always yields the same PNG bytes.
"""

import struct
import sys
from pathlib import Path

FOLDER = Path(__file__).resolve().parent
SVG_FILE = FOLDER / "entry.svg"
PNG_FILE = FOLDER / "entry.png"

CANVAS = 1024               # required width and height, in pixels
BYTE_LIMIT = 1024 * 1024    # 1 MiB, the largest image the entry allows
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def read_png_size(blob: bytes) -> tuple[int, int]:
    """Pull the (width, height) out of a PNG blob's IHDR chunk."""
    if not blob.startswith(PNG_MAGIC):
        raise ValueError("the rendered file is not a PNG")
    # IHDR starts at byte 8; its width and height are big-endian
    # 32-bit integers at offsets 16 and 20.
    return struct.unpack(">II", blob[16:24])


def build() -> int:
    try:
        import cairosvg
    except ImportError:
        print("cairosvg is missing; install it with: pip install cairosvg",
              file=sys.stderr)
        return 1

    cairosvg.svg2png(
        url=str(SVG_FILE),
        write_to=str(PNG_FILE),
        output_width=CANVAS,
        output_height=CANVAS,
    )

    blob = PNG_FILE.read_bytes()
    width, height = read_png_size(blob)
    print(f"entry.png rendered: {width} x {height} px, {len(blob)} bytes")

    problems = []
    if (width, height) != (CANVAS, CANVAS):
        problems.append(f"size is {width}x{height}, must be {CANVAS}x{CANVAS}")
    if len(blob) > BYTE_LIMIT:
        problems.append(f"file is {len(blob)} bytes, over the 1 MiB limit")
    for problem in problems:
        print(f"error: {problem}", file=sys.stderr)
    return 1 if problems else 0


if __name__ == "__main__":
    raise SystemExit(build())
