#!/usr/bin/env python
#! translate_APOE.py


from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO


seq = SeqIO.parse("APOE_refseq_transcript.fasta","fasta")
se = []
for s in seq:
    s.seq = s.seq.translate()
    se.append(s)

SeqIO.write(se,"apoe_aa.fasta","fasta")

