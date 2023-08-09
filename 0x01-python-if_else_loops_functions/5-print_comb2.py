#!/usr/bin/python3
output = ""
for i in range(0, 100):
    if i < 10:
        output = output + "0" + str(i) + ", "
    elif i < 99:
        output = output + str(i) + ", "
    else:
        output = output + str(i)
print("{}".format(output))
