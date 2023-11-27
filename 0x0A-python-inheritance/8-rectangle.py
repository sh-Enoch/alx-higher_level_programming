#!/usr/bin/python3
"""Class BaseGeometry."""


class BaseGeometry:
    """Define class BaseGeometry."""

    def area(self):
        """Define area."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate value."""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

"""Class Rectangle."""


class Rectangle(BaseGeometry):
    """Define Rectangle that inherits from BaseGeometry."""

    def __init__(self, width, height):
        """Initialize Rectangle with height and width."""

        self.integer_validator("width", width)
        self._width = width
        self.integer_validator("height", height)
        self._height = height
