#56birthday.py by Sophia Chen and Devin Fan

import random
import sys

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])

shared_bdays = 0
for i in range(trials):
	all_bdays = []
	for j in range(people):
		bday = random.randint(1, days)
		all_bdays.append(bday)
	all_bdays.sort()
	for k in range(people - 1):
		if all_bdays[k] == all_bdays[k + 1]:
			shared_bdays += 1
			break

chance = (shared_bdays / trials) * 100
print(f'{chance:.2f}% chance there is a shared birthday.')

	
	
		