#43randomdna.py by Sophia Chen

import random

for i in range(1, 4):
	print(f'>seq-{i}') 
	for nt in range(random.randint(50, 60)):
		print(random.choice('AGCT'), end='')
	print()