## insertionSort implementation in Python3
## W Chen
## find the right position for the ith element
## --------------------------------------------

def insertionSort(array):
	for i in range(len(array)):
		temp=array[i]
		j=i
		while (j>0):
			if (array[j-1]<temp):
				break
			array[j]=array[j-1]
			j=j-1

		array[j]=temp
		print ("After " + str(i+1) + " times, the array becomes " + str(array))
	return (array)

test_array=[38, 27, 43, 3, 9, 82, 10]
print ("The original array is: " + str(test_array))
print (insertionSort(test_array))