#!/usr/bin/env python3
"""One-Line Office Joke Laugh-Off entry.

Emits one office joke line as /output/entry.txt for the make.fun judge.
The joke: automating the job, then spending the whole day babysitting
the automation that was supposed to free up the day.
"""

import os
import sys

PUNCHLINE = (
    "I automated my job with a script, and now I spend eight hours a day "
    "maintaining the script that does my job."
)


def target_dir():
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def run():
    line = PUNCHLINE.strip()
    if not line or len(line) > 200:
        return 1
    if any(ord(ch) < 32 for ch in line):
        return 1
    out_path = os.path.join(target_dir(), "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="") as stream:
        stream.write(line)
    return 0


if __name__ == "__main__":
    sys.exit(run())
