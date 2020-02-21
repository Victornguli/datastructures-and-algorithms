"""Collection of recursive algorithms"""


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


# Binary search
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
	print(n)
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
	return x * power(x, n-1)


# Improved power algorithm
def power_imp(x, n):
	if n == 0:
		return 1
	partial = power_imp(x, n // 2)
	result = partial * partial
	if n % 2 == 1:
		result *= x
	return result


if __name__ == '__main__':
	# print(factorial(5))
	# draw_ruler(3, 3)
	# print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 11, 0, 9))
	# print(linear_sum([1, 2, 3, 4, 5], 3))
	# print(linear_reverse([1, 2, 3, 4, 5], 0, 5))
	print(power_imp(2, 5))