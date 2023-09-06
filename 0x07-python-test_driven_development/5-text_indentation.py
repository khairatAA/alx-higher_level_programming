#!/usr/bin/python3
"""
prints a text with 2 new lines after each
of these characters: ., ? and :.
5-text_indentation.py
"""


def text_indentation(text):
    """prints a text with 2 new lines after
    each of these characters: ., ? and :.

    Args:
        character(list) : containing the characters.
        count(int): keeps track of the number of loops
        lines(list): list containing the splitted string

    Raises:
        TypeError: text must be a string
        ValueError: input must not be an empty string
    """
    if type(text) is not str or text is None:
        raise TypeError("text must be a string")
    if not text.strip():
        raise ValueError("input must not be an empty string")

    characters = ['.', '?', ':']

    for char in characters:
        text = text.replace(char, char + '\n')

    lines = text.split('\n')

    for i, line in enumerate(lines):
        stripped_line = line.strip()

        if stripped_line:
            print(stripped_line)
            if i < len(lines) - 1:
                print()
