## project euler problem 5
## find smallest positive number that can is evenly divisible by all of 1 to 20
## damnguychen

import math

## General Thoughts
## factorize each number and find lcm
# least common multiple from 1 to 10
# 1=1
# 2=2
# 3=3
# 4=2*2
# 5=5
# 6=2*3
# 7=7
# 8=2*2*2
# 9=3*3
# 10=2*5
# 2*2*2*3*3*5*7 for 1 to 10

#########################################
## Functions
def CheckPrime(num):	# check if this number is a prime
	if (num==2 or num==3):
		return True
	for i in range(2, int(math.sqrt(num))+1, 1):
		if (num%i==0):
			return False
	return True

def CountPrime(maxnum):	# count how many prime from 1 to maxnum
	count=0
	for i in range(2, maxnum+1, 1):
		if(CheckPrime(i)==True):
			count=count+1
	return count

def Factorize(num, count_prime):
	new_prime_count_list=[0]*count_prime
	prime_pos=-1
	for i in range(2, num+1, 1):
		if(CheckPrime(i)==True):
			prime_pos=prime_pos+1
			while (num % i == 0):
				num=int(num/i)
				new_prime_count_list[prime_pos]=new_prime_count_list[prime_pos]+1
	return new_prime_count_list


def UpdateList(list, newlist, count_prime):
	for i in range(0, count_prime, 1):
		if (list[i]<newlist[i]):
			list[i]=newlist[i]

def FindLcm(maxnum):	# find lcm from 1 to maxnum
	# make sure how many prime number from 1 to maxnum
	count_prime=CountPrime(maxnum)
	prime_count_list=[0]*count_prime

	# factorize each number, return a list of prime factor count
	for i in range(2, maxnum+1, 1):
		new_prime_count_list=Factorize(i, count_prime)

	# update the list of prime factor count by choosing max number of each slot
		UpdateList(prime_count_list, new_prime_count_list, count_prime)

	# sum each count multiplies each prime
	sum=1
	prime_pos=-1
	print(prime_count_list)
	for i in range(2, maxnum+1, 1):
		if (CheckPrime(i)==True):
			prime_pos=prime_pos+1
			sum=sum*math.pow(i, prime_count_list[prime_pos])
	
	return sum

########################################
## Main loop
print(FindLcm(20))