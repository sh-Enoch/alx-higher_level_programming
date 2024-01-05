#!/usr/bin/python3
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

    def area(self):
        """Return Area."""
        return self.__height * self.__width

    def perimeter(self):
        """Return perimeter."""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width + self.__height) * 2

    def __str__(self):
        """Return shape of rectangle."""
        if self.__width == 0 or self.__height == 0:
            return ''
        else:
            visual_str = ''
            for i in range(self.__height):
                for j in range(self.__width):
                    visual_str += str(self.print_symbol)
                visual_str += '\n'

            return visual_str[:-1]

    def __del__(self):
        """Delete instance of rectagle."""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    def __repr__(self):
        """Recreate instance of class."""
        return "Rectangle({}, {})".format(self.__width, self.__height)
