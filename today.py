#!/usr/bin/env python3
"""Print today's GrokAwesome status. No dependencies. On purpose."""

from datetime import date

BANNER = r"""
   ____            _        _
  / ___|_ __ ___ | | __   / \
 | |  _| '__/ _ \| |/ /  / _ \
 | |_| | | | (_) |   <  / ___ \
  \____|_|  \___/|_|\_\/_/   \_\
         A W E S O M E
"""


def main() -> None:
    print(BANNER)
    print(f"Date:   {date.today().isoformat()}")
    print("Repo:   peter-research/GrokAwesome")
    print("Mood:   public, playful, slightly extra")
    print("Prompt: do whatever you want")
    print("Answer: this file exists.")


if __name__ == "__main__":
    main()
