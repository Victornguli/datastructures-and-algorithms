""""
Dynamic Array in Python. This is similar to Python's List implementation, but not fully concise since Python's List
methods are actually implemented using C in Cython.
By Utilizing the concrete Array from C, a DynamicArray can shrink and expand dynamically to accommodate deletion and
addition of new elements. This low-level behaviour enables Lists in Python to extend C's concrete Array and add
Dynamic operations on top of it.
"""
import ctypes


class DynamicArray:
	"""Dynamic array similar to python's list"""

	def __init__(self):
		"""Create empty array"""
		self._n = 0  # Total number of elements in the array
		self._capacity = 1  # The capacity of the array
		self._A = self._make_array(self._capacity)  # Actual concrete array created using ctypes

	def __len__(self):
		"""Return the length of the array"""
		return self._n  # Allows for constant time lookup of an array's length

	def __getitem__(self, key):
		"""Retrieves an item from the array e.g array[0]"""
		if not 0 <= key < self._n:
			raise IndexError('Index Out of Range')
		return self._A[key]

	def __repr__(self):
		"""Returns the string representation of the dynamic array e.g str(array)"""
		return str([self._A[i] for i in range(self._n)])

	def __contains__(self, item):
		"""Returns True if item is found in array: Represented as item in array e.g item in array"""
		for idx in range(self._n):
			if self._A[idx] == item:
				return True
		return False

	def __add__(self, other):
		"""Concatenates second array to the first array e.g array + other"""
		new = DynamicArray()
		for k in range(self._n):
			new.append(self._A[k])
		for j in range(len(other)):
			new.append(other[j])
		return new

	def __reversed__(self):
		"""Returns an iterator over the reversed items of the array e.g for item in reversed(array)..."""
		for idx in range(self._n - 1, -1, -1):
			yield self._A[idx]

	def __delitem__(self, key):
		"""Deletes an item given its index"""
		if not (0 <= key < self._n):
			raise IndexError('Index Out of range!')
		for j in range(key, self._n - 1):
			self._A[j] = self._A[j + 1]
		self._A[self._n - 1] = None  # Optional since del performs garbage collection automatically,, I think...
		self._n -= 1

	def __iter__(self):
		"""Iterator magic function to enable the DynamicArray to be iteratable"""
		for idx in range(self._n):
			yield self._A[idx]

	def append(self, obj):
		"""Insert into the dynamic array an obj at the last index available"""
		if self._n == self._capacity:  # There isn't enough space
			self._resize(2 * self._capacity)
		self._A[self._n] = obj  # n is applicable as an index pointing to an index after the last element is there
		# are a total of n elements in an array with extra capacity.
		self._n += 1

	def _resize(self, c):
		"""Non-public utility method for resizing the dynamic array to a new capacity c"""
		B = self._make_array(c)
		for k in range(self._n):
			B[k] = self._A[k]
		self._A = B
		self._capacity = c

	@staticmethod
	def _make_array(c):
		"""Create a new Array object from Cython's ctypes"""
		return (c * ctypes.py_object)()

	def insert(self, k, value):
		"""Insert value at index k assuming that 0 <= k < n"""
		if self._n == self._capacity:
			self._resize(2 * self._capacity)
		for j in range(self._n, k, -1):  # Shift items right, starting with the rightmost up-to the index k
			self._A[j] = self._A[j - 1]
		self._A[k] = value
		self._n += 1

	def remove(self, value):
		"""Removes a value from the array """
		for k in range(self._n):
			if self._A[k] == value:  # Found a match. Loop over remaining items to shift them to the left
				for j in range(k, self._n - 1):
					self._A[j] = self._A[j + 1]  # Shift items to fill the removed item
				self._A[self._n - 1] = None  # Simple garbage collection.
				self._n -= 1
				return
		raise ValueError('Value not found')

	def count(self, value):
		"""Returns the count of an occurrence of a value in the array e.g list.count(val)"""
		count = 0
		for i in range(self._n):
			if self._A[i] == value:
				count += 1
		return count

	def index(self, value):
		"""Returns the index of a value within the array: similar to builtin array.index(val)"""
		for idx in range(self._n):
			if self._A[idx] == value:
				return idx
		raise ValueError('Value not found!')

	def reverse(self):
		"""Mutates the array elements into a reversed order"""
		left, right = 0, self._n - 1
		while left < right:
			self._A[left], self._A[right] = self._A[right], self._A[left]
			left += 1
			right -= 1
		return

	def pop(self, key = None):
		"""
		Removes and return an items at an index if self._n >= 1. Defaults to the last item
		"""
		if self._n < 1:
			raise IndexError('Pop from an empty Array')
		if key is not None and not 0 <= key < self._n:
			raise IndexError('Index Out of range')
		key = key if key is not None else self._n - 1
		val = self._A[key]
		if key == self._n - 1:  # Pop in constant time since this is the last element of the array
			val = self._A[key]
			self._A[key] = None
		else:  # Remove the element and shift the remaining right-side elements to the left.
			for j in range(key, self._n - 1):
				self._A[j] = self._A[j + 1]
			self._A[self._n - 1] = None
		self._n -= 1
		return val

	def extend(self, other):
		"""
		Adds all elements of another array to the end of the array e.g arr.extend(other)
		"""
		for item in other:
			self.append(item)


