#47deathsaves.py by Sophia Chen and Devin Fan

import random

turns = 10000

death = 0
stable = 0
revive = 0
for i in range(turns):
	failure = 0
	success = 0
	rev = 0
	while failure < 3 and success < 3 and rev < 1:
		d = random.randint(1, 20)
		if d == 1:     failure += 2
		elif d < 10:   failure += 1
		elif d == 20:  rev += 1
		elif d >= 10:  success += 1
	if failure >= 3:   death += 1
	elif success >= 3: stable += 1
	elif rev == 1:     revive += 1
total = death + stable + revive
print('die:', death / total)
print('stabilize:', stable / total)
print('revive:', revive / total)