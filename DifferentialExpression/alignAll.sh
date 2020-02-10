#!/usr/bin/env bash
# alignAll.sh
outDir="quant/"
fastqPath="/scratch/SampleDataFiles/Paired/"
leftSuffix=".R1.paired.fastq"
rightSuffix=".R2.paired.fastq"
outDir='quant/'
pathRemoved="${leftInFile/$fastqPath/}"
suffixRemoved="${pathRemoved/$leftSuffix/}"
for sample in $fastqPath*$leftSuffix
do
    pathRemoved="${sample/$fastqPath/}"
    echo $pathRemoved
    suffixRemoved="${sample/$leftSuffix/}"
    echo $suffixRemoved
    salmon quant -l IU \
        -1 $suffixRemoved.R1.paired.fastq \
        -2 $suffixRemoved.R2.paired.fastq \
        -i AipIndex \
        --validateMappings \
        -o $outDir${suffixRemoved/$fastqPath/}


   
    
done

align 1>align.log 2>align.err &



