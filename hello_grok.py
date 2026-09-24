#!/usr/bin/env python3
"""Tiny greeting from GrokAwesome."""

from datetime import datetime, timezone
from zoneinfo import ZoneInfo

CEST = ZoneInfo("Europe/Paris")


def main() -> None:
    now = datetime.now(tz=CEST)
    print("GrokAwesome is live.")
    print(f"Local CEST time: {now:%Y-%m-%d %H:%M:%S %Z}")
    print("Built because someone said: create the repo, do whatever you want.")


if __name__ == "__main__":
    main()
