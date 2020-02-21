""""List (Array) datastructure in Python"""
import ctypes


class DynamicArray:
	"""Dynamic array similar to python's list"""

	def __init__(self):
		"""Create empty array"""
		self._n = 0
		self._capacity = 1
		self._A = self._make_array(self._capacity)

	def __len__(self):
		return self._n

	def __getitem__(self, item):
		if not 0 <= item < self._n:
			raise IndexError('Index Out of Range')
		return self._A[item]

	def append(self, obj):
		if self._n == self._capacity:  # There isn't enough space
			self._resize(2 * self._capacity)
		self._A[self._n] = obj
		self._n += 1

	def _resize(self, c):
		B = self._make_array(c)
		for k in range(self._n):
			B[k] = self._A[k]
		self._A = B
		self._capacity = c

	def _make_array(self, c):
		return (c * ctypes.py_object)()

	def insert(self, k, value):
		"""Insert value at index k assuming that 0 <= k <= n"""
		if self._n == self._capacity:
			self._resize(2 * self._capacity)
		for j in range(self._n, k, -1):  # Shift items right, starting with the rightmost up-to the index k
			self._A[j] = self._A[j - 1]
		self._A[k] = value
		self._n += 1

	def remove(self, value):
		for k in range(self._n):
			if self._A[k] == value:  # Found a match. Loop over remaining items to shift them to the left
				for j in range(k, self._n - 1):
					self._A[j] = self._A[j + 1]  # Shift items to fill the removed item
				self._A[self._n - 1] = None  # Simple garbage collection.
				self._n -= 1
				return
		raise ValueError('Value not found')

# def __str__(self):
# 	"""Return the string representation of the Array"""
# 	# res = ''
# 	return str(self)


# Sorting Sequences
# Insertion Sort
def insertion_sort(data):
	"""Insertion sort Algorithm"""
	for i in range(len(data)):
		curr = data[i]
		j = i
		while j > 0 and data[j - 1] > curr:
			data[j] = data[j - 1]
			j -= 1
		data[j] = curr
	return data


if __name__ == '__main__':
	print(insertion_sort([5, 2, 6, 65, 22, 35, 56, 1, 3, 45, 6, 7]))
