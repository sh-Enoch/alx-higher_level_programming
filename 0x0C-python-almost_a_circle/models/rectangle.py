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
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width > 0:
            self.__width = width
        else:
            raise ValueError("width must be > 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height > 0:
            self.__height = height
        else:
            raise ValueError("height must be > 0")
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x >= 0:
            self.__x = x
        else:
            raise ValueError("x must be >= 0")
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y >= 0:
            self.__y = y
        else:
            raise ValueError("y must be >= 0")

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
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value > 0:
            self.__width = value
        else:
            raise ValueError("width must be > 0")

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
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value > 0:
            self.__height = value
        else:
            raise ValueError("height must be > 0")

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
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value >= 0:
            self.__x = value
        else:
            raise ValueError("x must be >= 0")

    @property
    def y(self):
        """Get y."""
        return self.__y

    @y.setter
    def y(self, value):
        """Set y."""
        if not isinstance(value, int):
            raise TypeError("y must be an integer""")
        if value >= 0:
            self.__y = value
        else:
            raise ValueError("y must be >= 0")

    def area(self):
        """Return the area value of rectangle."""
        area = self.__width * self.__height
        return area

    def display(self):
        """Print in stdout the Rectangle."""
        for i in range(self.__height):
            for j in range(self.__width):
                print('#', end='')
            print()

    def __str__(self):
        """Return new string."""
        t = type(self).__name__
        h = self.__height
        w = self.__width
        i = self.id
        x = self.__x
        y = self.__y
        return "[{}] ({}) {}/{} - {}/{}".format(t, i, x, y, w, h)

    def update(self, *args, **kwargs):
        """Assign arguments to each attribute."""
        if args:
            ls = []
            for arg in args:
                ls.append(arg)
            if len(ls) == 5:
                self.id = ls[0]
                self.__width = ls[1]
                self.__height = ls[2]
                self.__x = ls[3]
                self.__y = ls[4]
            elif len(ls) == 4:
                self.id = ls[0]
                self.__width = ls[1]
                self.__height = ls[2]
                self.__x = ls[3]
            elif len(ls) == 3:
                self.id = ls[0]
                self.__width = ls[1]
                self.__height = ls[2]
            elif len(ls) == 2:
                self.id = ls[0]
                self.__width = ls[1]
            else:
                self.id = ls[0]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "width":
                    self.__width = value
                elif key == "height":
                    self.__height = value
                elif key == "x":
                    self.__x = value
                elif key == "y":
                    self.__y = value

    def to_dictionary(self):
        """Return dictionary representation of a rectangle."""
        return {"x": self.x, "y": self.y, "id": self.id, "height": self.height,
                "width": self.width}
