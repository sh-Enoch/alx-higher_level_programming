#!/usr/bin/python3
"""Print name."""


def say_my_name(first_name, last_name=""):
    """Print first name and last name.

    Args:
        first_name (string): first name to print
	last_name (string): last name

    Return:
        My name is <first name> <last name>
    """
    if first_name == None or last_name == None:
        raise TypeError('please enter a name')
    elif type(first_name) != type('enoch'):
        raise TypeError('first_name must be a string')
    elif type(last_name) != type('enoch'):
        raise TypeError('last_name must be a string')
    else:
        print("My name is {} {}".format(first_name, last_name))
