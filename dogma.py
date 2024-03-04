#dogma.py by Sophia Chen

import math

def transcribe(dna):
	return dna.replace('T', 'U')
	
def revcomp(dna):
	rc = []
	for nt in dna[::-1]:
		if   nt == 'A': rc.append('T')
		elif nt == 'C': rc.append('G')
		elif nt == 'G': rc.append('C')
		elif nt == 'T': rc.append('A')
		else:           rc.append('N')
	return ''.join(rc)

def translate(dna):
	aas = []
	for i in range(0, len(dna), 3):
		codon = dna[i:i+3]
		if   codon == 'ATG': aas.append('M')
		elif codon == 'TAA' or codon == 'TAG' or codon == 'TGA': aas.append('*')
		elif codon == 'TTT' or codon == 'TTC': aas.append('F')
		elif codon == 'TTA' or codon == 'TTG': aas.append('L')
		elif codon == 'CTT' or codon == 'CTC' or codon == 'CTA' or codon == 'CTG': aas.append('L')
		elif codon == 'ATT' or codon == 'ATC' or codon == 'ATA': aas.append('I')
		elif codon == 'GTT' or codon == 'GTC' or codon == 'GTA' or codon == 'GTG': aas.append('V')
		elif codon == 'TCT' or codon == 'TCC' or codon == 'TCA' or codon == 'TCG': aas.append('S')
		elif codon == 'CCT' or codon == 'CCC' or codon == 'CCA' or codon == 'CCG': aas.append('P')
		elif codon == 'ACT' or codon == 'ACC' or codon == 'ACA' or codon == 'ACG': aas.append('T')
		elif codon == 'GCT' or codon == 'GCC' or codon == 'GCA' or codon == 'GCG': aas.append('A')
		elif codon == 'TAT' or codon == 'TAC': aas.append('Y')
		elif codon == 'CAT' or codon == 'CAC': aas.append('H')
		elif codon == 'CAA' or codon == 'CAG': aas.append('Q')
		elif codon == 'AAT' or codon == 'AAC': aas.append('N')
		elif codon == 'AAA' or codon == 'AAG': aas.append('K')
		elif codon == 'GAT' or codon == 'GAC': aas.append('D')
		elif codon == 'GAA' or codon == 'GAG': aas.append('E')
		elif codon == 'TGT' or codon == 'TGC': aas.append('C')
		elif codon == 'TGG': aas.append('W')
		elif codon == 'CGT' or codon == 'CGC' or codon == 'CGA' or codon == 'CGG': aas.append('R')
		elif codon == 'AGT' or codon == 'AGC': aas.append('S')
		elif codon == 'AGA' or codon == 'AFF': aas.append('R')
		elif codon == 'GGT' or codon == 'GGC' or codon == 'GGA' or codon == 'GGG': aas.append('G')
	return aas
	
def gc_comp(seq):
	return (seq.count('C') + seq.count('G')) / len(seq)
	
def gc_skew(seq):
	c = seq.count('C')
	g = seq.count('G')
	if c + g == 0: return 0
	return (g - c) / (g + c)
	
def entropy(a, t, c, g):
	prob = []
	total = a + t + c + g
	if a > 0: prob.append(a / total)
	if t > 0: prob.append(t / total)
	if c > 0: prob.append(c / total)
	if g > 0: prob.append(g / total)
	h = 0
	for p in prob: 
		h += p * math.log2(p)
	return h * -1