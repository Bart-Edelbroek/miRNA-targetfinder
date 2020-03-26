#!/usr/bin/env python
# file: genetoseq.py

import re, sys, pybedtools

#read in gene_id's 
genelist = open(sys.argv[1]).read().split('\n')

#read in original .bed file

oribed = open('./reference/D_discoideum_PASAua.bed').readlines()

#subset of .bed for genelist
newbed = ""

for line in oribed:
	for gene in genelist:
		if re.search(str(gene), line): 
			newbed+=line 

print(newbed)

bt = pybedtools.BedTool(newbed, from_string=True)
fastaref = './reference/dicty_2.7.toplevel.masked.fa'
genseq = bt.sequence(fi=fastaref, s=True)
print(open(genseq.seqfn).read())