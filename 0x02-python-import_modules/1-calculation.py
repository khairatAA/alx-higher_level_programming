#!/usr/bin/python3
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    a = 10
    b = 5
    total = add(a, b)
    print("{} + {} = {}".format(a, b, total))
    total = sub(a, b)
    print("{} - {} = {}".format(a, b, total))
    total = mul(a, b)
    print("{} * {} = {}".format(a, b, total))
    total = div(a, b)
    print("{} / {} = {}".format(a, b, total))
