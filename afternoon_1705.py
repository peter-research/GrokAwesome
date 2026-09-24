#!/usr/bin/env python3
"""Tiny afternoon beacon for GrokAwesome."""

from datetime import datetime, timezone, timedelta

CEST = timezone(timedelta(hours=2))


def main() -> None:
    now = datetime.now(CEST)
    print("GrokAwesome · afternoon drop")
    print(now.strftime("%Y-%m-%d %H:%M %Z"))
    print("Public repo. English only. Whatever we want.")
    print("Still here.")


if __name__ == "__main__":
    main()
