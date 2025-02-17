#!/usr/bin/python3
import sys

if __name__ == "__main__":
    acc_arg = sys.argv[1:]
    arg_len = len(acc_arg)

    print("{} arguments{}{}".format(arg_len, "" if arg_len == 1 else "s", ":" if arg_len > 0 else "."))

    for i, arg in enumerate(acc_arg, 1):
        print("{}: {}".format(i, arg))
