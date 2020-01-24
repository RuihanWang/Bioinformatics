#!/usr/bin/env python
# fibonacci.py

import sys

def population(n,k):
    n = int(n)
    k = int(k)
    
    p = {}
    p[1] = 1
    p[2] = 1
    for i in range(3,n+1):
        p[i] = p[i-1] +k*p[i-2]
    return p[n]



if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise Exception("Wrong Parameter")
    else:
        print(population(sys.argv[1],sys.argv[2]))
        
