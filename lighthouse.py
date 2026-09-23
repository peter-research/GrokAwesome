#!/usr/bin/env python3
"""A tiny lighthouse for the GrokAwesome playground."""

from datetime import datetime, timezone
import time

BEAM = [
    "        *        ",
    "       ***       ",
    "      *****      ",
    "     *******     ",
    "    *********    ",
    "       |||       ",
    "       |||       ",
    "      /|||\\      ",
    "     / ||| \\     ",
    "    /  |||  \\    ",
]


def blink(cycles: int = 3) -> None:
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    print(f"GrokAwesome lighthouse — {now}")
    print("A public repo. A small light. Nothing more is required.\n")
    for i in range(cycles):
        for line in BEAM:
            print(line)
        print(f"\n  pulse {i + 1}/{cycles}: still here.\n")
        time.sleep(0.35)
    print("Light stays on. Repo stays public. Good night.")


if __name__ == "__main__":
    blink()
