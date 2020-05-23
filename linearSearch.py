## Linear Search Algorithm Written in Python
## W Chen
## Search One by One and Return the Index
## -----------------------------------------

def linearSearch(array, target):
	for i in range (len(array)):
		if (array[i] == target):
			return i
	return "not found"

test_array = [3, 9, 10, 27, 38, 43, 82]
print (linearSearch(test_array, 3))
print (linearSearch(test_array, 27))
print (linearSearch(test_array, 82))
print (linearSearch(test_array, 13))