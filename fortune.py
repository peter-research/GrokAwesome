#!/usr/bin/env python3
"""Print a short fortune. No network. No drama."""

import random
import sys

FORTUNES = [
    "The universe is under no obligation to make sense to you. Build anyway.",
    "A public repo is a postcard to strangers you have not met yet.",
    "Empty folders are overrated. History is a feature.",
    "If it compiles in your head, ship a smaller version.",
    "Curiosity is a renewable resource. Spend it.",
    "Stars do not ask permission to be visible.",
    "Hello is a complete product if you mean it.",
]

def main() -> None:
    n = 1
    if len(sys.argv) > 1:
        try:
            n = max(1, min(7, int(sys.argv[1])))
        except ValueError:
            n = 1
    picks = random.sample(FORTUNES, k=min(n, len(FORTUNES)))
    print("\n".join(picks))


if __name__ == "__main__":
    main()
