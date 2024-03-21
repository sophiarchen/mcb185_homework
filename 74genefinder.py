#74genefinder.py by Sophia Chen and Devin Fan

import mcb185
import sys

ntseq = []
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	defwords = defline.split()
	for nt in seq: 
		if nt in 'ATCG': ntseq.append(nt)
	ntseq = ''.join(ntseq)
	
	minlength = int(sys.argv[2])
	
	for frame in range(3): #3 frame translation on forward strand
		stops_used = {}
		orf = ntseq[frame:]
		
		for i in range(0, len(orf) - 3 + 1, 3):
			codon = orf[i:i+3]
			if codon == 'ATG':
				start = i+1
				
				for j in range(i, len(orf) - 2, 3):
					codon = orf[j:j+3]
					if codon == 'TAA' or codon == 'TAG' or codon == 'TGA':
						stop = j+3
						genelength = stop - start
						if genelength >= minlength:
							if stop not in stops_used:
								stops_used[stop] = True
								print('gene:', start, stop)
								print('found in the forward strand')
								break	
		
	revseq = mcb185.anti_seq(ntseq)
	for frame in range(3): #3 frame translation on reverse strand
		stops_used = {}
		orf = revseq[frame:]
		
		for i in range(0, len(orf) - 3 + 1, 3):
			codon = orf[i:i+3]
			if codon == 'ATG':
				start = i+1
				
				for j in range(i, len(orf) - 2, 3):
					codon = orf[j:j+3]
					if codon == 'TAA' or codon == 'TAG' or codon == 'TGA':
						stop = j+3
						genelength = stop - start
						if genelength >= minlength:
							if stop not in stops_used:
								stops_used[stop] = True
								print('gene:', start, stop)
								print('found in the reverse strand')
								break	