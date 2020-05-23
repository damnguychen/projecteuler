## Selection Sort
## W Chen
## Find smallest element and swap to the head
## ------------------------------------------

def swap(array, i, j):
	temp=array[i]
	array[i]=array[j]
	array[j]=temp
	return (array)

def selectionSort(array):
	for i in range (len(array)):
		minIndex=i
		j=i + 1

		# find min value
		for j in range (j, len(array)):
			if (array[j]<array[minIndex]):
				minIndex=j

		# swap min value to the head
		swap(array, i, minIndex)
		print ("After " + str(i+1) + " times the array becomes "+ str(array))
	return (array)

test_array=[38, 27, 43, 3, 9, 82, 10]
print ("The original array is: " + str(test_array))
print (selectionSort(test_array))