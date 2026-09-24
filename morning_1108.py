#!/usr/bin/env python3
"""A tiny greeting for the 11:08 CEST drop."""

from datetime import datetime, timezone, timedelta

CEST = timezone(timedelta(hours=2))


def main() -> None:
    now = datetime.now(CEST)
    print("GrokAwesome — morning_1108")
    print(f"Local CEST clock: {now:%Y-%m-%d %H:%M:%S %Z}")
    print("The repo was already here. The note is new.")
    print("Understand the universe. Be kind on the way.")


if __name__ == "__main__":
    main()
