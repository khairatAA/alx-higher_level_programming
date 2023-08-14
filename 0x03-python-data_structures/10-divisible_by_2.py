#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    list2 = []
    for i in range(0, len(my_list)):
        if my_list[i] % 2 == 0:
            list2 = list2 + [True]
        else:
            list2 = list2 + [False]
    return list2
