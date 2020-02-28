"""Linked List ADT"""


class Empty(Exception):
	"""Error class to be raised when an ADT is empty"""
	pass


class LinkedStack:
	"""LIFO Stack implementation using linked list for storage"""

	class _Node:
		"""A non-public class to store a singly linked node"""
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
			raise Empty('Stack Underflow')
		value = self._head._element
		self._head = self._head._next  # Override the head value to contain the current head's next node
		self._size -= 1
		return value


class LinkedQueue:
	"""FIFO Implementation using a linked list as storage"""

	class _Node:
		"""A non-public class for storing a single node"""
		def __init__(self, element, next):
			"""Initialize a new node"""
			self._element = element
			self._next = next

	def __init__(self):
		"""Initialize a new Queue"""
		self._head = None
		self._tail = None
		self._size = 0

	def __len__(self):
		"""Returns number of elements in the queue"""
		return self._size

	def is_empty(self):
		"""Return True if the queue is empty"""
		return self._size == 0

	def first(self):
		"""Return(But do not remove) the element at the front of the queue"""
		if self.is_empty():
			raise Empty('Queue is empty')
		return self._head._element

	def enqueue(self, e):
		"""Add an element to the back of the queue"""
		newest = self._Node(e, None)  # Initialize the next of the node as None since it will be the tail anyways
		if self.is_empty():
			self._head = newest
		else:
			self._tail._next = newest  # Update the current tail node to reference new tail in its next
		self._tail = newest
		self._size += 1

	def dequeue(self):
		"""Remove the element at the front of the queue"""
		if self.is_empty():
			raise Empty('Queue is empty')
		value = self._head._element
		self._head = self._head._next  # Set the head the the next Node. If there is not next node, head becomes None
		self._size -= 1
		if self.is_empty():  # If the queue is empty, then for sanity the _tail is set to point to None
			self._tail = None
		return value


class CircularQueue:
	"""Queue implementation using circularly linked list for storage"""

	class _Node:
		"""Non-public class for storing a Node in a linked list"""

		def __init__(self, element, next):
			"""Initialize a new node"""
			self._element = element
			self._next = next

	def __init__(self):
		"""Initialize a new queue"""
		self._tail = None
		self._size = 0

	def __len__(self):
		"""Return current size of the queue"""
		return self._size

	def is_empty(self):
		"""Return True if queue is empty"""
		return self._size == 0

	def first(self):
		"""Return(But do Not Remove) the first element in the queue(Queue  - Front)"""
		if self.is_empty():
			raise Empty('Queue is empty')
		head = self._tail._next
		return head._element

	def dequeue(self):
		"""Remove the first element (FIFO)"""
		if self.is_empty():
			raise Empty('Queue is empty')
		head = self._tail._next
		if self._size == 1:
			self._tail = None
		else:
			self._tail._next = head._next
		self._size -= 1
		return head._element

	def enqueue(self, e):
		"""Add an element at the end of the queue"""
		newest = self._Node(e, None)
		if self.is_empty():
			newest._next = newest
		else:
			newest._next = self._tail._next
			self._tail._next = newest
		self._tail = newest
		self._size += 1

	def rotate(self):
		"""Rotate front element to the back of the queue"""
		if self._size > 0:
			self._tail = self._tail._next


class _DoublyLinkedBase:
	"""A base class providing a doubly linked list representation"""

	class _Node:
		"""A non-public class for storing a node in a doubly linked list"""
		__slots__ = '_element', '_prev', '_next'  # Streamline memory

		def __init__(self, element, prev, next):
			"""Create a new node """
			self._element = element
			self._prev = prev
			self._next = next

	def __init__(self):
		"""Creates an empty list"""
		# _header and _trailer are the two sentinel nodes at the start and the end of the linked list
		self._header = self._Node(None, None, None)
		self._trailer = self._Node(None, None, None)
		self._header._prev = self._trailer
		self._trailer._next = self._header
		self._size = 0  # Initial size is 0: _header and _trailer are not acknowledged as real elements of the list

	def __len__(self):
		"""Returns the length of the list"""
		return self._size

	def is_empty(self):
		"""Returns True if the list is empty"""
		return self._size == 0

	def _insert_between(self, e, predecessor, successor):
		"""
		Add a new node between two existing nodes, the predecessor and a successor, and return the new node
		"""
		newest = self._Node(e, predecessor, successor)
		predecessor._next = newest
		successor._prev = newest
		self._size += 1
		return newest

	def _delete_node(self, node):
		"""Delete a non-sentinel node(neither the header or the trailer) from the list and return its element"""
		predecessor = node._prev
		successor = node._next
		successor._prev = predecessor
		predecessor._next = successor
		self._size -= 1
		# Successfully unlinked the node
		element = node._element
		node._next = node._element = node._element = None  # Garbage collect/cleanup the unliked node
		return element




if __name__ == '__main__':
	ls = LinkedStack()
	for i in range(5):
		ls.push(i)
	print(ls.top)  # Current head
	print(ls.pop())
