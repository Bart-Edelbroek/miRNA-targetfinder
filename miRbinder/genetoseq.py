#!/usr/bin/env python
# file: genetoseq.py

import re, sys, pybedtools

class Gene2seq(object):
	"""docstring for Gene2seq"""
	def __init__(self, genelist):
		#read in gene_id's and reference files 
		self.genelist = open(genelist).read().split('\n')
		self.gfffile = open('./reference/D_discoideum_PASAua.gff').readlines()
		self.oribed = open('./reference/D_discoideum_PASAua.bed').readlines()
		self.fastaref = './reference/dicty_2.7.toplevel.masked.fa'

	def genetomRNA(self, genelist, gfffile):
		s = []
		for line in gfffile:
			if re.search("mRNA", line):
				for gene in genelist:
					if re.search(gene, line):
						s.append(re.search('(?<=ID=)\w+', line).group())
		return(s)


	#read in original .bed file


	#subset of .bed for genelist
	def mRNAtobed(self, mRNA_IDs,oribed):
		newbed = ""
		for line in oribed:
			for ID in mRNA_IDs:
				if re.search(str(ID), line): 
					newbed+=line
		return(newbed) 

	def run(self):
		mRNAs = self.genetomRNA(self.genelist, self.gfffile)
		newbed = self.mRNAtobed(mRNAs, self.oribed)
		bt = pybedtools.BedTool(newbed, from_string=True)
		genseq = bt.sequence(fi=self.fastaref, s=True, name=True)
		return(open(genseq.seqfn).read())