#!/usr/bin/env python3
#sliding_window_fasta.py

import sys
import re
from Bio import SeqIO
import itertools

def get_kmers(k,file_name):
    reads = SeqIO.parse(file_name, "fasta")
    sequences = ""
    for fasta in reads:
        seq = str(fasta.seq)
        sequences += seq
    kmers = {}
    end = len(sequences) - k + 1
    for start in range(0,end):
        gc = 0
        kmer = sequences[start:start+k]
        for l in kmer:
            #print(l)
            if l in ['G','C']:
                gc+=1
               # print(gc)
        gc = gc/k
        #print(gc)
        kmers[kmer] = gc
    return kmers


if __name__ == "__main__":
    arg_count = len(sys.argv)
    if arg_count != 3:
        raise Exception("Enter right parameter")
    else:
        print(">NC_001477.1 Dengue virus 1, complete genome")
        kmers = get_kmers(int(sys.argv[1]),sys.argv[2])
        for kmer,gc in kmers.items():
           
            print("{}\t{:.2f}".format(kmer,float(gc)))

