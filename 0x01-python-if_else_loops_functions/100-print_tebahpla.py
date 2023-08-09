#!/usr/bin/python3
for i in range(122, 96, -1):
    if i % 2 == 0:
        l_case = chr(i)
    else:
        l_case = chr(i - 32)
    print("{}".format(l_case), end="")
