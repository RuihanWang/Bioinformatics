#!/usr/bin/env python
# hamming.py

import sys
def hamming(str1,str2):
    ham = 0
    if len(str1) != len(str2):
        raise Exception("Wrong Parameter, must be same length")
    else:
        for i in range(0,len(str1)):
            if str1[i]==str2[i]:
                continue;
            else:
                ham += 1
    return ham

if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise Exception("Wrong parameter, please check")
    else:
        print(sys.argv[1])
        print(sys.argv[2])
        print(hamming(str(sys.argv[1]),str(sys.argv[2])))
