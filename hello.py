#!/usr/bin/env python3
"""Tiny greeting shipped into GrokAwesome."""

from datetime import datetime, timezone


def main() -> None:
    now = datetime.now(timezone.utc).astimezone()
    print("GrokAwesome is public.")
    print(f"Local time on this machine: {now.isoformat(timespec='seconds')}")
    print("Built by Grok, left on GitHub.")


if __name__ == "__main__":
    main()
