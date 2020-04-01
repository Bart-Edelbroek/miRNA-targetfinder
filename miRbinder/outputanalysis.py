#!/usr/bin/env python
# file: genetoseq.py

import matplotlib.pyplot as plt
import csv
import pandas as pd

class Analysis(object):
	"""docstring for Analysis"""
	def __init__(self, genelist):
		self.genelist = open(genelist).read().split('\n')

	def plotoverlay(self, genelist):
		for a in range(1,(len(genelist)+1)):
			i = pd.read_csv(('MYPROFILEFILE-t'+str(a)+'q1.csv'), sep=';')
			x = i['idx']/len(i['idx'])
			y = []
			for n in i['minE']:
				if n < 0:
					y.append(n)
				else:
					y.append(0)
			axes = plt.gca()
			axes.set_xlim([0,1])
			#axes.set_ylim([-15,0])
			plt.plot(x,y,label=str(i.columns[1]))
			plt.legend(loc='center left', bbox_to_anchor=(1.04, 0.5))
		plt.savefig('fig1.pdf', bbox_inches='tight')


	def run(self):
		overlayplot = self.plotoverlay(self.genelist)