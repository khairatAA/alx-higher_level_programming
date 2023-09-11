#!/usr/bin/python3
"""1-my_list module"""


class MyList(list):
    """a class MyList that inherits list"""
    def print_sorted(self):
        """prints the list, but sorted (ascending sort)"""
        self.sort()
        print(self)
