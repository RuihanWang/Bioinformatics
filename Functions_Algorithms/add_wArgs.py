#!/usr/bin/env python3
# add_wArgs.py

import sys

def add(x, y):
    """
    Adds two numbers, x and y.
    """
    return x+y

if __name__ == "__main__":

    # First: Check to make sure there are at least two arguments
    arg_count = len(sys.argv) - 1
    if arg_count < 2:
        raise Exception("This script requires at least 2 arguments")

    # Now, get the numbers from the argument list
    # Note: arguements are passed as strings, so need to be converted to int
    x = int(sys.argv[1])
    y = int(sys.argv[2])

    result = add(x, y)
    print("{} + {} = {}".format(x, y, result))
