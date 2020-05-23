## Bubble Sort Implementation in Python3
## W Chen
## Repeatedly compare adjacent elements and swap
## ----------------------------------------------

def swap(array, i, j):
	temp=array[i]
	array[i]=array[j]
	array[j]=temp
	return (array)

def bubbleSort(array):
	for i in range(len(array)-1, 0, -1):
		for j in range(0, i, 1):
			if (array[j]>array[j+1]):
				swap(array, j, j+1)

		print ("After "+str(len(array)-i)+" times, the array becomes "+str(array))
	return (array)

test_array=[38, 27, 43, 3, 9, 82, 10]
print ("The original array is: " + str(test_array))
print (bubbleSort(test_array))