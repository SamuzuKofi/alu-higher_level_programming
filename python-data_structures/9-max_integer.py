#!/usr/bin/python3


def max_integer(my_list=[]):
    tmp = 0
    if len(my_list) == 0:
        return None
    for i in my_list:
        if my_list[i] > tmp:
            tmp = my_list[i]
    print("Max: {}".format(tmp))
