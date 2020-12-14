# sum factor of 3

def SumOf3Factor(lst):
	result = 0

	for num in lst:
		if num % 3 == 0:
			result += num / 3

	return result

# print(SumOf3Factor([3, 6, 9]))
print(SumOf3Factor([2, 4, 9]))