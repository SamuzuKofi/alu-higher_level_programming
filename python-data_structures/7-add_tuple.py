#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    a1, a2 = (tuple_a + (0, 0))[:2]
    b1, b2 = (tuple_b + (0, 0))[:2]

    new_tuple = (a1 + b1, a2 + b2)
    return(new_tuple)
