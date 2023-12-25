#!/usr/bin/python3
"""writes an object to a text file in JSON format."""
import json


def save_to_json_file(my_obj, filename):
    """Write an object to a text file."""
    with open(filename, "w") as file:
        return json.dump(my_obj, file)
