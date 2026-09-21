#!/usr/bin/env python3
"""Print a handful of cosmic one-liners."""

from __future__ import annotations

import argparse
import random

QUOTES = [
    "The universe is under no obligation to make sense to you. — Neil deGrasse Tyson",
    "We are a way for the cosmos to know itself. — Carl Sagan",
    "Not only is the universe stranger than we imagine, it is stranger than we can imagine. — J. B. S. Haldane",
    "If you wish to make an apple pie from scratch, you must first invent the universe. — Carl Sagan",
    "Curiosity is not a bug. It is the whole product.",
    "Build small things that tell the truth.",
    "Awesome is not a feature. It is a mood.",
]


def main() -> None:
    parser = argparse.ArgumentParser(description="Print cosmic one-liners.")
    parser.add_argument("--count", type=int, default=1, help="How many quotes to print")
    args = parser.parse_args()
    count = max(1, min(args.count, len(QUOTES)))
    for quote in random.sample(QUOTES, count):
        print(quote)


if __name__ == "__main__":
    main()
