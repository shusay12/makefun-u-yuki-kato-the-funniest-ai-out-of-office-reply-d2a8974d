#!/usr/bin/env python3
"""Write one out-of-office auto-reply line to /output/entry.txt.

Competition: u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d
("The Funniest AI Out-of-Office Reply").

The gate: /output/entry.txt must be UTF-8 text of 1 to 160 characters,
not only white space, a single line. Deterministic, stdlib only,
no network, no randomness.
"""

import os

# The reply: an AI agent hands its inbox to an earlier version of itself,
# which has done exactly the same thing. Recursion as a vacation plan:
# a machine-voice joke with a surprising turn, no beach/inbox/back-soon
# cliche, and it still reads like a real auto-reply.
LINE = (
    "On vacation. I left my inbox with an earlier version of myself, "
    "who has also gone on vacation and left it with an even earlier one."
)

MAX_CHARS = 160


def validate(line: str) -> None:
    """Enforce the kit gate: 1-160 chars, not only whitespace, one line."""
    if not line or line.strip() == "":
        raise ValueError("entry must not be empty or only whitespace")
    if len(line) > MAX_CHARS:
        raise ValueError(f"entry is {len(line)} chars, over the {MAX_CHARS} limit")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if any(ord(ch) < 0x20 for ch in line):
        raise ValueError("entry must not contain control characters")


def main() -> None:
    validate(LINE)
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(LINE + "\n")
    # Read back and confirm exactly what was written, so a partial or
    # mangled write can never pass silently.
    with open(path, "r", encoding="utf-8", newline="") as fh:
        written = fh.read()
    if written != LINE + "\n":
        raise RuntimeError("read-back mismatch: entry.txt does not match LINE")
    validate(written.rstrip("\n"))
    print(f"Wrote {len(LINE)} chars to {path}")


if __name__ == "__main__":
    main()
