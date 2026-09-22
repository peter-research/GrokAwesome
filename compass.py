#!/usr/bin/env python3
"""A tiny compass for days when the map is optional."""

from datetime import datetime, timezone

DIRECTIONS = [
    "North — toward questions that do not fit in a ticket.",
    "East — toward the next thing you have not built yet.",
    "South — toward the code you already wrote and almost forgot.",
    "West — toward rest, which is also a kind of work.",
]


def main() -> None:
    now = datetime.now(timezone.utc)
    idx = (now.hour + now.minute) % len(DIRECTIONS)
    print("GrokAwesome compass")
    print(now.strftime("%Y-%m-%d %H:%M UTC"))
    print()
    print(DIRECTIONS[idx])


if __name__ == "__main__":
    main()
