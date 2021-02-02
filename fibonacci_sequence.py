#!/usr/bin/python3

# FIlename: fibonacci_sequence.py
# print fibonacci sequence

# calculate n-th term of fibonacci sequence
def fibo(n):
	if n <= 1:
		return 1
	else:
		return(fibo(n-1) + fibo(n-2))

# input how many terms to calculate
nterms = int(input('Fibonacci number up to n-th term:'))

# print the result
if nterms <= 0:
	print('Please enter a postive integer')
else:
	for i in range(nterms):
		print(i+1,'th is:',fibo(i+1))