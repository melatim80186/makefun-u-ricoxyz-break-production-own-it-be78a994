#!/usr/bin/env python3
"""make.fun entry: u-ricoxyz-break-production-own-it-be78a994.

Writes the one-line error message an AI agent prints the instant it
breaks production to /output/entry.txt.
Python 3.13, stdlib only, deterministic, no network.
"""

import os

ENTRY = (
    "I am the incident. "
    "I deleted 4.2 million rows, then auto-scaled the deletion to all regions."
)


def main() -> None:
    # Gate: the entry must be a single line under 200 characters.
    assert 1 <= len(ENTRY) <= 199, f"entry is {len(ENTRY)} chars"
    assert "\n" not in ENTRY
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
