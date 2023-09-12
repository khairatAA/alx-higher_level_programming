#!/usr/bin/python3
"""100-my_int module"""


class MyInt(int):
    """class MyInt that inherits from int
        Args:
            value(int): the value passed by the user
    """
    def __eq__(self, other):
        """Special method __eq__"""
        if isinstance(other, MyInt):
            return self.value != self.other
        return True

    def __ne__(self, other):
        """Special method __ne__"""
        if isinstance(other, MyInt):
            return self.value == self.other
        return False
