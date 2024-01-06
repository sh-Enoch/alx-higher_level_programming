#!usr/bin/python3
"""Class Rectangle."""


class Rectangle:
    """Define class Rectangle."""

    print_symbol = '#'
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Class constructor.

        ARGS:
            width(int) - initialized to 0.
            height(int) - initialized to 0.
        """
        self.__width = width
        self.__height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """Get width value."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width.

        Args:
            Value.
        """
        if isinstance(value, int):
            if value >= 0:
                self.__width = value
            else:
                raise ValueError('width must be >= 0')
        else:
            raise TypeError('width must be an integer')

    @property
    def height(self):
        """Get height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height."""
        if isinstance(value, int):
            if value >= 0:
                self.__height = value
            else:
                raise ValueError('height must be >= 0')
        else:
            raise TypeError('height must be an integer')
