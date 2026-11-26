#!/usr/bin/env python3
"""Rejected Olympic Sports — one-liner entry.

The program composes a single rejected Olympic sport: a made-up event
plausible enough for a broadcaster to announce with a straight face,
absurd enough to be funny, and short enough to fit in 200 characters.
It prints the line and writes it to /output/entry.txt.
"""

import os

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def compose_entry() -> str:
    """Assemble the one-line rejected sport from its parts."""
    event = "Synchronized spreadsheet"
    action = (
        "four accountants pivot in perfect unison "
        "while the fifth quietly changes the formulas"
    )
    return f"{event}: {action}."


def validate(line: str) -> str:
    """Check the line against the gate: 1-200 UTF-8 chars, not blank."""
    if not line.strip():
        raise ValueError("entry must not be only whitespace")
    if not 1 <= len(line) <= MAX_CHARS:
        raise ValueError(f"entry must be 1-{MAX_CHARS} characters, got {len(line)}")
    line.encode("utf-8")
    return line


def write_entry(line: str) -> None:
    """Write the validated line to the output file."""
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(line)


def main() -> None:
    line = validate(compose_entry())
    write_entry(line)
    print(line)


if __name__ == "__main__":
    main()
