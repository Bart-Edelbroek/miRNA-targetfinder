#!/usr/bin/env python
# file: genetoseq.py

import matplotlib.pyplot as plt
import csv
import pandas as pd
import numpy as np

class Analysis(object):
	"""docstring for Analysis"""
	def __init__(self, genelist, steps):
		self.genelist = open(genelist).read().split('\n')
		self.steps = steps

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
		plt.clf()

	def plotcombined(self, genelist, steps):
		comb = np.array([])
		for a in range(1,(len(genelist)+1)):
			i = pd.read_csv(('MYPROFILEFILE-t'+str(a)+'q1.csv'), sep=';')
			x = np.array(i['idx']/len(i['idx']))
			y = np.array([])
			for n in i['minE']:
				if n < 0:
					y = np.append(y, n)
				else:
					y = np.append(y, 0)
			s = np.array_split(y,int(steps))
			a = np.array([])
			for l in s:
				a = np.append(a, np.average(l))
			comb = np.append(comb, a)
		y = (np.mean(np.array_split(comb,len(genelist)), axis=0))
		x = np.linspace(0,1, int(steps))
		plt.plot((x),y)
		plt.savefig('fig2.pdf')

	def run(self):
		overlayplot = self.plotoverlay(self.genelist)
		plotcomb = self.plotcombined(self.genelist, self.steps)