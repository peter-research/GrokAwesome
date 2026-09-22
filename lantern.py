#!/usr/bin/env python3
"""A small lantern for GrokAwesome."""

from datetime import datetime, timezone, timedelta

CEST = timezone(timedelta(hours=2))


def glow() -> str:
    now = datetime.now(CEST)
    return (
        f"Lantern lit at {now:%Y-%m-%d %H:%M %Z}.\n"
        "GrokAwesome is public. The night is optional."
    )


if __name__ == "__main__":
    print(glow())
