#36poisson.py by Sophia Chen and Devin Fan

import math

def poisson(n, k):
	k_fact = math.factorial(k)
	prob = (n**k * math.e**(-n)) / k_fact
	return prob
	
print(poisson(3, 2))
print(poisson(4, 1))
print(poisson(5, 5))
print(poisson(7, 6))
print(poisson(3, 11))