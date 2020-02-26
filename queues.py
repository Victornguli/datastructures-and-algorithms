"""The queue Abstract Data Structure"""
from typing import List


class Empty(Exception):
	"""Empty queue error"""
	pass


class Queue:
	"""Queue FIFO Implementation using underlying python list storage"""
	DEFAULT_CAPACITY = 10

	def __init__(self,):
		"""Create an empty queue instance"""
		self._data = [None] * Queue.DEFAULT_CAPACITY
		self._front = 0
		self._size = 0

	def __len__(self):
		"""Return the actual length of contents inside the queue"""
		return self._size

	def is_empty(self):
		"""Return True if the queue is empty"""
		return self._size == 0

	def first(self):
		"""Return (Does not Remove) the first element in-front of the queue"""
		if self.is_empty():
			raise Empty('Queue is empty!')
		return self._data[self._front]

	def dequeue(self):
		"""Remove and return the first element in the queue
		Raise Empty Error if queue is empty
		"""
		if self.is_empty():
			raise Empty('Empty queue')
		front = self._data[self._front]
		self._data[self._front] = None  # Assign new empty index to None
		self._front = (self._front + 1) % len(self._data)  # Point the new front index by applying  n = (n+1) % len
		# for the circular array semantics
		self._size -= 1
		if 0 < self._size < len(self._data) // 4:
			self._resize(len(self._data) // 2)
		return front

	def enqueue(self, element):
		"""Insert an element at the end of a queue"""
		if len(self._data) == self._size:
			# Double size since there is no enough space for a new element
			self._resize(2*len(self._data))  # Double array size
			avail = (self._front + self._size) % len(self._data)
			self._data[avail] = element
			self._size += 1

	def _resize(self, cap):
		"""Resize to a new list of capacity  => len(self)"""
		old = self._data
		self._data = [None] * cap  # Create the new list with the appropriate capacity
		walk = self._front  # First element index
		for k in range(self._size):  # Only consider the existing elements since actual size => self._size
			self._data[k] = old[walk]     # Append elements in new _data from old data shifting their indices
			walk = (walk + 1) % len(old)  # Use old size as modulus
		self._front = 0  # Front has been re-aligned
