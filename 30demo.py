#30demo.py by Sophia Chen

while True:
	print('hello')
	
i = 0
while True:
	i = i + 1
	print('hey', i)
	if i == 3: break
	
i = 0
while i < 3:
	print(i)
	i = i + 1
print('the final value of i is', i)

i = 0
while i < 10:
	print(i)
	i = i + 3
print('the final value of i is', i)


for i in range(1, 10, 3):
	print(i)
	
for i in range(0, 5):
	print(i)
	
for i in range(5):
	print(i)

for char in 'hello':
	print(char)
	
seq = 'GAATTC'
for nt in seq:
	print(nt)

for n1 in 'ACGT':
	for n2 in 'ACGT':
		if n1 == n2: print(n1, n2, '+1')
		else:        print(n1, n2, '-1')

nts = 'ACGT'
for n1 in nts:
	for n2 in nts:
		if n1 == n2: print(n1, n2, '+1')
		else:        print(n1, n2, '-1')

limit = 4
for i in range(0, limit):
	for j in range(i + 1, limit): #set 2nd loop 1 beyond position of 1st loop
		print(i + 1, j + 1)
