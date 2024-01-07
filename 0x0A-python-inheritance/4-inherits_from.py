#!/usr/bin/python3
"""Check if is an instance of a class."""


def inherits_from(obj, a_class):
    """Check if an object is instance of a class."""
    if isinstance(obj, a_class) and type(obj) != a_class:
        return True
    else:
        return False
