#!/usr/bin/python3
"""Define class Rectangle that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Define class rectangle."""

    def __init__(self, width, height):
        """Initialize the class."""
        self.integer_validator('width', width)
        self.__width = width
        self.integer_validator('height', height)
        self.__height = height

    def area(self):
        """Implement area."""
        return self.__width * self.__height

    def __str__(self):
        """String representation."""
        a = type(self).__name__
        return "[{}] {}/{}".format(a, self.__width, self.__height)
