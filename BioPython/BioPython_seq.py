#!/usr/bin/env python
# BioPython_seq.py

from Bio.Seq import Seq
from Bio.Alphabet import generic_dna
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
my_seq = SeqRecord(Seq("AAAATGGGGGGGGGGCCCCGTT",generic_dna), id = "#12345", description = "example 1")
SeqIO.write(my_seq,"BioPython_seq.gb","gb")
