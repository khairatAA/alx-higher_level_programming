#!/usr/bin/python3.8
import marshal

if __name__ == "__main__":
    with open("/mnt/c/Users/HP/Downloads/hidden_4.pyc", "rb") as file:
        code = marshal.load(file)
    names = code.co_names
    sorted_names = sorted(name for name in names if not name.startswith("__"))
    for name in sorted_names:
        print("{}".format(name))
