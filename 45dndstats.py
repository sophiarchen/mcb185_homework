#45dndstats.py by Sophia Chen and Devin Fan

import random

tries = 10000

#36D
total = 0
for i in range(tries):
	d1 = random.randint(1, 6)
	d2 = random.randint(1, 6)
	d3 = random.randint(1, 6)
	total = total + d1 + d2 + d3 
print('36D average stat value:', round(total / tries, 2))

#36Dr1
total = 0
for i in range(tries):
	for j in range(3):
		d = random.randint(1, 6)
		if d == 1: 
			d = random.randint(1, 6)
		total += d
print('36Dr1 average stat value:', round(total / tries, 2))

#3D6x2
total = 0
for i in range(tries):
	for j in range(3): 
		d1 = random.randint(1, 6)
		d2 = random.randint(1, 6)
		if d1 > d2: total += d1
		else:       total += d2
print('3D6x2 average stat value:', round(total / tries, 2))

#4D6d1
total = 0
for i in range(tries):
	d1 = random.randint(1, 6)
	d2 = random.randint(1, 6)
	d3 = random.randint(1, 6)
	d4 = random.randint(1, 6)
	min_d = 6
	if d1 < min_d: min_d = d1
	if d2 < min_d: min_d = d2
	if d3 < min_d: min_d = d3
	if d4 < min_d: min_d = d4
	total += d1 + d2 + d3 + d4 - min_d	
print('4D6d1 average stat value:', round(total / tries, 2))