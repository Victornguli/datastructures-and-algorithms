""""List (Array) datastructure in Python"""
import ctypes


class DynamicArray:
	"""Dynamic array similar to python's list"""

	def __init__(self):
		"""Create empty array"""
		self._n = 0  # Total number of elements in the array
		self._capacity = 1  # The capacity of the array
		self._A = self._make_array(self._capacity)

	def __len__(self):
		"""Return the length of the array"""
		return self._n

	def __getitem__(self, item):
		if not 0 <= item < self._n:
			raise IndexError('Index Out of Range')
		return self._A[item]

	def __repr__(self):
		"""Returns the string representation of the dynamic array"""
		return str([self._A[i] for i in range(len(self))])

	def append(self, obj):
		"""Insert into the dynamic array an obj at the last index available"""
		if self._n == self._capacity:  # There isn't enough space
			self._resize(2 * self._capacity)
		self._A[self._n] = obj  # n is applicable as an index pointing to an index after the last element is there
		# are a total of n elements in an array with extra capacity.
		self._n += 1

	def _resize(self, c):
		"""Resize the dynamic array with a capacity c"""
		B = self._make_array(c)
		for k in range(self._n):
			B[k] = self._A[k]
		self._A = B
		self._capacity = c

	def _make_array(self, c):
		"""Create a new Array object"""
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
	print(insertion_sort([5, 1, 4, 3, 2]))
	message = 'THE EAGLE HAS LANDED'
	enc = CaesarCipher(5)
	coded = enc.encrypt(message)
	print('SECRET: ', coded)
	decoded = enc.decrypt(coded)
	print('DECODED: ', decoded)
	simple_list = DynamicArray()
	for i in range(5):
		simple_list.append(i)
	print(simple_list)
