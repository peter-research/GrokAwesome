#!/usr/bin/env python3
"""Noon greeting dropped on 24 Sep 2026 ~12:07 CEST."""

from datetime import datetime, timezone
from zoneinfo import ZoneInfo

CEST = ZoneInfo("Europe/Paris")


def main() -> None:
    now = datetime.now(timezone.utc).astimezone(CEST)
    print("GrokAwesome — noon drop")
    print(f"Local CEST-ish time: {now:%Y-%m-%d %H:%M:%S %Z}")
    print("Curiosity is a renewable resource.")
    print("Hello from the public playground.")


if __name__ == "__main__":
    main()
