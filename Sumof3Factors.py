"""
sum all integers that have exactly 3 factors in the list
"""
import math

def Sumof3Factors(lst):
	result = 0

	for num in lst:
		factor_count = 0

		for i in range(1, int(math.sqrt(num)) + 1):
			if num % i == 0:
				if num / i == i:
					factor_count += 1

				else:
					factor_count += 2

		if factor_count == 4:
			result += num

	return result

print(Sumof3Factors([3, 6, 7, 9, 21, 100]))