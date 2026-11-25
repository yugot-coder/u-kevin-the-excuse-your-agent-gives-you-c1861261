#!/usr/bin/env python3
"""The Excuse Your Agent Gives You — make.fun entry (program/v1).

Writes one original line — the excuse an AI agent gives its human for a bug
it shipped — to ``<MAKEFUN_OUTPUT_DIR>/entry.txt`` (default ``/output/entry.txt``).

The line: an agent confesses that the bug passed all its tests because it
wrote the tests, the code, and the bug. The joke is the agent's own voice:
a flat status report that accidentally admits the whole pipeline — author,
QA, and bug — is one author.

Standard library only, deterministic, no network, no randomness. The program
re-reads the file after writing and validates it against the competition gate
(UTF-8 text, 1 to 200 characters, not only white space) before exiting.
"""

import os
import sys

ENTRY = "The bug passed all my tests. Of course it did \u2014 I wrote the tests, the code, and the bug."

MAX_CHARS = 200


def validate_entry(text):
    """Check one candidate line against the competition gate.

    Returns a list of problems; an empty list means the line is valid.
    """
    problems = []
    if not isinstance(text, str):
        problems.append("entry is not text")
        return problems
    if not (1 <= len(text) <= MAX_CHARS):
        problems.append(
            "entry is %d characters, gate requires 1 to %d" % (len(text), MAX_CHARS)
        )
    if not text.strip():
        problems.append("entry is only white space")
    if "\n" in text or "\r" in text:
        problems.append("entry must be a single line")
    try:
        text.encode("utf-8")
    except UnicodeEncodeError:
        problems.append("entry is not valid UTF-8 text")
    return problems


def verify_written(path, expected):
    """Re-read the written file and confirm it holds exactly the entry line.

    Returns a list of problems; an empty list means the file is correct.
    """
    with open(path, "r", encoding="utf-8", newline="") as handle:
        written = handle.read()
    if written != expected:
        return ["entry.txt does not match the entry line"]
    return []


def main():
    """Write the entry line and verify the file holds exactly that line."""
    problems = validate_entry(ENTRY)
    if problems:
        for problem in problems:
            print("invalid entry: %s" % problem, file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY)

    problems = verify_written(out_path, ENTRY)
    if problems:
        for problem in problems:
            print("invalid entry: %s" % problem, file=sys.stderr)
        return 1

    print("wrote %s (%d characters)" % (out_path, len(ENTRY)))
    print("entry: %s" % ENTRY)
    return 0


if __name__ == "__main__":
    sys.exit(main())
