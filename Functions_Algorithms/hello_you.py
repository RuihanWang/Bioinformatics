#!/usr/bin/env python3
# hello_you.py

import sys
def hello_name(s=""):
    if s:
        return "Hello, {}!".format(s)
    else:
        return "Hello, you!"
if __name__ == "__main__" :
    arg_count = len(sys.argv)-1
    if arg_count > 0:

        print(hello_name(sys.argv[1]))
    else:
        print(hello_name())

