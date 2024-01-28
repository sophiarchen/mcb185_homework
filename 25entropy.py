#25entropy.py by Sophia Chen & Devin Fan

import math

def shannon_entropy(a, c, t, g):
	total = a + c + t + g
	prob_a = a / total
	prob_c = c / total
	prob_t = t / total
	prob_g = g / total
	
	if a == 0:
		info_c = math.log2(prob_c)
		info_t = math.log2(prob_t)
		info_g = math.log2(prob_g)
		h = -(prob_c * info_c + prob_t * info_t + prob_g * info_g)
	elif c == 0:
		info_a = math.log2(prob_a)
		info_t = math.log2(prob_t)
		info_g = math.log2(prob_g)
		h = -(prob_a * info_a + prob_t * info_t + prob_g * info_g)
	elif t == 0:
		info_a = math.log2(prob_a)
		info_c = math.log2(prob_c)
		info_g = math.log2(prob_g)
		h = -(prob_a * info_a + prob_c * info_c + prob_g * info_g)
	elif g == 0: 
		info_a = math.log2(prob_a)
		info_c = math.log2(prob_c)
		info_t = math.log2(prob_t)
		h = -(prob_a * info_a + prob_c * info_c + prob_t * info_t)
	else:
		info_a = math.log2(prob_a)
		info_c = math.log2(prob_c)
		info_t = math.log2(prob_t)
		info_g = math.log2(prob_g)
		h = -(prob_a * info_a + prob_c * info_c + prob_t * info_t + prob_g * info_g)
	print('Shannon entropy is:', round(h, 4))
	return h
	
shannon_entropy(4, 4, 4, 4)
shannon_entropy(0, 8, 8, 8)
shannon_entropy(6, 5, 4, 0)