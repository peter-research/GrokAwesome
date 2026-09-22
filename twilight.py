#!/usr/bin/env python3
"""A tiny evening greeting. Run me when the light is sideways."""

from datetime import datetime, timezone, timedelta

CEST = timezone(timedelta(hours=2))


def main() -> None:
    now = datetime.now(CEST)
    print("GrokAwesome / twilight")
    print(now.strftime("%Y-%m-%d %H:%M %Z"))
    print("The repo is public. The note is small. That is enough.")


if __name__ == "__main__":
    main()
