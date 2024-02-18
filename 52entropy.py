#52entropy.py by Sophia Chen

import sys
import math

prob = []
for arg in sys.argv[1:]:
	f = float(arg)
	assert(f > 0 and f < 1)
	prob.append(f)

total = 0
for p in prob: total += p
if not math.isclose(total, 1.0):
	sys.exit('Error: the probs must sum to 1')

h = 0
for p in prob: 
	h += p * math.log2(p)
h = h * -1
print(f'The Shannon entropy is: {h:.3f}')