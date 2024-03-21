#70demo.py

import random

d = {'dog': 'woof', 'cat': 'meow'}
print(d)
print(d['cat'])
'''
size = 100
words = []
wordd = {}
for i in range(size):
	token = []
	for j in range(10):
		token.append(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
	token = ''.join(token)
	words.append(token)
	wordd[token] = True
print(words)

for i in range(1000):
	if 'MYNAMEISSOPH' in words:
		print('found')

import mcb185
import sys
import itertools

kcount = {}
k = 3

for aas in itertools.product('ACDEFGHIKLMNPQRSTVWY', repeat = 3):
	kmer = ''.join(aas)
	kcount[kmer] = 0

for defline, seq in mcb185.read_fasta(sys.argv[1]):
	for i in range(len(seq) -k +1):
		kmer = seq[i:i+k]
		
		if kmer not in kcount: kcount[kmer] = 0
		kcount[kmer] += 1

for kmer, n in kcount.items():
	print(kmer, n)
'''