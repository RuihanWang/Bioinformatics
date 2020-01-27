#!/usr/bin/env python
# BioPython_genbank.py

from Bio import Entrez
from Bio import SeqIO

Entrez.email = "wang.ruih@husky.neu.edu"
handle = Entrez.efetch(db="nucleotide", rettype="gb", retmode="text", id="51505")
seq_record = SeqIO.read(handle, "gb")
def pt(seq_record):
    print(seq_record.seq)
    for feature in seq_record.features:


        print("type {} , location {} , strand {}".format( feature.type, feature.location, feature.strand))
pt(seq_record)


handle = Entrez.efetch(db="nucleotide", rettype="gb", retmode="text", id="J01673.1")
seq_record = SeqIO.read(handle, "gb")
pt(seq_record)
