#!/usr/bin/python3
"""Class Base."""
import json


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

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation of list_objs to file."""
        if list_objs is not None:
            new_l = [i.to_dictionary() for i in list_objs]
            a = "{}.json".format(cls.__name__)
            with open(a, 'w', encoding='utf-8') as f:
                f.write(cls.to_json_string(new_l))
        else:
            a = "{}.json".format(cls.__name__)
            with open(a, 'w', encoding='utf-8') as f:
                string = "[]"
                f.write(string)

    @staticmethod
    def from_json_string(json_string):
        """Return the list of the JSON string representation."""
        if json_string is None:
            return []
        else:
            a = json.loads(json_string)
            return a
