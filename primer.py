"""Exercises from Primer chapter"""
import math


def is_multiple(n, m):
	"""
	R-1.1 Write a short Python function, is multiple(n, m), that takes two integer
	values and returns True if n is a multiple of m, that is, n = mi for some
	integer i, and False otherwise.
	"""
	return True if n % m == 0 else False


def is_even(k):
	"""
	R-1.2 Write a short Python function, is even(k), that takes an integer value and
	returns True if k is even, and False otherwise. However, your function
	cannot use the multiplication, modulo, or division operators.
	"""
	minimum = math.inf
	maximum = -math.inf
	for i in k:
		if i > maximum:
			maximum = i
		if i < minimum:
			minimum = i
	return minimum, maximum


def sum_of_squares(n):
	"""
	R-1.4 Write a short Python function that takes a positive integer n and returns
	the sum of the squares of all the positive integers smaller than n
	"""
	sum_sq = 0
	for i in range(1, n):
		sum_sq += i * i
	return sum_sq


def sum_comprehension(n):
	"""
	R-1.5 Give a single command that computes the sum from Exercise R-1.4, relying on Python’s comprehension syntax and
	the built-in sum function
	"""
	return sum(i*i for i in n)


def sum_odd(n):
	"""
	R-1.6 Write a short Python function that takes a positive integer n and returns
	the sum of the squares of all the odd positive integers smaller than n
	"""
	for i in range(1, n):
		return sum(i*i for i in n if i % 2 != 0)


# R-1.9 What parameters should be sent to the range constructor, to produce a
# range with values 50, 60, 70, 80?
# range(50, 90, 10)
def range_1():
	"""
	Implementation of the above range generator
	"""
	for i in range(50, 90, 10):
		print(i)  # Prints 50, 60, 70, 80


# R-1.10 What parameters should be sent to the range constructor, to produce a
# range with values 8, 6, 4, 2, 0, −2, −4, −6, −8?
# range(8, -10, -2)
def range_2():
	"""
	Implementation of the above range generator
	"""
	for i in range(8, -10, -2):
		print(i)  # Prints 8, 6, 4, 2, 0, -2, -4, -6, -8


def list_comprehension():
	"""
	R-1.11 Demonstrate how to use Python’s list comprehension syntax to produce
	the list [1, 2, 4, 8, 16, 32, 64, 128, 256].
	"""
	return [2 ** i for i in range(9)]


