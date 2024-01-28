#22oligotemp.py by Sophia Chen & Devin Fan

import math

def oligo_temp(a, t, c, g):
	oligo_length = (a + t + c + g)/2
	if oligo_length <= 13:
		tm = (a+t)*2 + (g+c)*4
	else:
		tm = 64.9 + 41*(g + c - 16.4)/(a + c+ t+ g)
	print('The melting temperature for your oligo is:', round(tm, 2))
	return tm
	

oligo_temp(8, 8, 4, 4)

oligo_temp(8, 8, 6, 6)

oligo_temp(10, 10, 10, 10)