#!/usr/bin/env python3
"""The Internet in One Word -- make.fun entry.

Writes one word to /output/entry.txt: the whole internet, described
in a single word. The word is "feral": funny on its own, true of the
internet as a whole (untamed, unsupervised, no one in charge, bites
back), surprising (not the first obvious word anyone reaches for),
and five letters that land in one beat.

The program is deliberately tiny and deterministic: it writes the
same five bytes on every run, reads nothing, and needs no network.
"""

import os

WORD = "feral"

# The grader runs the program in a sandbox and reads /output/entry.txt.
# MAKEFUN_OUTPUT exists only so the same program can be verified on a
# machine where /output is not the sandbox directory.
OUTPUT_PATH = os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt")


def main() -> None:
    parent = os.path.dirname(OUTPUT_PATH)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(WORD)
    # Fail loudly instead of handing the grader a bad file: the gate
    # wants UTF-8 text of 1 to 30 characters, not only white space.
    with open(OUTPUT_PATH, "rb") as handle:
        written = handle.read()
    text = written.decode("utf-8")
    if not 1 <= len(text) <= 30 or not text.strip():
        raise SystemExit(f"refusing to leave an invalid entry: {written!r}")


if __name__ == "__main__":
    main()
