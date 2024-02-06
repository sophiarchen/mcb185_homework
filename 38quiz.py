#Co-Authors: Sophia Chen and Devin Fan

pi = 0
const = 1 
x = 1

for i in range(0, 100000):
	pi = pi + (const / x)
	x = x + 2
	const = const * -1
pi = pi * 4
print(pi)