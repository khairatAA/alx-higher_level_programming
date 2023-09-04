#!/usr/bin/python3
"""
Module to find the max integer in a list
"""


def max_integer(input_list=[]):
    """Function to find and return the max integer in a list of integers
        If the list is empty, the function returns None
    """
    if not isinstance(input_list, list):
        raise TypeError("Input must be a list of integers")

    if len(input_list) == 0:
        return None

    for i in input_list:
        if type(i) is not int:
            raise TypeError("Input must be a list of integers")

        if i is True or i is False:
            raise TypeError("Input must be a list of integers")

    result = input_list[0]

    for i in input_list:
        if i > result:
            result = i

    return result
