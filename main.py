#!/usr/bin/env python3
"""One Line, One Chill — writes the winning horror line to /output/entry.txt.

The line below won the local pairwise tournament: 7 candidate lines, every
pair judged in both orders by the Caffeine Inference router under the
bounty's published judge brief (42 judge calls). The winner's mean game
score was 0.617 — it beat the baby-monitor line 0.80, the suicide-note line
0.75 and the warm-chair line 0.75, drew the grave-text line 0.50, and lost
narrowly to the grocery-list line 0.45 and the daughter's-drawings line
0.45. Full table in README.md; every call is recorded in tournament.jsonl.
"""

import os

LINE = "Every photo in my grandmother's album has me standing in the background, smiling, forty years before I was born."

def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    line = LINE.strip()
    assert 1 <= len(line) <= 200, f"line is {len(line)} chars, must be 1-200"
    assert "\n" not in line, "entry must be a single line"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line)

if __name__ == "__main__":
    main()
