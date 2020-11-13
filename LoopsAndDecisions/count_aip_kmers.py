#!/usr/bin/env python
# count_kmers.py

import re
import os
read_sample = open('/scratch/SampleDataFiles/Sample.R1.fastq', 'r')

line = ' '
kmer_dictionary = {}
kmer_length = 6
# While line is not empty
while line:
    line = read_sample.readline()
    line = line.rstrip(os.linesep)
    if re.match('^[ATGCN]+$', line):
        stop = len(line) - kmer_length + 1
        for start in range(0, stop):
            kmer = line[start:start + kmer_length]
            kmer_dictionary[kmer] = kmer_dictionary.get(kmer, 0) + 1



aip_kmers = open("aip_kmers.txt",'w')
for kmer, count in kmer_dictionary.items():
    aip_kmers.write("{0}\t{1}".format(kmer, count) + "\n")





read_sample.close()




