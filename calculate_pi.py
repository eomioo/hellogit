#!/usr/bin/python3

# FIlename: calculate_pi.py
# Calculate pi using Chudnovsky algorithm

from decimal import *

pi = Decimal('3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679')

# compute the factorial of n
def fact(n):
	if n == 0:
		return 1
	else:
		return n * fact(n-1)

# compute the sum form 1 to k
def sum(k):
	a = Decimal(fact(6*k)*(545140134*k+13591409))
	b = Decimal(fact(3*k)*(fact(k)**3)*((-262537412640768000)**k))
	res = a/b
	if k > 0:
		return res + sum(k-1)
	else:
		return res

# root_precision
def num(root_precision):
	p = getcontext().prec
	getcontext().prec = root_precision
	d = Decimal(10005).sqrt()
	getcontext().prec = p
	print(d)
	return 426880 * Decimal(10005).sqrt()

# calculate pi with given precision
def chudnovsky(k, root_precision):
	return num(root_precision) / sum(k)


getcontext().prec = 100
pi_estimate = chudnovsky(10, 100)
print(pi_estimate)
print(pi)
error = pi_estimate - pi
print('Error: {}'.format(error))