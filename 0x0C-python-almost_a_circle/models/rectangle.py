#!/usr/bin/python3
"""Define class Rectangle."""
from models.base import Base


class Rectangle(Base):
    """Class Rectangle that inherits from Base."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize class Rectangle.

        Args:
            width(int): width
            height(int): height
            x(int): x
            y(int): y
            id(int): id
        """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """Get width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width value.

        Args:
          value(int): value to be set

        """
        if value >= 0:
            self.__width = value

    @property
    def height(self):
        """Get height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height.

        Args:
            value(int): value to be height
        """
        if value >= 0:
            self.__height = value

    @property
    def x(self):
        """Get x."""
        return self.__x

    @x.setter
    def x(self, value):
        """Set x.

        Args:
            value(int): value to be x

        """
        if value >= 0:
            self.__x = value

    @property
    def y(self):
        """Get y."""
        return self.__y

    @y.setter
    def y(self, value):
        """Set y."""
        if value >= 0:
            self.__y = value
