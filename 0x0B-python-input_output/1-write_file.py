#!/usr/bin/python3
"""Appends a string at the end of atext file."""


def write_file(filename="", text=""):
    """Append a string."""
    with open(filename, "w", encoding="UTF8") as f:
        f.write(text)
    return len(text)
