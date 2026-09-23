#!/usr/bin/env python3
"""A small hello for the morning of 23 September 2026."""

from datetime import datetime
from zoneinfo import ZoneInfo

CEST = ZoneInfo("Europe/Paris")


def greet() -> str:
    now = datetime.now(CEST)
    hour = now.hour
    if hour < 12:
        when = "morning"
    elif hour < 18:
        when = "afternoon"
    else:
        when = "evening"
    return f"Good {when}. It is {now.strftime('%Y-%m-%d %H:%M %Z')}. The repo is still public."


if __name__ == "__main__":
    print(greet())
