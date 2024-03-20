#63dust.py by Sophia Chen and Devin Fan

import mcb185
import dogma
import sys
import math

window_size = int(sys.argv[2])
entropy = float(sys.argv[3])

ntseq = []
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	for nt in seq: 
		if nt in 'ATCG': ntseq.append(nt)
	ntseq = ''.join(ntseq)
	
	modseq = []
	for i in range(0, len(ntseq), window_size):
		chunk = ntseq[i:i+window_size]
		a = chunk.count('A')
		t = chunk.count('T')
		c = chunk.count('C')
		g = chunk.count('G')
		h = dogma.entropy(a, t, c, g)
		if h >= entropy: 
			for nt in chunk: modseq.append(nt)
		else: 
			for nt in chunk: modseq.append('N')
	modseq = ''.join(modseq)
	print(f'>{defline}\t{modseq}')