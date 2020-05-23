## Algorithms 1, Programming assignment 1
## W Chen
## Implementing Karatsuba algorithm in Python3

# Test case
# 5678 * 1234
# 100 * 100
# 1000 * 100
# 15 * 150
# 400*25

def karatsuba(x, y):
	n_x=len(str(x))	# number of digit of x
	n_y=len(str(y))	# number of digit of y
	if (n_x==1 or n_y==1):
		return x*y
	n=max(n_x, n_y)

	a= x//pow(10, round(n/2))
	b= x%pow(10, round(n/2))
	c= y//pow(10, round(n/2))
	d= y%pow(10, round(n/2))

	ac=karatsuba(int(a), int(c))
	bd=karatsuba(int(b), int(d))
	ad_plus_bc=karatsuba(int(a+b), int(c+d)) - ac - bd

	print('ac= ', ac)
	print('bd= ', bd)
	print('ad_plus_bc= ', ad_plus_bc)

	result=ac*pow(10, 2*round(n/2)) + ad_plus_bc*pow(10, round(n/2)) + bd

	return result

print ('result=', karatsuba(3141592653589793238462643383279502884197169399375105820974944592
	, 2718281828459045235360287471352662497757247093699959574966967627))