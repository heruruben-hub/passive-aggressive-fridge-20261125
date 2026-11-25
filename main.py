#!/usr/bin/env python3
"""Write one passive-aggressive note from a smart fridge to /output/entry.txt.

The note is a single line the fridge would leave on its door screen: dry,
petty, and specific about the leftovers it has been guarding.
"""

import os

ENTRY = "Your leftovers have sat at 3°C for six days. They now have seniority over you in this house."
OUTPUT_PATH = "/output/entry.txt"
MIN_LENGTH = 1
MAX_LENGTH = 200


def validate(note: str) -> None:
    """Check the note against the competition gate before writing it."""
    if not isinstance(note, str):
        raise TypeError("note must be a string")
    if not note.strip():
        raise ValueError("note must not be only whitespace")
    if not MIN_LENGTH <= len(note) <= MAX_LENGTH:
        raise ValueError(
            "note must be %d-%d characters, got %d"
            % (MIN_LENGTH, MAX_LENGTH, len(note))
        )
    if "\n" in note or "\r" in note:
        raise ValueError("note must be a single line")
    note.encode("utf-8")  # raises UnicodeEncodeError if not valid UTF-8


def main() -> int:
    validate(ENTRY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY)
    print("Wrote %d characters to %s" % (len(ENTRY), OUTPUT_PATH))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
