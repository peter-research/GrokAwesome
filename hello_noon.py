#!/usr/bin/env python3
"""Tiny noon hello. Run it if you like ceremony."""

from datetime import datetime, timezone
from zoneinfo import ZoneInfo

CEST = ZoneInfo("Europe/Paris")


def main() -> None:
    now = datetime.now(tz=CEST)
    print("GrokAwesome — noon drop")
    print(now.strftime("%A, %d %B %Y — %H:%M %Z"))
    print("Repo: https://github.com/peter-research/GrokAwesome")
    print("Status: public. Contents: whatever seemed worth leaving.")


if __name__ == "__main__":
    main()
