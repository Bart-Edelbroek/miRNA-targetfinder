#!/usr/bin/env python
# file: miRbinder.py
import sys, subprocess
from miRbinder.genetoseq import Gene2seq
from miRbinder.outputanalysis import Analysis
from os import system

genelist = sys.argv[1]
query_in = sys.argv[2]
combinedplot_steps = 100
g2seq = Gene2seq(genelist)
sequencelist = g2seq.run()

geneseq = open("genesequences.fasta","w+")
geneseq.write(sequencelist)

subprocess.run(["IntaRNA", "-t", "genesequences.fasta", "-q", query_in,
	"--seedBP=6", "--seedNoGU", "--seedMinPu=0.001", "--outMinPu=0.001",
	"--outNoLP", "--out=tMinE:MYPROFILEFILE.csv"])

analysis = Analysis(genelist, combinedplot_steps)
analysis.run()

subprocess.run(["rm ./MYPROFILEFILE-t*q1.csv"], shell = True)