## Methods

The two main steps in performing differential expression analysis are to
estimate the relative abundance of transcripts, and to apply statistical
models to test for differential expression between treatment groups.
Estimating relative abundance is basically determining how many NGS
reads match a given gene within a genome. In this module you’ll use
Salmon
(<span class="citeproc-not-found" data-reference-id="Patro">**???**</span>)
to estimate relative abundance, tximport
(<span class="citeproc-not-found" data-reference-id="Soneson">**???**</span>)
to import the Salmon abundance estimates, and DESeq2
(<span class="citeproc-not-found" data-reference-id="Love">**???**</span>)
to perform statistical tests to identify differentially expressed genes.

``` r
library(knitr)
deannotated <- read.csv("deAnnotated.csv", header = TRUE)
kable(head(deannotated))
```

| X | Row.names | log2FoldChange |      padj | Factor                        | trans                       |
| -: | :-------- | -------------: | --------: | :---------------------------- | :-------------------------- |
| 1 | ko:K00024 |    \-0.8911610 | 0.9452229 | Menthol\_Menthol\_vs\_Control | TRINITY\_DN9267\_c0\_g1\_i2 |
| 2 | ko:K00024 |    \-0.8911610 | 0.9452229 | Menthol\_Menthol\_vs\_Control | TRINITY\_DN9446\_c0\_g1\_i1 |
| 3 | ko:K00031 |    \-0.6698141 | 0.9452229 | Menthol\_Menthol\_vs\_Control | TRINITY\_DN9440\_c0\_g1\_i1 |
| 4 | ko:K00128 |    \-0.2299678 | 0.9452229 | Menthol\_Menthol\_vs\_Control | TRINITY\_DN9333\_c0\_g1\_i1 |
| 5 | ko:K00134 |      1.5188727 | 0.7036797 | Menthol\_Menthol\_vs\_Control | TRINITY\_DN9495\_c0\_g1\_i2 |
| 6 | ko:K00134 |      1.5188727 | 0.7036797 | Menthol\_Menthol\_vs\_Control | TRINITY\_DN9495\_c0\_g1\_i1 |
