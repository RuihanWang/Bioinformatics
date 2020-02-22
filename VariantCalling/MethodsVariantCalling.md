Methods
-------

### 1

get the genome info from from
<a href="ftp://ftp.ebi.ac.uk/pub/databases/gencode/Gencode_human/release_27/GRCh38.primary_assembly.genome.fa.gz" class="uri">ftp://ftp.ebi.ac.uk/pub/databases/gencode/Gencode_human/release_27/GRCh38.primary_assembly.genome.fa.gz</a>
and then etrieve reads in SRA (script getGenome.sh and getReads.sh)
\#\#\# 2 Using Trimmomatict do Quality trim (script
trimReads.sh)(Bolger, Lohse, and Usadel 2014) \#\#\# 3 Index the genome
for use by BWA (indexGenome.sh)(Abuín et al. 2016) \#\#\# 4 Align the
reads using bwa mem (alignReads.sh)(Zhang, Liu, and Dong 2019) \#\#\# 5
Using samtool to sort the file (script sort.sh)(Ramirez-Gonzalez et al.
2012) \#\#\# 6 Using samtool to index reads (script indexReads.sh)(Li et
al. 2009) \#\#\# 7 Using DeepVariant to do a analysis (script
runDeepVariant.sh) to generate a VCF file(Supernat et al. 2018)

Referenece
----------

Abuín, José M., Juan C. Pichel, Tomás F. Pena, and Jorge Amigo. 2016.
“SparkBWA: Speeding up the Alignment of High-Throughput DNA Sequencing
Data.” *PloS One* 11 (5): e0155461–e0155461.
<https://doi.org/10.1371/journal.pone.0155461>.

Bolger, Anthony M., Marc Lohse, and Bjoern Usadel. 2014. “Trimmomatic: A
Flexible Trimmer for Illumina Sequence Data.” *Bioinformatics (Oxford,
England)* 30 (15): 2114–20.
<https://doi.org/10.1093/bioinformatics/btu170>.

Li, Heng, Bob Handsaker, Alec Wysoker, Tim Fennell, Jue Ruan, Nils
Homer, Gabor Marth, Goncalo Abecasis, Richard Durbin, and 1000 Genome
Project Data Processing Subgroup. 2009. “The Sequence Alignment/Map
Format and SAMtools.” *Bioinformatics (Oxford, England)* 25 (16):
2078–9. <https://doi.org/10.1093/bioinformatics/btp352>.

Ramirez-Gonzalez, Ricardo H., Raoul Bonnal, Mario Caccamo, and Daniel
Maclean. 2012. “Bio-Samtools: Ruby Bindings for SAMtools, a Library for
Accessing BAM Files Containing High-Throughput Sequence Alignments.”
*Source Code for Biology and Medicine* 7 (1): 6–6.
<https://doi.org/10.1186/1751-0473-7-6>.

Supernat, Anna, Oskar Valdimar Vidarsson, Vidar M. Steen, and Tomasz
Stokowy. 2018. “Comparison of Three Variant Callers for Human Whole
Genome Sequencing.” *Scientific Reports* 8 (1): 17851–1.
<https://doi.org/10.1038/s41598-018-36177-7>.

Zhang, Lingqi, Cheng Liu, and Shoubin Dong. 2019. “PipeMEM: A Framework
to Speed up BWA-MEM in Spark with Low Overhead.” *Genes* 10 (11): 886.
<https://doi.org/10.3390/genes10110886>.
