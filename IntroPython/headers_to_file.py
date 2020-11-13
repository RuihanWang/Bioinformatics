#!/usr/bin/env python
import re
dmel_genome_path = '/scratch/Drosophila/dmel-all-chromosome-r6.17.fasta'

line_count = 0;
seq = ''
# Open the genome file
with open(dmel_genome_path) as dmel_genome:
        # Iterate over the lines in the file
    for line in dmel_genome:
        if re.match('^>', line):
            line_count +=1
        # If the line count is less than 50, print the line
            if line_count <= 50:
                seq += line         
with open("dmel_headers.txt", 'w') as out:
     out.write(seq)
