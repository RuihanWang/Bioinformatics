#!/usr/bin/env python3
#basic_functions.py

def multiply(x,y):
    return x*y

def hello_name (a=""):
    if a:
        return "Hello, {}!".format(a)
    else:
        return "Hello, you!"

def less_than_ten (a):
    b = []
    for ele in a:
        if ele < 10:
            b.append(ele)
        else:
            continue;
    return b

