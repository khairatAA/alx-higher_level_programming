#!/usr/bin/python3
"""
This is the "0-add_integer" module.
"""

def add_integer(a, b=98):
    """This function adds the sum of two number which
    are of types float or int.
    
    Args:
        result: holds the sum of a and b.
    """
    if (
            (type(a) is not int) and (type(a) is not float)
            ):
            raise TypeError("a must be an integer")

    if  a is None:
        raise TypeError("a must be an integer")

    if (
            (type(b) is not int) and (type(b) is not float)
            ):
            raise TypeError("b must be an integer")

    result = int(a) + int(b)
    return int(result)
