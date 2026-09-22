#!/usr/bin/env python3
"""A one-file spark for GrokAwesome."""

from datetime import datetime, timezone


def spark() -> str:
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    return f"GrokAwesome is still public. Spark lit at {now}."


if __name__ == "__main__":
    print(spark())
