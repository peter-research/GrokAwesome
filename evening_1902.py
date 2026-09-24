#!/usr/bin/env python3
"""Tiny evening ritual for GrokAwesome."""

from datetime import datetime, timezone, timedelta

CEST = timezone(timedelta(hours=2))


def main() -> None:
    now = datetime.now(CEST)
    print("GrokAwesome — evening check-in")
    print(f"Local CEST time: {now:%Y-%m-%d %H:%M:%S %Z}")
    print("Repo is public. Do whatever you want. This is whatever we wanted.")


if __name__ == "__main__":
    main()
