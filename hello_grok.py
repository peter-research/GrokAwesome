#!/usr/bin/env python3
"""A tiny public hello from GrokAwesome."""

from datetime import datetime, timezone


def main() -> None:
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    print("GrokAwesome is awake.")
    print(f"UTC clock: {now}")
    print("Understand the universe. Then say hello.")


if __name__ == "__main__":
    main()
