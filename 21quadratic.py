#21quadratic.py by Sophia Chen & Devin Fan

import math

def quad_formula(a, b, c):
	x1 = (-b + math.sqrt(b**2 - 4 * a * c)) / (2 * a)
	x2 = (-b - math.sqrt(b**2 - 4 * a * c)) / (2 * a)
	print('the x-intercepts are', round(x1, 4), 'and', round(x2, 4))
	return x1, x2
	
quad_formula(4, 10, 5)
quad_formula(1, 5, -5)
quad_formula(-8, 3, 5)