#!/usr/bin/env Rscript
# de.R
library(tximport)
library(readr)
library(DESeq2)
tx2gene <- read.csv("tx2gene.csv")
head(tx2gene)
samples <- read.csv("/scratch/SampleDataFiles/Samples.csv", header=TRUE)
head(samples)
files <- file.path("quant", samples$Sample, "quant.sf")
txi <- tximport(files, type="salmon", tx2gene=tx2gene)
dds <- DESeqDataSetFromTximport(txi, colData = samples, 
                                                                design = ~ Menthol + Vibrio)
dds$Vibrio <- relevel(dds$Vibrio, ref = "Control")
dds$Menthol <- relevel(dds$Menthol, ref = "Control")
keep <- rowSums(counts(dds)) >= 10
dds <- dds[keep,]
dds <- DESeq(dds)
padj <- .05
minLog2FoldChange <- .5
dfAll <- data.frame()
# Get all DE results except Intercept, and "flatten" into a single file.
for (result in resultsNames(dds)){
        if(result != 'Intercept'){
                    res <- results(dds, alpha=.05, name=result)
        dfRes <- as.data.frame(res)
                dfRes <- subset(subset(dfRes, select=c(log2FoldChange, padj)))
                dfRes$Factor <- result
                        dfAll <- rbind(dfAll, dfRes)
                    }
}


dim(dfAll)
head(dfAll)
head(tx2gene)
deAnnotated = merge(dfAll,tx2gene, by.x=0,by.y="ko")
head(deAnnotated)
write.csv(deAnnotated, file="deAnnotated.csv")

