#!/usr/bin/env python3
# one_argument_required.py

import sys

if __name__ == "__main__":
    arg_count = len(sys.argv) - 1
    if arg_count != 1:
        raise Exception("This script requires exactly 1 argument, but {} were given".format(arg_count))

    print("The script ran successfully!")
