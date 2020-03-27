#!/usr/bin/env python
# file: genetoseq.py

import re, sys, pybedtools

#read in gene_id's 
genelist = open(sys.argv[1]).read().split('\n')

gfffile = open('./reference/D_discoideum_PASAua.gff').readlines()

def genetotranscript(genelist, gfffile):
	s = []
	for line in gfffile:
		if re.search("mRNA", line):
			for gene in genelist:
				if re.search(gene, line):
					s.append(re.search('(?<=ID=)\w+', line).group())
	return(s)


#read in original .bed file
oribed = open('./reference/D_discoideum_PASAua.bed').readlines()

#subset of .bed for genelist
newbed = ""

for line in oribed:
	for gene in genelist:
		if re.search(str(gene), line): 
			newbed+=line 

#print(newbed)

bt = pybedtools.BedTool(newbed, from_string=True)
fastaref = './reference/dicty_2.7.toplevel.masked.fa'
genseq = bt.sequence(fi=fastaref, s=True)
#print(open(genseq.seqfn).read())

r = genetotranscript(genelist, gfffile)
print(r)