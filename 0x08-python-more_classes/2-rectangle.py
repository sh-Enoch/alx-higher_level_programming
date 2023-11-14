#!/usr/bin/python3
"""Define a class rectangle."""


class Rectangle:
    """Define a class rectangle.

    Args:
        pass
    """

    def __init__(self, width=0, height=0):
        """Initialize the class rectangle.

        Args:
            width(int): width attribute of type integer
            height(int): height attribute of type integer
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Width method that is used to get the value of width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Define a setter method width that sets the value of width.

        Args:
            value(int): value of type int

        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Define a method height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Define method height that sets the value of height.

        Args:
            value(int): value to be set.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Define a method area that returns area of rectangle.

        Args:
            No attributes.

        """
        return self.__height * self.__width

    def perimeter(self):
        """Define method perimeter that returns the perimeter of a rectangle.

        Args:
            No attributes

        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)
