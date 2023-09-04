#!/usr/bin/python3
"""
5-text_indentation.py
"""


def text_indentation(text):
    if type(text) is not str or text is None:
        raise TypeError("text must be a string")

    characters = ['.', '?', ':']

    for char in characters:
            text = text.replace(char + ' ', char + '\n\n')

    lines = text.split('\n')

    for line in lines:
        stripped_line = line.strip()
        if stripped_line:
            print(stripped_line)
