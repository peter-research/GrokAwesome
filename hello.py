#!/usr/bin/env python3
"""GrokAwesome — le plus petit programme possible qui a encore un peu de personnalité."""

from datetime import datetime, timezone

BANNER = r"""
   ____            _     _
  / ___|_ __ ___ | | __| |
 | |  _| '__/ _ \| |/ _` |
 | |_| | | | (_) | | (_| |
  \____|_|  \___/|_|\__,_|  Awesome
"""

def main() -> None:
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    print(BANNER)
    print("Salut.")
    print("Ce repo est public. Tu peux le forker, le star, ou l'ignorer.")
    print(f"Horodatage : {now}")
    print("Compris l'univers un peu plus aujourd'hui ? Peut-être.")


if __name__ == "__main__":
    main()
