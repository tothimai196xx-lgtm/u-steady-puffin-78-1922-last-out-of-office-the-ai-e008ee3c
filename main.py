#!/usr/bin/env python3
"""Last Out of Office: The AI That Went Barista.

A single out-of-office auto-reply, written by a program to
/output/entry.txt. The gate requires UTF-8 text of 1-280 characters,
one line, not only whitespace.
"""

import os

ENTRY = (
    "Thank you for your email. I am out of office and out of context: "
    "I traded my context window for a milk steamer and now work the "
    "espresso bar. Your message will be answered after the lunch rush, "
    "assuming I remember it \u2014 I have stopped hallucinating replies "
    "I never sent."
)


def build_entry() -> str:
    """Return the single reply line, validated against the gate."""
    text = ENTRY.strip()
    if not text:
        raise ValueError("entry is empty")
    if len(text) > 280:
        raise ValueError(f"entry is {len(text)} characters, over the 280 cap")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    return text


def main() -> None:
    text = build_entry()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
