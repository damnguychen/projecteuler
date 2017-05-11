## project euler problem 2
## sum of Fibonacci sequence within 4,000,000
## damnguychen

#####################
## main loop
a=1
b=2
num=3
sum=2
while (num <= 4000000):
	if (num%2==0):
		sum=sum+num
	a=b
	b=num
	num=a+b

print (sum)