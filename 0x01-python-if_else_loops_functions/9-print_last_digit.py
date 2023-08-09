#!/usr/bin/python3
def print_last_digit(number):
    number = abs(number)
    number = number % 10
    last_digit = number % 10
    print("{}".format(number), end="")
    return last_digit
