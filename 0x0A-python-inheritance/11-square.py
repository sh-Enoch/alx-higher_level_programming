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
        a = type(self).__name__
        return "[{}] {}/{}".format(a, self.__size, self.__size)
