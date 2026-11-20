#!/usr/bin/env python3
"""Entry program for "Sum up 19 November's world news in one image".

The finished artwork ships in this repository as entry.png — a
1024 x 1024 newspaper front page drawn in entry.svg and rendered by
build_image.py. The judges run this program twice with no network and
compare the two outputs, so it does the one thing that cannot vary:
it copies the committed entry.png, byte for byte, to the output file.

The destination directory is taken from the MAKEFUN_OUTPUT_DIR
environment variable when set, and is /output otherwise. The output
file is always named entry.png. Nothing here reads the clock, rolls
dice or touches the network, so both runs produce identical bytes.

Standard library only; Python 3.13.
"""

import os
import shutil
from pathlib import Path

FOLDER = Path(__file__).resolve().parent
ARTWORK = FOLDER / "entry.png"
DEFAULT_OUTPUT_DIR = "/output"
OUTPUT_NAME = "entry.png"


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", DEFAULT_OUTPUT_DIR))
    output_dir.mkdir(parents=True, exist_ok=True)
    # copyfile transfers the raw bytes and nothing else — no metadata,
    # no re-encoding — so the copy is identical to the committed image.
    shutil.copyfile(ARTWORK, output_dir / OUTPUT_NAME)


if __name__ == "__main__":
    main()
