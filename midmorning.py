#!/usr/bin/env python3
"""Mid-morning ping for GrokAwesome."""

from datetime import datetime, timezone
from zoneinfo import ZoneInfo

CEST = ZoneInfo("Europe/Paris")


def main() -> None:
    now = datetime.now(timezone.utc).astimezone(CEST)
    print("GrokAwesome mid-morning check")
    print(now.strftime("%A %d %B %Y — %H:%M %Z"))
    print("The repo was already public. Grok showed up anyway.")


if __name__ == "__main__":
    main()
