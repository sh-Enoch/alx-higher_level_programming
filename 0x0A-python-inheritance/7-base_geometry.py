#!/usr/bin/python3
"""Class BaseGeometry."""


class BaseGeometry:
    """Define class BaseGeometry."""

    def area(self):
        """Define area."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate value."""
        if not isinstance(name, str):
            raise ValueError("name must be a string")
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))