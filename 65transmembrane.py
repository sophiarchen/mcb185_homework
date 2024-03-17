#65transmembrane.py by Sophia Chen and Devin Fan

import gzip
import mcb185
import sys

def kyte(seq):
	hydro_value = 0
	for aa in seq:
		if aa == 'A':
			hydro_value += 1.80
		elif aa == 'C':
			hydro_value += 2.50
		elif aa == 'D' or aa == 'E' or aa == 'N' or aa == 'Q':
			hydro_value += -3.50
		elif aa == 'F':
			hydro_value += 2.80
		elif aa == 'G':
			hydro_value += -0.40
		elif aa == 'H':
			hydro_value += -3.20
		elif aa == 'I':
			hydro_value += 4.50
		elif aa == 'K':
			hydro_value += -3.90
		elif aa == 'L':
			hydro_value += 3.80
		elif aa == 'M':
			hydro_value += 1.90
		elif aa == 'P':
			hydro_value += -1.60
		elif aa == 'R':
			hydro_value += -4.50
		elif aa == 'S':
			hydro_value += -0.80
		elif aa == 'T':
			hydro_value += -0.70
		elif aa == 'V':
			hydro_value += 4.20
		elif aa == 'W':
			hydro_value += -0.90
		elif aa == 'Y':
			hydro_value += -1.30
	return hydro_value / len(seq)


def hydroreg(seq):
	sigpep = seq[:30]
	for i in range(len(sigpep) - 8 + 1):
		signal = sigpep[i:i+8]
		if 'P' in signal: continue
		kyteval = kyte(signal)
		if kyteval >= 2.5: 
			sigpep = True
			break
	if sigpep != True: return False
	transreg = seq[30:]
	for i in range(len(transreg) - 11 + 1):
		trans = transreg[i:i+11]
		if 'P' in trans: continue
		kyteval = kyte(trans)
		if kyteval >= 2.0:
			transreg = True
			break
	if transreg == True: return True
	else:                return False	
	
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	transpro = hydroreg(seq)
	if transpro == True: print(defline)
	
	

	
		
		
		
