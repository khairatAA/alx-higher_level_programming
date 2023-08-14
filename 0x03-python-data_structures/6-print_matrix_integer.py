#!/usr/bin/python
def print_matrix_integer(matrix=[[]]):
    length = range(len(matrix))
   # nested = range(len(matrix))
    matrix = [[int(i) for i in length] for i in length]
    print("{}".format(matrix))
