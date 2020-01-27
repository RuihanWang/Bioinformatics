#!/usr/bin/env python
# BioPython)seqio.py


from Bio import SeqIO
import sys
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
def read_seq(in_file, out_file):
    for record in SeqIO.parse(in_file, "fasta"):
        print(record.id)
        print(record.seq)
        
    
        new_record = record.seq.reverse_complement()
        
        SeqIO.write(SeqRecord(new_record,id = record.id),out_file,"fasta")



if __name__ == "__main__":

    if len(sys.argv) != 3:
        raise Exception("Need file name right")
    else:
       
        read_seq(sys.argv[1],sys.argv[2])





