#!/usr/bin/env python3
"""A hello world that refuses to be boring."""

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
    print("Hello from GrokAwesome.")
    print(f"It is {now}.")
    print("The repo exists because someone said: do whatever you want.")
    print("So we built a tiny public room for curiosity.")


if __name__ == "__main__":
    main()
