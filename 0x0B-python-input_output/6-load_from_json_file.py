#!/usr/bin/python3
"""Creates an object from a JSON fuile."""
import json


def load_from_json_file(filename):
    """Create an object from json."""
    with open(filename, "r") as file:
        return json.load(file)
