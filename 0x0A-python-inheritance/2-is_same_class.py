#!/usr/bin/python3
"""If object is instance of class."""


def is_same_class(obj, a_class):
    """Check if obj is in a_class."""
    if type(obj) is a_class:
        return True
    return False
