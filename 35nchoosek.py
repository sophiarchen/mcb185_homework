#35nchoosek.py by Sophia Chen

import math

def nchoosek(n, k):
	n_fact = math.factorial(n)
	k_fact = math.factorial(k)
	diff_fact = math.factorial(n-k)
	ans = n_fact / (k_fact * diff_fact)
	return ans
	
print(nchoosek(2, 1))
print(nchoosek(3, 2))
print(nchoosek(5, 4))
