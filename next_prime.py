#!/usr/bin/python3

# Filename: next_prize.py
# print next prime number

n = int(input("Please input a number to find the next prime:"))

# determine wheter k is a prime number
def isprime(k):
	for i in range(2, k):
		if (k/(i)).is_integer():
			return False
	return True

# look for the next prime number bigger than n
while True:
	n = n + 1
	if isprime(n):
		print(n)
		break