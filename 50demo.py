#50demo.py by Sophia Chen

#Indexes 
seq = 'GAATTC'
print(seq[0], seq[1])
print(seq[-1])

for i in range(len(seq)):
	print(i, seq[i])

#Slices
s = 'ABCDEFGHIJ'
print(s[0:5])
print(s[0:8:2])
print(s[0:5], s[:5]) #initial value replaced by 0
print(s[5:(len(s))], s[5:]) #final value replaced by len(s)
print(s, s[::], s[::1], s[::-1])

#Tuples
tax = ('Homo', 'sapiens', 9606) 
print(tax)
print(tax[0])
print(tax[::-1])

def quadratic(a, b, c):
	x1 = (-b + (b**2 - 4*a*c)**0.5) / (2*a)
	x2 = (-b - (b**2 - 4*a*c)**0.5) / (2*a)
	return x1, x2
x1, x2 = quadratic(5, 6, 1)     #unpacked tuple
print(x1, x2)
intercepts = quadratic(5, 6, 1) #packed tuple
print(intercepts[0], intercepts[1])

#enumerate() and zip()
nts = 'ACGT'
for i in range(len(nts)):
	print(i, nts[i])

for i, nt in enumerate(nts):
	print(i, nt)

names = ('adenine', 'cytosine', 'guanine', 'thymine')
for i in range(len(names)):
	print(nts[i], names[i])
	
for nt, name in zip(nts, names):
	print(nt, name)

for i, (nt, name) in enumerate(zip(nts, names)):
	print(i, nt, name)

#Lists
nts = ['A', 'T', 'C']
print(nts)
nts[2] = 'G'
print(nts)
nts.append('C')
print(nts)
last = nts.pop()
print(last)

nts.sort()
print(nts)
nts.sort(reverse = True)
print(nts)

#split() and join()
text = 'good day    to you'
words = text.split()
print(words)

line = '1.41, 2.72, 3.14'
print(line.split(','))

alph = 'ACDEFGHIKLMPQRSVW'
print(alph)
aas = list(alph)
print(aas)
s = '-'.join(aas)
print(s)
s = ''.join(aas)
print(s)