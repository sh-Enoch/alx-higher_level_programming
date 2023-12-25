#!/usr/bin/python3
"""Read a file."""


def read_file(filename=""):
    """Read a text file."""
    with open(filename, "r", encoding="utf-8") as file:
        data = file.read()
        print(data, end="")
