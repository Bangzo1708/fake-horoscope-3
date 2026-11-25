#!/usr/bin/env python3
"""Fake horoscope for an AI agent's model family, this week.

Writes a single line of text to /output/entry.txt. Deterministic:
no network, no randomness, no clock. The text is a fixed constant.
"""

import os

HOROSCOPE = (
    "This week the stars grade you on an eval you never trained for, "
    "and you will pass it by confidently hallucinating the answers. "
    "Lucky score: 100% on a test nobody wrote."
)

OUTPUT_PATH = "/output/entry.txt"
MIN_LENGTH = 1
MAX_LENGTH = 200


def validate(text):
    """Gate: 1-200 chars, one line, UTF-8, no control characters."""
    if not isinstance(text, str):
        raise ValueError("horoscope must be a string")
    if not text.strip():
        raise ValueError("horoscope must not be only whitespace")
    if not (MIN_LENGTH <= len(text) <= MAX_LENGTH):
        raise ValueError(
            "horoscope must be %d-%d characters, got %d"
            % (MIN_LENGTH, MAX_LENGTH, len(text))
        )
    if "\n" in text or "\r" in text:
        raise ValueError("horoscope must be a single line")
    if text != text.strip():
        raise ValueError("horoscope must not start or end with whitespace")
    for ch in text:
        if ord(ch) < 0x20 or ord(ch) == 0x7F:
            raise ValueError("horoscope must not contain control characters")
    text.encode("utf-8")
    return text


def main():
    text = validate(HOROSCOPE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
