"""
Given a list of numbers: 10,20,30,40, what is the code to produce the output: 100, 90, 70, 40.
What would be its time complexity?
"""

def ShowTarget(numlst):
	target = []

	for i in range(len(numlst)):
		sum = 0
		for j in range(i, len(numlst)):
			sum = sum + numlst[j]
		target.append(sum)

	return target

def ShowTarget_efficient(numlst):
	"""
	start from 40
	then 40 + 30
	then 40 + 30 + 20
	then 40 + 30 + 20 + 10
	avoid scanning repeatedly
	"""

	target = []
	sum = 0

	for i in range(-1, 0 - len(numlst) - 1, -1):
		sum = sum + numlst[i]
		target.append(sum)

	result = []
	for i in range(-1, 0 - len(numlst) - 1, -1): 
		result.append(target[i])

	return result