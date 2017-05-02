## project euler problem 1
## sum of multiple of 3 or 5 below 1000
## more efficient way according to suggested solution
## damnguychen

####################################
## functions
# calculate the sum divisible by a number
# target is the max number we can have
# num is the divisor
def SumDivisibleBy(target, num):
	p = target//num

	# return num*sum(1:p) which is sum of 1:target
	return (1+p)*p/2*num # for instance, sum(3i)=3+6+9+...=3*(1+2+3+...)=3*(1+3i)*i/2

####################################
## main loop
target = 999
 
# I want to sum only 3i, 5j, where i and j are positive integers
# while 15k, where k are positive integers, will be repeated
solution = SumDivisibleBy(999, 3) + SumDivisibleBy(999, 5) - SumDivisibleBy(999, 15)
print (solution)
