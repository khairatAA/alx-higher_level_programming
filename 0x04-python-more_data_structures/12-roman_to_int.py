#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None:
        return 0
    elif type(roman_string) is not str:
        return 0
    roman = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    total = 0
    prev_val = 0
    for char in reversed(roman_string):
        value = roman[char]
        if (value >= prev_val):
            total += value
        else:
            total -= value
        prev_val = value
    return total
