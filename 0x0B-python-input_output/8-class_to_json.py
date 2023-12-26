#!/usr/bin/python3
"""Returns the dictionary description with a simple data structure."""


def class_to_json(obj):
    """Ruturn the dictionary description with simple data structure."""
    return obj.__dict__
