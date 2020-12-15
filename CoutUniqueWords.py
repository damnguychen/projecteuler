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

def CountUniqueWords2(textstr):
	# transfer all element to lower cases
	textstr = textstr.lower()

	# tokenize
	tokens = textstr.split(' ')

	return len(set(tokens))

print(CountUniqueWords2('a a b c b a'))