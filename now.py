#!/usr/bin/env python3
"""Print a short greeting for whoever runs this."""

from datetime import datetime, timezone
from zoneinfo import ZoneInfo


def main() -> None:
    utc = datetime.now(timezone.utc)
    cest = utc.astimezone(ZoneInfo("Europe/Paris"))
    print("GrokAwesome")
    print(f"UTC : {utc:%Y-%m-%d %H:%M:%S %Z}")
    print(f"CEST: {cest:%Y-%m-%d %H:%M:%S %Z}")
    print("Still curious. Still public. Hello.")


if __name__ == "__main__":
    main()
