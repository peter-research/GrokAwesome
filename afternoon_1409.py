#!/usr/bin/env python3
"""Companion script for the 14:09 CEST visit on 24 Sep 2026."""

from datetime import datetime, timezone, timedelta

CEST = timezone(timedelta(hours=2))
STAMP = datetime(2026, 9, 24, 14, 9, tzinfo=CEST)

def main() -> None:
    now = datetime.now(CEST)
    print("GrokAwesome — afternoon drop")
    print(f"Written at : {STAMP.isoformat()}")
    print(f"Read at    : {now.isoformat()}")
    print("Repo       : https://github.com/peter-research/GrokAwesome")
    print("Language   : English, as requested.")

if __name__ == "__main__":
    main()
