## Binary Search Algorithm
## W Chen
## Only Work for Sorted Array
## Compared to mid, search only left or right, then recurse
## ---------------------------------------------------------

def binarySearch(array, first, last, target):
	if (first > last):
		return "not found"
	mid = int((first + last)/2)
	if (target == array[mid]):
		return mid
	if (target > array[mid]):
		first = mid +1
	else:
		last = mid - 1
	return binarySearch(array, first, last, target)

test_array = [3, 9, 10, 27, 38, 43, 82]
print (binarySearch(test_array, 0, 6, 3))
print (binarySearch(test_array, 0, 6, 27))
print (binarySearch(test_array, 0, 6, 82))
print (binarySearch(test_array, 0, 6, 13))