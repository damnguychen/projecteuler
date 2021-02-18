import math

def largest_factor(n):
	"""
	Return the largest factor of n that is smaller than n
	"""

	div = 2
	while div <= math.sqrt(n):
		if n % div == 0:
			return n / div

		else:
			div += 1

	return 1

print(largest_factor(13))