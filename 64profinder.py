#64profinder.py by Sophia Chen and Devin Fan

import dogma
import mcb185
import sys

ntseq = []
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	defwords = defline.split()
	for nt in seq: 
		if nt in 'ATCG': ntseq.append(nt)
	ntseq = ''.join(ntseq)

	prolen = int(sys.argv[2])
	procounter = 1 #provides unique identifier

	for frame in range(3): #3 frame translation on forward strand
		orf = ntseq[frame:]
		aaseq = dogma.translate(orf)
		proseqs = aaseq.split('*')
	
		for seq in proseqs:
			start = seq.find('M')
			if start != -1: 
				pro = list(seq[start:])
				if len(pro) >= prolen - 1:
					print(f'>{defwords[0]}-prot-{procounter}')
					print(f"{''.join(pro)}*")
					procounter += 1		
			
	rcseq = dogma.revcomp(ntseq) 

	for frame in range(3): #3 frame translation on reverse strand
		orf = rcseq[frame:]
		aaseq = dogma.translate(orf)
		proseqs = aaseq.split('*')
	
		for seq in proseqs:
			start = seq.find('M')
			if start != -1: 
				pro = list(seq[start:])
				if len(pro) >= prolen - 1:
					print(f'>{defwords[0]}-prot-{procounter}')
					print(f"{''.join(pro)}*")
					procounter += 1	