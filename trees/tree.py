"""Abstract Base Class for a Tree ADT"""


class Tree:
	"""Abstract base class representing a Tree ADT"""

	# Position Class
	class Position:
		"""An abstraction representing the location of one element"""

		def element(self):
			"""Return the element returned in this Position"""
			raise NotImplementedError('Must be implemented by subclass')

		def __eq__(self, other):
			"""Return true if other Position represents the same location"""
			raise NotImplementedError('Must be implemented by subclass')

		def __ne__(self, other):
			"""Return True if other Position does not represent the same location"""
			return not(self == other)  # Opposite of __eq__

	# Abstract methods that the concrete subclasses must implement
	def root(self):
		"""Return the Position representing the tree's root(Or None if empty)"""
		raise NotImplementedError('Must be implemented by subclass')

	def parent(self, p):
		"""Return the position representing p's parent(Or None if p is root)"""
		raise NotImplementedError('Must be implemented by subclass')

	def num_children(self, p):
		"""Return the number of children Position p has"""
		raise NotImplementedError('Must be implemented by subclass')

	def children(self, p):
		"""Generate an iterative representing the children of Position P"""
		raise NotImplementedError('Must be implemented by subclass')

	def __len__(self):
		"""Return the total number of elements in Tree"""
		raise NotImplementedError('Must be implemented by subclass')

	# Concrete methods

	def is_root(self, p):
		"""Return True if Position p represents the root of the tree"""
		return self.root() == p

	def is_leaf(self, p):
		"""Return True if Position p is a leaf(p does not contain any child)"""
		return self.num_children(p) == 0

	def is_empty(self):
		"""Return True if the tree is empty"""
		return len(self) == 0
