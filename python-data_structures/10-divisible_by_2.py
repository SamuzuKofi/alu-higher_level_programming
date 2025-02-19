x#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    for i in my_list:
        print("{:d} {:s} divisible by 2".format(i, "is" if i % 2 == 0 else "is not"))
