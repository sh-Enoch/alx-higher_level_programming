#!/usr/bin/python3
"""class square that defines a aquare
   instantiation
   size of type int
   size must be > 0
   public instance method returns square area"""


class Square:
    """initialization """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        a = self.__size * self.__size
        return a
