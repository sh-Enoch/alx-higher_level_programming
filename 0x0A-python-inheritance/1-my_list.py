#!/usr/bin/python3
"""Class MyList that inherits from list."""


class MyList(list):
    """inherits from class list."""

    def print_sorted(self):
        """Sort list in ascending."""
        copy_list = self[:]
        copy_list.sort()
        print(copy_list)