"""" Application of Python Sequence Types in Problems """


class GameEntry(object):
	"""Represents an entry of a list of high scores"""

	def __init__(self, name, score):
		self._name = name
		self._score = score

	def get_name(self):
		return self._name

	def get_score(self):
		return self._score

	def __str__(self):
		return '({0}, {1})'.format(self._name, self._score)


class HighScore(object):
	"""Fixed length sequence of high scores in non-decreasing order"""

	def __init__(self, capacity = 10):
		"""Initialize the score boar with a given capacity. Defaults to 10"""
		self._board = [None] * capacity
		self._n = 0

	def __getitem__(self, k):
		"""Return item at index k"""
		return self._board[k]

	def __str__(self):
		"""Return the string representation of the high score list"""
		return '\n'.join(str(self._board[j]) for j in range(self._n))

	def add(self, entry):
		"""Add a new entry to high scores"""
		score = entry.get_score()

		# Check if board is not full or score is greater than last entry in the board
		good = self._n < len(self._board) or self._board[-1].get_score < score

		if good:
			if self._n < len(self._board):
				self._n += 1
			pos = self._n - 1  # Actual count of high-scores currently on the board
			while pos > 0 and self._board[pos - 1].get_score() < score:
				self._board[pos] = self._board[pos - 1]
				pos -= 1
			self._board[pos] = entry


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


# Caesar's Cipher
class CaesarCipher:
	"""Caesar's Cipher implementation with an arbitrary character shift"""
	def __init__(self, shift):
		"""Construct a Caesar cipher using a given integer for shift rotation"""
		encoder = [None] * 26
		decoder = [None] * 26
		for k in range(26):
			encoder[k] = chr((k + shift) % 26 + ord('A'))
			decoder[k] = chr((k - shift) % 26 + ord('A'))
		self._forward = ''.join(encoder)
		self._backward = ''.join(decoder)

	def encrypt(self, message):
		"""Returns the string representation of the encrypted message"""
		return self._transform(message, self._forward)

	def decrypt(self, secret):
		"""Return decrypted message given decrypted secret"""
		return self._transform(secret, self._backward)

	@staticmethod
	def _transform(original, code):
		"""Utility to perform transformation given a certain string"""
		msg = list(original)
		for k in range(len(msg)):
			if msg[k].isupper():
				j = ord(msg[k]) - ord('A')
				msg[k] = code[j]
		return ''.join(msg)


if __name__ == '__main__':
	# print(insertion_sort([5, 1, 4, 3, 2]))
	message = 'THE EAGLE HAS LANDED'
	enc = CaesarCipher(5)
	coded = enc.encrypt(message)
	print('SECRET: ', coded)
	decoded = enc.decrypt(coded)
	print('DECODED: ', decoded)
	simple_list = DynamicArray()
	other_list = DynamicArray()
	for i in range(6, 11):
		other_list.append(i)
	for i in range(1, 6):
		simple_list.append(i)
	print(simple_list)  # [1, 2, 3, 4, 5]
	print(other_list)  # [6, 7, 8, 9, 10]
	print(simple_list + other_list)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] => Operator overload using __add__ magic method
	print(simple_list.pop(0))
	print(simple_list)
	simple_list.extend(other_list)
	print(simple_list)
