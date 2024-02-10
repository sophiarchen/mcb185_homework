#40demo.py by Sophia Chen

import random

for i in range(5):
	print(random.random())
	
for i in range(50):
	print(random.choice('AGCT'), end='')
print()

for i in range(50):
	r = random.random()
	if r < 0.7: print(random.choice('AT'), end ='')
	else:       print(random.choice('GC'), end='')
print()

for i in range(3):
	print(random.randint(1, 6))
	
for i in range(5):
	print(random.gauss(0.0, 1.0))