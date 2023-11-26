#!/usr/bin/python3
"""Class MyList that inherits from list."""


class MyList(list):
    """inherits from class list."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def print_sorted(self):
        """Sort list in ascending."""
        print(sorted(self))
