#!/usr/bin/env python
# file: miRbinder.py
import sys, subprocess
from miRbinder.genetoseq import Gene2seq

genelist = sys.argv[1]
query_in = sys.argv[2]
g2seq = Gene2seq(genelist)
sequencelist = g2seq.run()

geneseq = open("genesequences.fasta","w+")
geneseq.write(sequencelist)

subprocess.run(["IntaRNA", "-t", "genesequences.fasta", "-q", query_in,
	"--seedBP=6", "--seedNoGU", "--seedMinPu=0.001", "--outMinPu=0.001",
	"--outNoLP"])