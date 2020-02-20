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


if __name__ == '__main__':
	# print(factorial(5))
	# draw_ruler(3, 3)
	print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 11, 0, 9))
