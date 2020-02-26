"""Linked List ADT"""


class Empty(Exception):
	"""Error class to be raised when an ADT is empty"""
	pass


class LinkedStack:
	"""LIFO Stack implementation using linked list for storage"""

	class _Node:
		"""A non-public class to store a singly linked list"""
		__slots__ = '_element', '_next'

		def __init__(self, element, next):
			self._element = element
			self._next = next

		def __repr__(self):
			return str([self._element, self._next._element if self._next is not None else None])

	def __init__(self):
		"""Initialize an empty stack"""
		self._head = None
		self._size = 0

	def __len__(self):
		"""Return the length of the linked list"""
		return self._size

	def is_empty(self):
		"""Return True if the linked- list is empty"""
		return self._size == 0

	def push(self, e):
		"""Inserts a new node with element e to the linked list at the head position"""
		self._head = self._Node(e, self._head)
		self._size += 1

	def top(self):
		"""Returns the top element of the stack(The head of the linked-list)"""
		if self.is_empty():
			raise Empty('Stack is empty')
		return self._head._element

	def pop(self):
		"""Remove and return the element at the top of the stack(LIFO)"""
		if self.is_empty():
			raise Empty('Stack is empty')
		value = self._head._element
		self._head = self._head._next  # Override the head value to contain the current head's next node
		self._size -= 1
		return value


if __name__ == '__main__':
	ls = LinkedStack()
	for i in range(5):
		ls.push(i)
	print(ls.top)  # Current head
	print(ls.pop())
