#!/usr/bin/python3
"""Class student."""


class Student:
    """Define a class student."""
    def __init__(self, first_name, last_name, age):
        """Initialize class student

        Args:
            first_name(string): first name
            last_name (string): last name
            age(int): age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve a dictionary representation of a student instance."""
        if attrs:
            return {attr: getattr(self, attr) for attr in attrs}
        else:
            return self.__dict__.copy()
