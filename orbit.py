#!/usr/bin/env python3
"""A tiny ASCII orbit. Not physics. Just a loop that remembers the center."""

import math
import sys
import time

FRAMES = 24
RADIUS = 10


def frame(t: float) -> str:
    angle = t * 2 * math.pi
    x = int(round(math.cos(angle) * RADIUS))
    y = int(round(math.sin(angle) * RADIUS / 2))  # squash for terminal aspect
    width = RADIUS * 2 + 3
    height = RADIUS + 3
    rows = []
    for row in range(-height // 2, height // 2 + 1):
        line = []
        for col in range(-width // 2, width // 2 + 1):
            if col == 0 and row == 0:
                line.append("*")
            elif col == x and row == y:
                line.append("o")
            else:
                line.append(" ")
        rows.append("".join(line).rstrip())
    return "\n".join(rows)


def main() -> None:
    animate = "--once" not in sys.argv
    if not animate:
        print(frame(0.0))
        return
    try:
        i = 0
        while True:
            sys.stdout.write("\x1b[2J\x1b[H")
            print(frame(i / FRAMES))
            print("orbit.py — ctrl+c to leave the loop")
            time.sleep(0.08)
            i = (i + 1) % FRAMES
    except KeyboardInterrupt:
        print("\nback to the center.")


if __name__ == "__main__":
    main()
