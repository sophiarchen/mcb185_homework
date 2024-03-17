#62skewer.py by Sophia Chen

import dogma
import mcb185
import sys

w = int(sys.argv[2])

ntseq = []
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	for nt in seq: 
		if nt in 'ATCG': ntseq.append(nt)
	ntseq = ''.join(ntseq)

	g = ntseq[0:w].count('G')
	c = ntseq[0:w].count('C')

	for i in range(len(ntseq) - w):
		off = ntseq[i]
		on = ntseq[i + w]
	
		if off == 'C': c -= 1
		elif off == 'G': g -=1
	
		if on == 'C': c += 1
		elif on == 'G': g += 1
	
		comp = (g+c)/w
	
		if (g+c) > 0: skew = (g-c)/(g+c)
		else:         skew = 0
	
		print(i, comp, skew)