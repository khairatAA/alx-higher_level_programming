#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <a> <operator> <b>".format(sys.argv[0]))
        sys.exit(1)

    operator = sys.argv[2]
    a = int(sys.argv[1])
    b = int(sys.argv[3])

    if operator == '+':
        total = add(a, b)
    elif operator == '-':
        total = sub(a, b)
    elif operator == '*':
        total = mul(a, b)
    elif operator == '/':
        total = div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    print("{} {} {} = {}".format(a, operator, b, total))
