## Quick Sort Implementation in Python3
## W Chen
import statistics

## ------------------------------------------
def QuickSort(array, first, last):
	if (first>=last):
		return 
		
	pivot_pos=Partition_med(array, first, last)
	print('the pivot pos is: '+str(pivot_pos))
	QuickSort(array, first, pivot_pos-1)	# quick sort left part
	QuickSort(array, pivot_pos+1, last)	# quick sort right part


## use the first element as pivot
def Partition_first(array, first, last):
	pivot=array[first]	# choose the first element as pivot
	print('the pivot this time is : '+ str(pivot))
	i=first + 1		# guarantee all right to i is greater than pivot
	for j in range(first + 1, last+1, 1):
		if (array[j]<pivot):
			Swap(array, j, i)
			i=i+1
	
	Swap(array, first, i-1)
	print('the array after partition is: '+str(array))
	return i-1

## use the last element as pivot
def Partition_last(array, first, last):
	pivot=array[last]
	print('the pivot this time is : '+ str(pivot))
	i=first 	# guarantee all left to i is smaller than pivot
	for j in range(first, last, 1):
		if (array[j]<pivot):
			Swap(array, j, i)
			i=i+1
	
	Swap(array, last, i)
	print('the array after partition is: '+str(array))
	return i

## use median of three as pivot
def Partition_med(array, first, last):
	pos=Med(array, first, last)
	
	if(pos==first):
		return Partition_first(array, first, last)
	elif(pos==last):
		return Partition_last(array, first, last)
	else:
		pivot=array[pos]
		print('the pivot this time is : '+ str(pivot))
		i=first
		for j in range(first, last + 1, 1):
			if (array[j]<pivot):
				Swap(array, j, i)
				i=i+1
				if (i==pos):
					i=i+1	# skip pivot
	
		Swap(array, pos, i-1)
		print('the array after partition is: '+str(array))
		return i-1

def Med(array, first, last):
	f=array[first]
	l=array[last]
	middle=(first + last)//2
	m=array[middle]
	result=statistics.median([f, m, l])

	if (result==f):
		return first
	elif (result==m):
		return middle
	elif (result==l):
		return last

def Swap(array, i, j):
	temp=array[j]
	array[j]=array[i]
	array[i]=temp
	return array

test_array=[3, 8, 2, 5, 1, 4, 7, 6]
print ('test array is : ' + str(test_array))
QuickSort(test_array, 0, len(test_array)-1)
print ('sorted test array is : ' + str(test_array))