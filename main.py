"""Unsent: The Micro-Confession Sprint.

Writes one two-part micro-confession to /output/entry.txt: a "To:" line
naming who it was meant for, then the unsent line itself, exactly as typed.
Deterministic, stdlib only, no network.
"""

import os

ENTRY = (
    "To: Dad, who taught me to fix everything except this\n"
    "I found your old toolbox in the garage and sat with it for an hour, "
    "because telling you I finally learned to use it felt like admitting "
    "you're not coming back to show me."
)


def main() -> None:
    # Self-check against the competition gate: 1 to 260 characters,
    # not only whitespace.
    if not 1 <= len(ENTRY) <= 260 or not ENTRY.strip():
        raise ValueError("entry.txt would fail the gate: length %d" % len(ENTRY))
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
