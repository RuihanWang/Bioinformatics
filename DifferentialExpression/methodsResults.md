## Methods

There are mainly two steps to do a differential express analysis. First
we need to estimate relative abundance with salmon
(<span class="citeproc-not-found" data-reference-id="Raithen">**???**</span>).
Second we will apply statistical models to test the differential
expression between groups with tximport.(Soneson, Love, and Robinson
2015) Then use DESeq2(Caballero-Solares et al. 2018) to test the
results. 21 22 23 \`\`\`{r, layout=“l-body-outset”,include=FALSE} 24
library(knitr) 25 deannotated \<- read.csv(“deAnnotated.csv”, header =
TRUE) 26 kable(deannotated)

<div id="refs" class="references hanging-indent">

<div id="ref-Albert">

Caballero-Solares, Albert, Xi Xue, Christopher C. Parrish, Maryam
Beheshti Foroutani, Richard G. Taylor, and Matthew L. Rise. 2018.
“Changes in the Liver Transcriptome of Farmed Atlantic Salmon (Salmo
Salar) Fed Experimental Diets Based on Terrestrial Alternatives to Fish
Meal and Fish Oil.” *BMC Genomics* 19 (1): 796–96.
<https://doi.org/10.1186/s12864-018-5188-6>.

</div>

<div id="ref-Love">

Soneson, Charlotte, Michael I. Love, and Mark D. Robinson. 2015.
“Differential Analyses for RNA-Seq: Transcript-Level Estimates Improve
Gene-Level Inferences.” *F1000Research* 4 (December): 1521–1.
<https://www.ncbi.nlm.nih.gov/pubmed/26925227>.

</div>

</div>
