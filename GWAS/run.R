#!/usr/bin/env Rscript
# run.R
d <- read.table("rec_snp1.raw" , header=T)
summary(glm(PHENOTYPE-1 ~ rs2222162_1, data=d, family="binomial"))
