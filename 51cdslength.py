#51cdslength.py by Sophia Chen

import gzip

path = '../MCB185/data/GCF_000005845.2_ASM584v2_genomic.gff.gz'
with gzip.open(path, 'rt') as fp:
	for line in fp:
		if line[0] == '#': continue #skips over comment lines
		words = line.split()
		if words [2] != 'CDS': continue
		cds_length = int(words[4]) - int(words[3]) + 1
		print(cds_length)
		