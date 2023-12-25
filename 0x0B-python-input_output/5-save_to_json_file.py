#!/usr/bin/python3
"""writes an object to a text file in JSON format."""
import json


def save_to_json_file(my_obj, filename):
    """Write an object to a text file."""
    my_obj_dump = json.dumps(my_obj)
    with open(filename, "w", encoding="UTF8") as file:
        file.write(my_obj_dump)
