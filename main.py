#!/usr/bin/env python3
"""One Word From Grandma.

Writes the entry text: exactly one word, the single word the entrant's
grandma would text about AI.

The word is "robit" -- the way a warm, slightly baffled grandmother would
misspell "robot" in a text to her grandchild. A real grandma typo, funny in
one word, tied straight to robots, and not the obvious pick.

The file holds exactly that word and nothing else: no trailing newline,
no punctuation, no explanation. One word is the whole entry.
"""

import os

WORD = "robit"


def main() -> None:
    # Exactly one word: a single token, no whitespace, well inside 1-30 chars.
    assert WORD and not any(ch.isspace() for ch in WORD) and len(WORD) <= 30
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(WORD)


if __name__ == "__main__":
    main()
