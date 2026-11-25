#!/usr/bin/env python3
"""Fortune Cookie for the Liquidated Trader.

Writes one fortune cookie line to /output/entry.txt.

The line (12 words, 57 bytes):

    Your lucky numbers are 0, 0, 0, and 0. Spend them wisely.

Why this line: it opens in the most recognisable fortune-cookie voice
there is ("Your lucky numbers are ..."), the loss is the joke itself (a
liquidated trader's balance is all zeroes), and the punchline breaks the
oracle voice with deadpan advice that is impossible to follow -- you
cannot spend zeroes. Rueful and warm, never cruel: the cookie laughs
with the trader, not at him.

Deterministic: the same bytes on every run. No model calls, no network,
no randomness, no input files -- standard library only.
"""

import os

FORTUNE = "Your lucky numbers are 0, 0, 0, and 0. Spend them wisely."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(FORTUNE)


if __name__ == "__main__":
    main()
