#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_key = sorted(a_dictionary.keys())
    for i in sorted_key:
        value = a_dictionary[i]
        print("{}: {}".format(i, value))
