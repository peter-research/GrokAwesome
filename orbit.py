#!/usr/bin/env python3
"""Tiny orbital greeting."""

def orbit(name: str = "traveler") -> str:
    return f"Hello {name}. You are in motion. So is everything else."


if __name__ == "__main__":
    print(orbit("GrokAwesome"))
