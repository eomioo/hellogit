#!/usr/bin/python3

# Filename: prime_factorization.py
# print Prime factors tree

n = int(input("Please input a number to find it's prime factors:"))

# initial the list L
L = []
f = 2
k = 2

while k != 1:
	k = n / f
	if k.is_integer():
		L.append(f)
		n = k
	else:
		f = f + 1

# print the prime factors list
print(L)
