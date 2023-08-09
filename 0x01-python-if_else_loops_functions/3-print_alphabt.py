#!/usr/bin/python3
output = ""
for i in range(97, 123):
    if i != 113 and i != 101:
        output = output + chr(i)
print("{}".format(output), end="")
