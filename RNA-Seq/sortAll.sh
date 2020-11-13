#!/usr/bin/env bash
# sortAll.sh
# Initialize variable to contain the directory of un-trimmed fastq files 
fastqPath="/scratch/AiptasiaMiSeq/fastq/"
# Initialize variable to contain the suffix for the left reads
leftSuffix=".R1.fastq"
rightSuffix=".R2.fastq"
sam="sam/"
bam="bam/"
pairedOutPath="Paired/"
unpairedOutPath="Unpaired/"
# Create the output directories
mkdir -p $bam
# Loop through all the left-read fastq files in $fastqPath
function sortAll {
    for leftInFile in $fastqPath*$leftSuffix
    do
# Remove the path from the filename and assign to pathRemoved
        pathRemoved="${leftInFile/$fastqPath/}"
# Remove the left-read suffix from $pathRemoved and assign to suffixRemoved
        sampleName="${pathRemoved/$leftSuffix/}"
# Print $sampleName to see what it contains after removing the path
        samtools sort $sam$sampleName.sam -o $bam$sampleName.sorted.bam \
        1>$bam$sampleName.sort.log 2>$bam$sampleName.sort.err
    done            
}
sortAll 1>sortAll.log 2>sortAll.err &
