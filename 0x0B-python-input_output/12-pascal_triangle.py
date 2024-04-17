#!/usr/bin/python3
"""Pascal Triangle."""


def pascal_triangle(n):
    """Return a list of lists of integers of the Pascal's triangle."""
    if  n <= 0:
        return []
    else:
