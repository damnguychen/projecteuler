## A palindromic number reads the same both ways
## The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99
## Find the largest palindrome made from the product of two 3-digit numbers
## damnguychen

#########################
## Functions
def CheckPalindrome(num):	# check if a number is a palindromic number
	str_num=str(num)
	for i in range(0, int(len(str_num)/2), 1):
		if (str_num[i]!=str_num[len(str_num)-i-1]):
			return False
	return True

def CheckProduct(num, num1, num2):	# check if a number is a product of two x-digit numbers
	digit=len(str(num1))	# num1 is the min x-digit number, num2 is the max x-digit number
	for i in range(num2, num1-1, -1):
		if (num % i==0):
			result=int(num/i)
			if (len(str(result))==digit):
				return True
	return False

def LargestPalindrome(num1, num2):	# find largest palindrome made from product of two x-digit numbers
	MaxNum=num2*num2	# max product available of two x-digit number
	MinNum=num1*num1 	# min product available of two x-digit number
	for i in range(MaxNum, MinNum-1, -1):
		if (CheckPalindrome(i)==True):
			if(CheckProduct(i, num1, num2)==True):
				return (i)

#########################
## Main loop
print (LargestPalindrome(100, 999))