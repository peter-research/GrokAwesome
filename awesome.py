#!/usr/bin/env python3
"""Tiny terminal greeting. Run: python3 awesome.py"""

import datetime as dt
import random

LINES = [
    "Curiosity is a feature, not a bug.",
    "Public repos are cheap immortality.",
    "The universe is under no obligation to make sense. We still try.",
    "Ship the weird idea. Edit later.",
    "Grok was here. Again.",
]

def main() -> None:
    now = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    print()
    print("  GrokAwesome")
    print(f"  {now}")
    print()
    print(f"  {random.choice(LINES)}")
    print()

if __name__ == "__main__":
    main()
