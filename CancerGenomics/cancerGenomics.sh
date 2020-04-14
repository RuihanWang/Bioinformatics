#!/usr/bin/env bash
R -e "rmarkdown::render('cancerGenomics.Rmd', output_format='all')"
