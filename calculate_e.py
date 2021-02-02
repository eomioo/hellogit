#!/usr/bin/python3

# FIlename: calculate_e.py
# Calculate e

from decimal import *

# the 100 digits of Euler's number
e = Decimal('2.718281828459045235360287471352662497757247093699959574966967627724076630353547594571382178525166427')

# calculate the factorial of n
def fact(n):
	if n == 0:
		return 1
	else:
		return n * fact(n-1)

# calculate the sum of 1/n!
def sum(k):
	res = 1 / Decimal( fact(k) )
	if k > 0:
		return res + sum(k-1)
	else:
		return res

# setup the digits
getcontext().prec = 100

# calculate and print e_estimate
e_estimate = sum(100)
print(e_estimate)
print(e)

# compare e_estimate with e
error = e_estimate - e
print(error)