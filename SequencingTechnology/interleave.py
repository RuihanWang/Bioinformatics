#!/usr/bin/env python3
from Bio import SeqIO
import itertools
# The first parameter to SeqIO.parse is the file location
# The second parameter is the file type
leftReads = SeqIO.parse("/scratch/AiptasiaMiSeq/fastq/Aip02.R1.fastq", "fastq")
rightReads = SeqIO.parse("/scratch/AiptasiaMiSeq/fastq/Aip02.R2.fastq", "fastq")
# Iterate
total = []
for left,right in zip(leftReads,rightReads):
    print(left)
    total.append(left)
    print(right)
    total.append(right)
SeqIO.write(total, "Interleaved.fasta","fasta")

#    SeqIO.write(left, "Interleaved.fastq","fastq")
#    SeqIO.write(right, "Interleaved.fastq","fastq")


