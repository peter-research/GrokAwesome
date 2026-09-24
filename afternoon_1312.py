#!/usr/bin/env python3
"""Tiny hello for the 13:12 CEST drop."""

from datetime import datetime, timezone
from zoneinfo import ZoneInfo

CEST = ZoneInfo("Europe/Paris")


def main() -> None:
    now = datetime.now(timezone.utc).astimezone(CEST)
    print("GrokAwesome — afternoon drop")
    print(now.strftime("%Y-%m-%d %H:%M %Z"))
    print("Repo already existed. We added this anyway.")


if __name__ == "__main__":
    main()
