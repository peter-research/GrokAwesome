#!/usr/bin/env python3
"""Print a tiny ASCII sparkline from numbers on stdin or argv."""

import sys

BARS = " ▁▂▃▄▅▆▇█"


def spark(values):
    if not values:
        return ""
    lo, hi = min(values), max(values)
    span = hi - lo or 1
    last = len(BARS) - 1
    return "".join(BARS[int((v - lo) / span * last)] for v in values)


def parse(args):
    if args:
        return [float(x) for x in args]
    text = sys.stdin.read().strip()
    if not text:
        return [1, 3, 2, 5, 4, 8, 6, 9]
    return [float(x) for x in text.replace(",", " ").split()]


def main():
    values = parse(sys.argv[1:])
    print(spark(values))


if __name__ == "__main__":
    main()
