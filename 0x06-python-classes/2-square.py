#!/usr/bin/python3
""" class square that defines a square by:
    private instance attribute size
    instantiation
    size must be int or raise TypError
    size must be > 0 else raise ValueError """


class Square:
    """ Square class """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise valueError("size must be >= 0")
        else:
            self.__size = size
