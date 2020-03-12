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

	# Let p be a position of a node in tree T. The depth of p is the number of ancestors of p excluding p itself.
	# If p is the root then the depth is obviously 0. Else it's depth can be calculated by adding 1 to the depth of
	# its parent and calling this recursively. The recursion base at consideration will be when the referenced
	# ancestor is the root.
	def depth(self, p):
		"""Returns number of levels separating Position p from the root"""
		if self.root() == p:
			return 0
		else:
			return 1 + self.depth(self.parent(p))

		# Running Time:
		# The running time of T.depth(p) for a position p is O(dp + 1) where dp denotes the depth of p in tree T

	# Height of a tree is also defined recursively:
	# If p is a leaf then height is 0. Otherwise, the height of p is one more than the maximum of the heights of p's
	# children. The height of a non-empty tree is equal to the the depths of its leaf positions.
	def _height1(self):  # Works in O(n^2) time
		"""Return the height of the Tree"""
		return max(self.depth(p) for p in self.positions() if self.is_leaf(p))

	def _height2(self, p):
		"""Return the height of the subtree rooted at Position P"""
		if self.is_leaf(p):
			return 0
		return 1 + max(self._height2(c) for c in self.children(p))


if __name__ == '__main__':
	rowIndex = 3
	triangle, prev = [], []
	for idx in range(1, rowIndex):
		if idx == 1:
			prev = [1]
		left = 0
		triangle.append(1)
		while left + 1 < len(prev):
			triangle.append(prev[left] + prev[left + 1])
			left += 1
		triangle.append(1)
		prev = triangle
	print(triangle)
