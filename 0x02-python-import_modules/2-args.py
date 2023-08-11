#!/usr/bin/python3
import sys

if __name__ == "__main__":
    len_of_argv = len(sys.argv) - 1
    if len_of_argv == 1:
        print("{} argument:".format(len_of_argv))
    elif len_of_argv > 1:
        print("{} arguments:".format(len_of_argv))
    else:
        print("{} arguments.".format(len_of_argv))

    count = 0
    if len_of_argv >= 1:
        for i in range(1, len(sys.argv)):
            count = count + 1
            print("{}: {}".format(count, sys.argv[i]))
