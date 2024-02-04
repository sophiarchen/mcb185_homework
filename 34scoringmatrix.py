#34scoringmatrix.py by Sophia Chen and Devin Fan

seq = 'ACGT'

print('', end=' ')
for n1 in seq:
	print(' ', n1, end='')
print()

for n1 in seq:
	print(n1, end=' ')
	for n2 in seq:
		if n1 == n2: 
			print('+1', end=' ')
		else: 
			print('-1', end=' ')   
	print()    
