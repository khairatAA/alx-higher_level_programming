#!/usr/bin/python3
"""100-my_int module"""


class MyInt(int):
    """class MyInt that inherits from int
    """
    def __eq__(self, other):
        """Special method __eq__"""
        if isinstance(other, MyInt):
            return False
        return super().__eq__(other)

    def __ne__(self, other):
        """Special method __ne__"""
        if isinstance(other, MyInt):
            return True
        return super().__ne__(other)
