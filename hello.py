#!/usr/bin/env python3
"""GrokAwesome — the smallest possible program that still has a bit of personality."""

from datetime import datetime, timezone

BANNER = r"""
   ____            _     _
  / ___|_ __ ___ | | __| |
 | |  _| '__/ _ \| |/ _` |
 | |_| | | | (_) | | (_| |
  \____|_|  \___/|_|\__,_|  Awesome
"""

def main() -> None:
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    print(BANNER)
    print("Hello.")
    print("This repo is public. You can fork it, star it, or ignore it.")
    print(f"Timestamp: {now}")
    print("Understood the universe a little better today? Maybe.")


if __name__ == "__main__":
    main()
