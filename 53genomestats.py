#53genomestats.py by Sophia Chen and Devin Fan

import gzip
import sys 
import math

#Calculates mean
def mean(nums):
	total = 0
	for num in nums: total += num
	return total / len(nums) 

#Calculates median 
def median(nums):
	nums.sort()
	if len(nums) % 2 == 0:
		med_1 = nums[len(nums) // 2] 
		med_2 = nums[(len(nums) // 2) - 1]
		median = (med_1 + med_2) / 2
	else: 
		median = nums[len(nums) // 2]
	return median 
	
#Calculates minimum
def minimum(nums):
	mini = nums[0]
	for num in nums[1:]:
		if num < mini: mini = num
	return mini
	
#Calculates maximum
def maximum(nums):
	maxi = nums[0]
	for num in nums[1:]:
		if num > maxi: maxi = num
	return maxi
	
#Calculates standard deviation
def stddev(nums):
	total = 0
	for num in nums: total += num
	mean = total / len(nums)
	diff = 0
	for num in nums[0:]: 
		diff += ((int(num) - mean) ** 2)
	denom = len(nums) 
	return math.sqrt(diff / denom)
	
gffpath = sys.argv[1]
feature = sys.argv[2]

nt_lengths = []
with gzip.open(sys.argv[1], 'rt') as fp:
	for line in fp:	
		if line[0] != '#':
			data = line.split()
			if data[2] == feature:
				nt_lengths.append(int(data[4]) - int(data[3]) + 1)

print('Type:', feature)
print('N:', len(nt_lengths)) 
print('Min:', minimum(nt_lengths))
print('Max:', maximum(nt_lengths))
print('Mean:', round(mean(nt_lengths), 2))
print('Std Dev:', round(stddev(nt_lengths), 2))
print('Median:', round(median(nt_lengths), 2))
	