#!/usr/bin/python3
import sys

if __name__ == "__main__":
    len_of_argv = len(sys.argv) - 1
    if len_of_argv >= 1:
        count = 0
        for i in range(1, len(sys.argv)):
            count = count + int(sys.argv[i])
        print("{}".format(count))
    else:
        print(0)
