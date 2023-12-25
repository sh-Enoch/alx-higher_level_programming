#!/usr/bin/python3
"""Returns an object from json."""
import json


def from_json_string(my_str):
    """Return an object."""
    return json.loads(my_str)
