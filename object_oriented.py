"""Exercises for Object-Oriented Programming chapter"""


# Vector Overloading
class Vector(object):
	"""Represents a vector in a multidimensional space"""

	def __init__(self, d):
		"""Creates a vector of d dimensions"""
		self._coords = [0] * d

	def __len__(self):
		"""Returns the dimension of the vector"""
		return len(self._coords)

	def __getitem__(self, j):
		"""Returns the jth coordinate of a vector"""
		return self._coords[j]

	def __setitem__(self, j, val):
		"""Sets jth coordinate to value val"""
		self._coords[j] = val

	def __add__(self, other):
		"""Returns the sum of two vectors"""
		if len(self) != len(other):  # relies on the __len__ method (Method Overloading)
			return ValueError('Dimensions must be equal')
		result = Vector(len(self))  # Initialize a vector of zeroes
		for j in range(len(self)):
			result[j] = self[j] + other[j]
		return result

	def __eq__(self, other):
		"""Return True if vector has same coordinates as other"""
		return self._coords == other._coords

	def __ne__(self, other):
		"""Return True if vector does not have same coordinates as other"""
		return not self == other

	def __str__(self):
		"""Return string representation of the vector"""
		return '<' + str(self._coords)[1:-1] + '>'  # Adapt list representation


class SequenceIterator:
	"""An iterator for any of Python's sequence types"""

	def __init__(self, sequence):
		"""Create an iterator for a given sequence"""
		self._seq = sequence  # Reference to underlying data
		self._k = -1  # Increments to 0 first call to next

	def __next__(self):
		"""Returns the next element else raise StopIteration Error"""
		self._k += 1  # Advance to next index
		if self._k < len(self._seq):
			return self._seq[self._k]  # Return the sequence item
		else:
			raise StopIteration()  # There are no more elements

	def __iter__(self):
		"""By convention an iterator must return itself as an iter"""
		return self


class Range:
	"""A class that mimics built-in range class."""

	def __init__(self, start, stop = None, step = 1):
		"""Initializes a Range instance with semantics similar to the built-in range class"""
		if step == 0:
			raise ValueError('Step cannot be 0')

		if stop is None:
			start, stop = 0, start  # Should be treated as range(0, n)

		# Calculate the effective length
		self._length = max(0, (stop - start + step - 1) // 2)

		# To support __getitem__ add start and step as instance variables
		self._start = start
		self._step = step

	def __len__(self):
		"""Return length of entries in the range"""
		return self._length

	def __getitem__(self, k):
		"""Return entry at index k (using standard interpretation if negative)"""
		if k < 0:
			k += len(self)  # Attempt to convert negative indices

		if not 0 <= k < self._length:
			raise IndexError('Index out of range')

		return self._start + k * self._step


class Progression:
	"""
	Iterator producing a generic progression
	Default iter produces the pattern 0,1,2,3...
	"""

	def __init__(self, start = 0):
		"""
		Initialize the current to the first value of the progression
		"""
		self._current = start

	def _advance(self):
		"""Updates current with new value. Override this in sub-classes for custom progression"""
		self._current += 1

	def __next__(self):
		"""Return the next element else raise StopIteration Error"""
		if self._current is None:
			raise StopIteration()
		else:
			answer = self._current
			self._advance()
			return answer

	def __iter__(self):
		"""By convention an iter must return itself"""
		return self

	def print_progression(self, n):
		"""Print the next n values of a progression"""
		print(' '.join(str(self.__next__()) for j in range(n)))


class ArithmeticProgression(Progression):
	"""Iterator producing arithmetic progression"""

	def __init__(self, increment = 1, start = 0):
		"""Initialize the iterator with 1 as the increment to be used starting from 0"""
		super().__init__(start)
		self._increment = increment

	def _advance(self):
		"""Update the current value by adding the fixed increment"""
		self._current += self._increment


class GeometricProgression(Progression):
	"""Iterator producing geometric progression"""

	def __init__(self, base = 2, start = 1):
		"""Initialize GeometricProgression with a base and start value"""
		super().__init__(start)
		self._base = base

	def _advance(self):
		"""Update the current value by multiplying the previous value with the base"""
		self._current *= self._base


class FibonacciProgression(Progression):
	"""Iterator producing fibonacci progression"""

	def __init__(self, first = 0, second = 1):
		"""Create a new fibonacci series"""
		super().__init__(first)
		self._prev = second - first

	def _advance(self):
		"""Update the current value by adding two previous values"""
		self._prev, self._current = self._current, self._current + self._prev


if __name__ == '__main__':
	print('Default Progression: ')
	Progression().print_progression(10)

	print('Arithmetic Progression with increment of 5')
	ArithmeticProgression(5).print_progression(10)

	print('Geometric Progression with base of 2')
	GeometricProgression(2).print_progression(10)

	print('Fibonacci Progression with start values of 4 and 6')
	FibonacciProgression(4, 6).print_progression(10)
