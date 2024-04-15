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

    def update(self, *args, **kwargs):
        """Assign attributes."""
        if args:
            ls = []
            for arg in args:
                ls.append(arg)
            n = len(ls)
            if n == 4:
                self.id = ls[0]
                self.size = ls[1]
                self.x = ls[2]
                self.y = ls[3]
            elif n == 3:
                self.id = ls[0]
                self.size = ls[1]
                self.x = ls[2]
            elif n == 2:
                self.id = ls[0]
                self.size = ls[1]
            elif n == 1:
                self.id = ls[0]
        else:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                if key == 'size':
                    self.size = value
                if key == "x":
                    self.x = value
                if key == 'y':
                    self.y = value
