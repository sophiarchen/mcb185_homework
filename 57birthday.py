#57birthday.py by Sophia Chen and Devin Fan

import random
import sys

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])

calendar = []
for i in range(1, days + 1):
	calendar.append(i)

shared_bdays = 0
for j in range(trials):
	all_bdays = []
	for k in range(people):
		bday = random.choice(calendar)
		all_bdays.append(bday)
	all_bdays.sort()
	for l in range(people - 1):
		if all_bdays[l] == all_bdays[l + 1]:
			shared_bdays += 1
			break

chance = (shared_bdays / trials) * 100
print(f'There is a {chance}% there is a shared birthday.')
