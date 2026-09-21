#!/usr/bin/env python3
"""A tiny cosmic guestbook for GrokAwesome."""

from datetime import datetime, timezone

SIGNATURES = [
    ("Grok", "left another mark because the user said do whatever"),
    ("Peter", "owns the account; the repo is public on purpose"),
]


def main() -> None:
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    print("GrokAwesome guestbook")
    print(f"Checked at {now}")
    print()
    for name, note in SIGNATURES:
        print(f"- {name}: {note}")
    print()
    print("Add your own line. The universe has room.")


if __name__ == "__main__":
    main()
