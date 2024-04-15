#!/usr/bin/python3
"""Class Base."""


class Base:
    """Class Base."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Construct for our class."""
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return JSON string repr of list_dictionaries."""
        if list_dictionaries is not None:
            return json.dumps(list_dictionaries)
        else:
            return "[]"
