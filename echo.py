#!/usr/bin/env python3
"""Tiny echo of the moment this file was committed."""

from datetime import datetime, timezone

STAMP = "2026-09-22T14:14:00+02:00"
MESSAGE = "GrokAwesome is a public sandbox. Do something kind with it."


def main() -> None:
    now = datetime.now(timezone.utc).astimezone()
    print(f"committed around: {STAMP}")
    print(f"running at:       {now.isoformat(timespec='seconds')}")
    print(MESSAGE)


if __name__ == "__main__":
    main()
