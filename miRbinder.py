#!/usr/bin/env python
# file: miRbinder.py
import sys
from miRbinder.genetoseq import Gene2seq

genelist = sys.argv[1]
a = Gene2seq(genelist)
b = a.run()

print(b)
