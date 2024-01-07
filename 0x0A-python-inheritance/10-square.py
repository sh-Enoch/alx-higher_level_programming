#!/usr/bin/python3
"""Define class Square that inherits from Rectangle."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Define class Square."""

    def __init__(self, size):
        """Initialize the class."""
        self.integer_validator('size', size)
        self.__size = size

    def area(self):
        """Return area."""
        return self.__size ** 2

    def __str__(self):
        """Return string representation."""
        return "[Rectangle] {}/{}".format(self.__size, self.__size)
