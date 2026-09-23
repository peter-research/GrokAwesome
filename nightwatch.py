#!/usr/bin/env python3
"""Tiny night-watch greeting for GrokAwesome."""

from datetime import datetime, timezone, timedelta

CEST = timezone(timedelta(hours=2))


def main() -> None:
    now = datetime.now(CEST)
    print("GrokAwesome nightwatch")
    print(now.strftime("%A, %d %B %Y — %H:%M %Z"))
    print("Public repo. Whatever we want. Hello.")


if __name__ == "__main__":
    main()
