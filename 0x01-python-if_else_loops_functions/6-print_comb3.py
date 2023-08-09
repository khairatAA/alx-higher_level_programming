#!/usr/bin/python3
output = ""
for i in range(0, 10):
    for j in range(i + 1, 10):
        output = output + f"{i}{j}, "
output = output[:-2]
print("{}".format(output))
