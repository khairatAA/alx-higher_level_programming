#!/usr/bin/python3
"""4-inherits_from module"""


def inherits_from(obj, a_class):
    """Returns True if the object is an instance of a class
    that inherited (directly or indirectly) frm the specified
    class ; otherwise False
    """

    if isinstance(a_class) is obj:
        return True

    return False
