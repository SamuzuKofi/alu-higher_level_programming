#!/usr/bin/python3
def add(a,b):
    return a + b
a = 1
b = 2

if __name__ == "__main__":  # Ensures code runs only when executed directly
    print("{} + {} = {}".format(a, b, add(a, b)))
