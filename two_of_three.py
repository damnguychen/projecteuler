def two_of_three(a, b, c):
	"""
	Return x*x + y*y
	where x and y are the two largest members of the positive numbers a, b and c
	"""

	if a < b and a < c:
		return b*b + c*c

	elif b < a and b < c:
		return a*a + c*c

	else:
		return a*a + b*b

print(two_of_three(5, 5, 5))