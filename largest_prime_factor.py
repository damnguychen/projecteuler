## project euler problem 3
## find largest prime factor of a number
## damnguychen

import math
########################
## Function

def CheckPrime(num):	# check if this number is a prime
	if (num==2 or num==3):
		return True
	for i in range(2, int(math.sqrt(num))+1, 1):
		if (num%i==0):
			return False
	return True

def Factorize(target, num):		# keep dividing target by num until unavailable
	while (target % num == 0) & (target!=num):
		target=int(target/num)
	return (target)		# find a new target to factorize

def MaxPrimeFactor(target):
	num=2	# initialization with smallest prime
	while (num < target):
		if (CheckPrime(num)==True):
			target=Factorize(target, num)	# keep trying to factorize target starting from small prime
		num=num+1
	return (target)

########################
## Main loop
print(MaxPrimeFactor(600851475143))