#!/usr/bin/env python
# file: miRbinder.py
import sys, subprocess
import argparse
from miRbinder.genetoseq import Gene2seq
from miRbinder.outputanalysis import Analysis
from os import system

parser = argparse.ArgumentParser()
parser.add_argument("-is","--input_srna", required=True, 
	help ="Input (small)RNA sequence")
parser.add_argument("-il","--input_list", required=True, 
	help ="List of dictyBase geneIDs on\
	which to find binding sites for the input RNA")
parser.add_argument("-s","--steps", 
	help= "Define number of steps in which to\
	evaluate the average binding energy for input list; default steps 100", 
	type=int)
parser.add_argument("-oo","--outoverlay", 
	help= "Output name for overlay plot, default fig1.pdf")
parser.add_argument("-oa","--outaverage", 
	help= "Output name for average energy plot, default fig2.pdf")
args = parser.parse_args()

genelist = args.input_list
query_in = args.input_srna
if args.steps:
	combinedplot_steps = args.steps
else:
	combinedplot_steps = 100
if args.outoverlay:
	out_fig1 = args.outoverlay
else:
	out_fig1 = 'fig1.pdf'
if args.outaverage:
	out_fig2 = args.outaverage
else:
	out_fig2 = 'fig2.pdf'

g2seq = Gene2seq(genelist)
sequencelist = g2seq.run()

geneseq = open("genesequences.fasta","w+")
geneseq.write(sequencelist)

subprocess.run(["IntaRNA", "-t", "genesequences.fasta", "-q", query_in,
	"--seedBP=6", "--seedNoGU", "--seedMinPu=0.001", "--outMinPu=0.001",
	"--outNoLP", "--out=tMinE:MYPROFILEFILE.csv"])

analysis = Analysis(genelist, combinedplot_steps, out_fig1, out_fig2)
analysis.run()

subprocess.run(["rm ./MYPROFILEFILE-t*q1.csv"], shell = True)