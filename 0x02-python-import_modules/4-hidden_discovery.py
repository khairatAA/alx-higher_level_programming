#!/usr/bin/python3.8
import hidden_4

if __name__ == "__main__":
    hidden_names = dir(hidden_4)
    for name in hidden_names:
        if name[:2] != "__":
            print("{}".format(name))
