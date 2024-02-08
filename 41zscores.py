#41zscores.py by Sophia Chen

import random

z1 = 0
z2 = 0
z3 = 0 
limit = 10000
for i in range(10000):
	r = random.gauss(0.0, 1.0)
	if r > 1: z1 += 1
	if r > 2: z2 += 1
	if r > 3: z3 += 1
print(1 - 2*z1/limit)
print(1 - 2*z2/limit)
print(1 - 2*z3/limit)