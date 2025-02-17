#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argv = sys.argv[1:]
    sum = 0

    for i, arg in enumerate(argv, 1):
        arg = int(arg)
        sum = arg
        sum = sum + arg
    print(sum)
