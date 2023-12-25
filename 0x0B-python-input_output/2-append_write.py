#!/usr/bin/python3
"""Appends a string at the end of a text file."""


def append_write(filename="", text=""):
    """Append text to file."""
    with open(filename, "a", encoding="UTF8") as file:
        file.write(text)
    return len(text)
