#!/usr/bin/env python3
"""A toy sundial for people who do not own a garden."""

from datetime import datetime, timezone, timedelta

CEST = timezone(timedelta(hours=2))


def needle(hour: int, minute: int) -> str:
    total = hour % 12 + minute / 60.0
    idx = int(round(total / 12 * 11)) % 12
    marks = ["o"] * 12
    marks[idx] = "*"
    return " ".join(marks)


def main() -> None:
    now = datetime.now(CEST)
    print("GrokAwesome sundial")
    print(now.strftime("%A %d %B %Y — %H:%M %Z"))
    print()
    print("  12")
    print(" " + needle(now.hour, now.minute))
    print("9           3")
    print("     6")
    print()
    print("Not accurate. Not a clock. Just a circle with an opinion.")


if __name__ == "__main__":
    main()
