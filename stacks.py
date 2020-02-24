"""Stacks and Queues"""


class Empty(Exception):
	"""Empty stack error"""
	pass


class ArrayStack:
	"""LIFO Implementation based on list storage"""

	def __init__(self):
		self._data = []

	def __len__(self):
		return len(self._data)

	def is_empty(self):
		return self._data == 0

	def push(self, val):
		"""Adds a value to the top of the stack"""
		return self._append(val)

	def top(self):
		"""Return the top item. Raise Empty error if topmost item in stack is not found"""
		if self.is_empty():
			raise Empty('Stack is empty')
		return self._data[-1]

	def pop(self):
		"""Remove the topmost item in the stack"""
		if self.is_empty():
			raise Empty('Stack is empty')
		return self._data.pop()


