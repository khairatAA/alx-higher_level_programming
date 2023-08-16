#!/usr/bin/python3
def number_keys(a_dictionary):
    num = 0
    for i in a_dictionary:
        num = num + 1
        if isinstance(a_dictionary[i], dict):
            num = num + number_keys(a_dictionary[i])
    return num
