"""
Given a string representing a number, 
we need to get the sum of all possible sub strings of this string.

Input : s = "6759"
Output : 8421
sum = 6 + 7 + 5 + 9 + 67 + 75 + 
      59 + 675 + 759 + 6759
      = 8421

Input : s = "16"
Output : 23
sum = 1 + 6 + 16 = 23
"""

def SubstringSum(s):
	substring = []

	if s[0].isdigit() == False or s[0] == '0':
		s = s[1:len(s)]

	for i in range(len(s)):
		for j in range(i + 1, len(s) + 1):
			substring.append(s[i:j])

	sum = 0

	for num in substring:
		sum = sum + int(num)

	return sum


