Reads were quality trimmed using Trimmonatic which is a NGS tools that is flexible and high performed. It could correct handling paired-end data to remove adapters[1]. 
Reads were aligned with GSNAP. It is a enhancement to speed,accuracy and functionality. Improvements to the algorithms have included a greedy match-and-extend algorithm using suffix arrays, segment chaining using genomic hash tables, diagonalization using segmental hash tables, and nucleotide-level dynamic programming procedures that use SIMD instructions and eliminate the need for F-loop calculations. Enhancements to the functionality of the programs include standardization of indel positions, handling of ambiguous splicing, clipping and merging of overlapping paired-end reads, and alignments to circular chromosomes and alternate scaffolds[2]
Alignments were sorted and indexed with SAMtools which is widely-used genomics application for post-processing high-throughput sequence alignment data[3].




[1]Anthony M. Bolger, Marc Lohse, Bjoern Usadel, Trimmomatic: a flexible trimmer for Illumina sequence data, Bioinformatics, Volume 30, Issue 15, 1 August 2014, Pages 2114–2120, https://doi.org/10.1093/bioinformatics/btu170
[2]Investigators at Genentech, Inc. Have Reported New Data on Molecular Biology (GMAP and GSNAP for Genomic Sequence Alignment: Enhancements to Speed, Accuracy, and Functionality)." Life Science Weekly, 23 Aug. 2016, p. 755. Gale Academic Onefile, https://link-gale-com.ezproxy.neu.edu/apps/doc/A461195450/AONE?u=mlin_b_northest&sid=AONE&xid=c791cdce. Accessed 27 Oct. 2019.
[3]Weeks, N.T. & Luecke, G.R. Cluster Comput (2017) 20: 1869. https://doi-org.ezproxy.neu.edu/10.1007/s10586-017-0874-8
