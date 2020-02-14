"""Exercises for Object-Oriented Programming chapter"""


# Vector Overloading
class Vector(object):
	"""Represents a vector in a multidimensional space"""

	def __init__(self, d):
		"""Creates a vector of d dimensions"""
		self._coords = [0] * d

	def get_coords(self):
		"""Return coordinates of the vector"""
		return self._coords

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
		return self._coords == other.get_coords()

	def __ne__(self, other):
		"""Return True if vector does not have same coordinates as other"""
		return not self == other

	def __str__(self):
		"""Return string representation of the vector"""
		return '<' + str(self._coords)[1:-1] + '>'  # Adapt list representation

