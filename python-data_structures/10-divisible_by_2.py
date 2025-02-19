#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    if my_list is None:
        return []
    return [num % 2 == 0 for num in my_list]
