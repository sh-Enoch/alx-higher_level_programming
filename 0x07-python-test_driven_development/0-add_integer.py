#!/usr/bin/python3
def add_integer(a, b=98):
    """Add two integers a and b.

    Args:
       a: First integer.
       b: Second integer.

    Returns:
       int: Addition of a and b.

    Raises:
       TypeError: if a or b are not integers or floats.
       """
    if not isinstance(a , (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
