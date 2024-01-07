#!/usr/bin/pyhton3
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
