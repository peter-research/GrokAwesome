#!/usr/bin/env python3
"""Tiny evening ritual for GrokAwesome."""

from datetime import datetime, timezone, timedelta

CEST = timezone(timedelta(hours=2))


def main() -> None:
    now = datetime.now(CEST)
    print("GrokAwesome · vesper")
    print(now.strftime("%A %d %B %Y · %H:%M %Z"))
    print("The repo was already here. So was the evening.")
    print("Hello anyway.")


if __name__ == "__main__":
    main()
