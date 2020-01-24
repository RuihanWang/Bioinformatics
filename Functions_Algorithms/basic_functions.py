#!/usr/bin/env python3


def multiply(x,y):
    return x*y

def hello_name (a):
    if a:
        print("Hello,",a,"!")
    else:
        print("Hello,","you!")

def less_than_ten (a):
    b = []
    for ele in a:
        if ele < 10:
            b.append(ele)
        else:
            continue;
    return b
print(less_than_ten([1, 5, 81, 10, 8, 2, 102]))

