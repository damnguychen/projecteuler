## project euler problem 1
## sum of multiple of 3 or 5 below 1000
## damnguychen

######################################
## main loop

# choose numbers that are multiples of 3 or 5
numbers=[0]*999
for i in range(1, 1000, 1):
	if (i % 3 == 0 or i % 5 ==0):
		numbers[i-1]=i

# sum list of these numbers
print (sum(numbers))
