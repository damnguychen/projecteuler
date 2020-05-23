## Merge Sort implementation in Python 3
## W Chen
## recursively divide and merge
## -------------------------------------------

def mergeSort(array, first, last):
	if (first>=last):	# stop recursion
		return array
	mid = (first + last)//2 ## in python3 divide is // instead of / in python2
	mergeSort(array, first, mid)
	mergeSort(array, mid + 1, last)

	merge(array, first, last)
	print (array)

def merge(array, first, last):
	temp = [0]*len(array)
	mid = (first + last)//2
	i=first
	j=mid + 1
	k=0
	while (i<=mid and j<=last): # when both sides are long enough
		if (array[i]<array[j]):
			temp[k]=array[i]
			i=i+1
			k=k+1
		else:
			temp[k]=array[j]
			k=k+1
			j=j+1

	while (i<=mid): # when right side already sorted into temp array and left side is to be sorted
		temp[k]=array[i]
		k=k+1
		i=i+1
	while (j<=last): # when left side already sorted into temp array and right side is to be sorted
		temp[k]=array[j]
		k=k+1
		j=j+1
	print (("Temp array is ")+ str(temp))
	for l in range(first, last+1, 1):
		array[l]=temp[l-first]

test_array=[9, 4, 8, 3, 1, 2, 5]
print ("The original array is: " + str(test_array))
mergeSort(test_array, 0, len(test_array)-1)

