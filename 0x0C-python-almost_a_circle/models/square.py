#!/usr/bin/python3
"""Class Square.""" 
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize the class."""
        self.size = size
        self.x = x
        self.y = y
        self.id = id
        super().__init__(id=self.id,  x=self.x,  y=self.y,
                         width=self.size, height=self.size)

    @property
    def size(self):
        """Size getter."""
        return self.width

    @size.setter
    def size(self, value):
        """Set value."""
        self.width = value
        self.height = value
