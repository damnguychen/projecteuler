"""
count all words in the text and their counts
"""

def WordCount(textstr):
	# transfer all element to lower case
	textstr = textstr.lower()

	# tokenize
	text = textstr.split(' ')

	# build dictionary
	textdict = {}

	for token in text:
		if token in textdict:
			textdict[token] += 1

		else:
			textdict[token] = 1

	return textdict

print(WordCount('I love collaboration I hate pointing fingers at each other'))