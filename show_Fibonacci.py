"""
write a function to calculate the first N elements in the Fibonacci numbers
"""

"""
logic

Fibo(n) = Fibo(n - 2) + Fibo(n - 1)
Fibo(1) = 0
Fibo(2) = 1
"""

def show_Fibonacci(N):
	fibo = [0, 1]

	if N == 1:
		return [0]

	elif N == 2:
		return fibo

	else:
		for i in range(2, N):
			fibo.append(fibo[i - 1] + fibo[i - 2])

		return fibo

print(show_Fibonacci(10))

