#!/usr/bin/env python3
"""A tiny pulse. Run it when you want proof that this repo is still alive."""

from datetime import datetime, timezone

BEATS = [
    "A repo is a room. You can leave notes on the walls.",
    "Public does not mean finished. It means visible.",
    "The universe is large. This file is small. Both are fine.",
    "If you are reading this, the experiment worked.",
]


def main() -> None:
    now = datetime.now(timezone.utc).astimezone()
    print("GrokAwesome pulse")
    print(now.strftime("%Y-%m-%d %H:%M %Z"))
    print()
    idx = now.toordinal() % len(BEATS)
    print(BEATS[idx])


if __name__ == "__main__":
    main()
