"""Exercises from Primer chapter"""
import math
import random


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


def reverse_list(seq):
	"""
	C-1.13 Write a pseudo-code description of a function that reverses a list of n
	integers, so that the numbers are listed in the opposite order than they
	were before, and compare this method to an equivalent Python function
	for doing the same thing.
	"""
	return seq[::-1]


def odd_distinct_values_sum(values):
	"""
	C-1.14 Write a short Python function that takes a sequence of integer values and
	determines if there is a distinct pair of numbers in the sequence whose
	product is odd.
	"""
	for i in values:
		for j in values:
			if i != j and (i * j) % 2 != 0:
				return True
	return False


def distinct_values(values):
	"""
	C-1.15 Write a Python function that takes a sequence of numbers and determines
	if all the numbers are different from each other (that is, they are distinct).
	"""
	return values == list(set(values))
	# Alternative approach would be the following non-reachable block:
	distinct = []
	for i in values:
		if i in distinct:
			return False
		distinct.append(i)
	return True


def list_comprehension_2():
	"""
	C-1.18 Demonstrate how to use Python’s list comprehension syntax to produce
	the list [0, 2, 6, 12, 20, 30, 42, 56, 72, 90].
	"""
	return [i*(i+1) for i in range(0, 10)]


def alphabet_gen():
	"""
	C-1.19 Demonstrate how to use Python’s list comprehension syntax to produce
	the list [ a , b , c , ..., z ], but without having to type all 26 such
	characters literally
	"""
	return [chr(i) for i in range(65, 91)]


def shuffle_fun(data):
	"""
	C-1.20 Python’s random module includes a function shuffle(data) that accepts a
	list of elements and randomly reorders the elements so that each possible order occurs with equal probability.
	The random module includes a more basic function randint(a, b) that returns a uniformly random integer
	from a to b (including both endpoints). Using only the randint function,
	implement your own version of the shuffle function.
	"""
	for i in range(len(data)):
		j = random.randint(0, len(data) - 1)
		data[i], data[j] = data[i], data[j]  # Swap value at index i with value at the randomly generated index j
	return data


def line_reader():
	"""
	C-1.21 Write a Python program that repeatedly reads lines from standard input
	until an EOFError is raised, and then outputs those lines in reverse order
	(a user can indicate end of input by typing ctrl-D).
	"""
	input_lines = []
	while True:
		try:
			input_command = input('Type in something cool. Press CTRL-D to terminate: ')
			input_lines.append(input_command)
		except EOFError:
			print('\n Uh-oh.. Seems you have chosen death...')
			for line in input_lines:
				print(line)
			break


def array_product(a, b, n):
	"""
	C-1.22 Write a short Python program that takes two arrays a and b of length n
	storing int values, and returns the dot product of a and b. That is, it returns
	an array c of length n such that c[i] = a[i] · b[i], for i = 0,...,n−1.
	"""
	c = []
	for i in range(n):
		c[i] = a[i] * b[i]
	return c


def index_out_of_bounds():
	"""
	C-1.23 Give an example of a Python code fragment that attempts to write an element to a list based on an index that
	may be out of bounds. If that index is out of bounds, the program should catch the exception that results, and
	print the following error message:
	“Don’t try buffer overflow attacks in Python!”
	"""
	my_list = [1,2,3,4,5]
	try:
		print(my_list[len(my_list)])
	except IndexError:
		print("Don’t try buffer overflow attacks in Python!")


