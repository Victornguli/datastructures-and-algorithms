"""Collection of recursive algorithms"""
from fractions import Fraction


# Factorial function
def factorial(n):
	if n == 0:
		return 1
	else:
		return n * factorial(n - 1)


# Drawing English ruler with ticks
def draw_line(tick_length, tick_label = ''):
	"""Draw one line with  a given tick length(followed by an optional label"""
	line = '-' * tick_length
	if tick_label:
		line += ' ' + tick_label
	print(line)


def draw_interval(center_length):
	"""Draw interval based upon a central tick length"""
	if center_length > 0:
		draw_interval(center_length - 1)
		draw_line(center_length)
		draw_interval(center_length - 1)


def draw_ruler(num_inches, major_length):
	"""Draw an English ruler with a given number of inches, major tick length"""
	draw_line(major_length, '0')
	for j in range(1, 1 + num_inches):
		draw_interval(major_length - 1)
		draw_line(major_length, str(j))


# Binary search algorithm recursively
def binary_search(data, target, low, high):
	if low >= high:
		return False
	mid = (low + high) // 2
	if target == data[mid]:
		return True
	elif target < data[mid]:
		return binary_search(data, target, low, mid - 1)
	else:
		return binary_search(data, target, mid + 1, high)


import os


# File traversals
def path_size(path):
	"""Return number of bytes used by a folder and its sub-folders"""
	size = os.path.getsize(path)
	if os.path.isdir(path):
		for filename in os.listdir(path):
			child_path = os.path.join(path, filename)
			size += path_size(child_path)
	print('{0:<7}'.format(size), path)
	return size


# Linear recursive sum
def linear_sum(data, n):
	if n == 0:
		return 0
	else:
		return linear_sum(data, n - 1) + data[n - 1]


# Linear reverse list
def linear_reverse(data, start, stop):
	if start < stop - 1:
		data[start], data[stop - 1] = data[stop - 1], data[start]
		linear_reverse(data, start + 1, stop - 1)
	return data


# Power calculation recursively
def power(x, n):
	if n == 0:
		return 1
	return x * power(x, n - 1)


# Improvement on the above power function. Uses repeated squaring Algorithm for odd and even numbers
def power_imp(x, n):
	if n == 0:
		return 1
	partial = power_imp(x, n // 2)
	result = partial * partial
	if n % 2 == 1:
		result *= x
	return result


# C-4.9 Write a short recursive Python function that finds the minimum and maximum values in a
# sequence without using any loops.
def min_recur(seq, n):
	"""Finds min numbers in a sequence recursively"""
	if n == 1:
		return seq[0]
	else:
		return min(seq[n - 1], min_recur(seq, n - 1))


def max_recur(seq, n):
	"""Finds max numbers in a sequence recursively"""
	if n == 1:
		return seq[0]
	else:
		return max(seq[n - 1], max_recur(seq, n - 1))


# C-4.10 Describe a recursive algorithm to compute the integer part of the base-two
# logarithm of n using only addition and integer division.
def base_two(n):
	if n <= 2:
		return 1
	else:
		return base_two(n // 2) + 1


# C-4.12 Give a recursive algorithm to compute the product of two positive integers,
# m and n, using only addition and subtraction.
def recursive_product(m, n):
	if n == 1:
		return m
	else:
		return recursive_product(m, n - 1) + m


# C-4.18 Use recursion to write a Python function for determining if a string s has
# more vowels than consonants
def has_more_vowels(s, idx, vowel_count, cons_count):
	vowels = 'aeiou'
	if idx == len(s):
		return vowel_count >= cons_count
	if s[idx] in vowels:
		return has_more_vowels(s, idx + 1, vowel_count + 1, cons_count)
	else:
		return has_more_vowels(s, idx + 1, vowel_count, cons_count + 1)


# R-4.6 Describe a recursive function for computing the nth Harmonic number, Hn = ∑ni=1 1/i.
def nth_harmonic_number(n):
	if n == 1:
		return Fraction(1, 1)  # Basically since 1/1 == 1
	else:
		return Fraction(1, n) + Fraction(nth_harmonic_number(n - 1))


def good_fib(n):
	"""Efficient fibonacci using recursion. Avoids exponential number of recursive function calls"""
	if n <= 1:
		return n, 0
	else:
		a, b = good_fib(n - 1)
		return a + b, a


def recursive_sum(elements, n):
	"""Sums a list of elements recursively"""
	if n == 0:  # Base case when the length of elements is zero
		return 0
	else:
		return elements[n - 1] + recursive_sum(elements, n - 1)


def binary_sum(s, start, stop):
	if start >= stop:
		return 0
	elif start == stop - 1:
		print(s[start])
		return s[start]
	else:
		print(s[start:stop])
		mid = (start + stop) // 2
		return binary_sum(s, start, mid) + binary_sum(s, mid, stop)


# C-4.11 Describe an efficient recursive function for solving the element uniqueness problem, which runs in time that
# is at most O(n2) in the worst case without using sorting.
def has_duplicates(data):
	print(data)
	if len(data) <= 1:
		return False
	if data[0] == data[1]:
		return True
	if has_duplicates([data[0]] + data[2:]):
		return True
	if has_duplicates(data[1:]):
		return True
	return False


if __name__ == '__main__':
	# print(factorial(5))
	# draw_ruler(3, 3)
	# print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 11, 0, 9))
	# print(linear_sum([1, 2, 3, 4, 5], 3))
	# print(linear_reverse([1, 2, 3, 4, 5], 0, 5))
	# print(power_imp(2, 5))
	# print(min_recur([1,2,3,4,5,6], 6))
	# print(recursive_product(1000, 35))
	# print(base_two(128))
	# print(has_more_vowels('viictoria', 0, 0, 0))
	# draw_ruler(2, 4)
	# print(binary_sum([1, 2, 3, 4, 5], 0, 5))
	# print(nth_harmonic_number(5))
	print(has_duplicates(['a', 'b', 'c', 'd']))
