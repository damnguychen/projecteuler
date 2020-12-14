"""
Count unique words in a string
"""

def CountUniqueWords(textstr):
	# transfer all element to lower cases
	textstr = textstr.lower()

	# tokenize
	tokens = textstr.split(' ')

	# build dictionary
	textdict = {}

	for token in tokens:
		if token not in textdict:
			textdict[token] = 1

	return len(textdict)

print(CountUniqueWords('a a b c b a'))