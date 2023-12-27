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
            __nb_objects += 1
            self.id = __nb_objects
