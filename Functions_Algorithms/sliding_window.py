#!/usr/bin/env python3
# sliding_window.py

import sys
import re

def sliding_window(k,string):
    kmers = []
    end = len(string) - k + 1
    for start in range(0,end):
        gc = 0
        kmer = string[start:start+k]
        for l in kmer:
            #print(l)
            if l in ['G','C']:
                gc+=1
               # print(gc)
        gc = gc/k
        #print(gc)
        kmers.append(kmer)
    return kmers
def gc_content(string):
    gc = 0
    for l in string:
        if l in ['G','C']:
            gc+=1
    gc = gc/len(string)
    return gc
if __name__ == "__main__":
    arg_count = len(sys.argv)
    if arg_count != 3:
        raise Exception("Enter right parameter")
    else:

        kmers = sliding_window(int(sys.argv[1]),sys.argv[2])
        for kmer in kmers:
            print(kmer," {}".format(gc_content(kmer)))

