#46savingthrows.py by Sophia Chen and Devin Fan

import random

tries = 1000

#normal condition
dc5 = 0  
dc10 = 0
dc15 = 0
for i in range(tries): 
	d1 = random.randint(1, 20)
	if d1 >= 5:  dc5 += 1
	if d1 >= 10: dc10 += 1 
	if d1 >= 15: dc15 += 1   

#advantage condition
dc5_adv = 0
dc10_adv = 0
dc15_adv = 0
max_roll = 0
for i in range(tries):
	d1 = random.randint(1, 20)
	d2 = random.randint(1, 20)
	if d1 > d2: max_roll = d1
	else:       max_foll = d2
	if max_roll >= 5:  dc5_adv += 1
	if max_roll >= 10: dc10_adv += 1
	if max_roll >= 15: dc15_adv += 1

#disadvantage condition
dc5_disadv = 0
dc10_disadv = 0
dc15_disadv = 0
min_roll = 0
for i in range(tries):
	d1 = random.randint(1, 20)
	d2 = random.randint(1, 20)
	if d1 < d2: min_roll = d1
	else:       min_roll = d2
	if min_roll >= 5: dc5_disadv += 1
	if min_roll >= 10: dc10_disadv += 1
	if min_roll >= 15: dc15_disadv += 1

print('DC\tNormal\tAdv\tDisadv')
print(f'5\t{dc5 / tries}\t{dc5_adv / tries}\t{dc5_disadv / tries}')
print(f'10\t{dc10 / tries}\t{dc10_adv / tries}\t{dc10_disadv / tries}')
print(f'15\t{dc15 / tries}\t{dc15_adv / tries}\t{dc15_disadv / tries}')

