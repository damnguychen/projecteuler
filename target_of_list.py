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