#!/usr/bin/python3
"""Defines a class Rectangle."""

class Rectangle:
    """This a class rectangle."""
    
    def  __init__(self, width=0, height=0):
        """Initialize a new instance of rectangle.

        Args:
           width (int):  private instance attribute.
           height (int): private instance attribute.
        """
        self.__width= width
        self.__height = height

    @property
    def width(self):
        """Get the value of width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the new value of the private attribute.

        Args:
           value(int): value to return 
        """
        try:
            if not isinstance(value, int):
                raise TypeError("width must be an integer")
            elif value < 0:
                raise ValueError("width must be >= 0")
            else:
                self.__width = value
        except TypeError as e:
            print(e)
        except ValueError as e:
            return e

    @property
    def height(self):
        """Get the value of the height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Define  a setter method height.

        Args:
            value(int): value to be set.
        """
        try:
            if not isinstance(value, int):
                raise TypeError("height must be an integer")
            elif value < 0:
                raise ValueError("height must be >= 0")
            else:
                self.__height = value 
        except TypeError as e:
            print(e)
        except ValueError as e:
            print(e)
