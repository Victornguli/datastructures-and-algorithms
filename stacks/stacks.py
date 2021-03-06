"""Stacks and Queues"""


class Empty(Exception):
	"""Empty stack error"""
	pass


class Full(Exception):
	"""Push operation on a full stack :)"""
	pass


class ArrayStack:
	"""LIFO Implementation based on list storage"""

	def __init__(self, max_len = None):
		self._max_len = max_len
		self._data = []
		self._n = 0
		if self._max_len:
			self._data = [None] * self._max_len

	def __len__(self):
		if self._max_len is not None:
			return self._n
		return len(self._data)

	def __repr__(self):
		"""Returns representational str of the array"""
		if self._max_len is not None:
			return str(self._data[0:self._n])
		return str(self._data)

	def is_empty(self):
		if self._max_len is not None:
			return self._n == 0
		return self._data == []

	def push(self, val):
		"""Adds a value to the top of the stack"""
		if self._max_len is not None and self._n == self._max_len:
			raise Full('Stack is full')
		# Append element then increment _n if max_len is specified.
		if self._max_len is not None:
			self._data[self._n] = val
			self._n += 1
			return
		else:
			return self._data.append(val)

	def top(self):
		"""Return the top item. Raise Empty error if topmost item in stack is not found"""
		if self.is_empty():
			raise Empty('Stack is empty')
		if self._max_len is not None:
			return self._data[self._n - 1]
		return self._data[-1]

	def pop(self):
		"""Remove the topmost item in the stack"""
		if self.is_empty():
			raise Empty('Stack is empty')
		if self._max_len is not None:
			val = self._data[self._n - 1]
			self._data[self._n - 1] = None
			self._n -= 1
			return val
		return self._data.pop()


def is_matched(expr):
	"""
	Code Fragment 6.4: Function for matching delimiters in an arithmetic expression.
	Return True if all delimiters are properly match; False otherwise.
	"""
	lefty = '({['
	righty = ')}]'
	stack = ArrayStack()
	for c in expr:
		if c in lefty:
			stack.push(c)
		elif c in righty:
			if stack.is_empty():  # If c in left then it must be in right to be a matching pair i.e () / {} / []
				return False
			if righty.index(c) != lefty.index(stack.pop()):  # Confirm if the index of c is same as the popped value
				# in the stack in left side. If they don't match return False
				return False
	return stack.is_empty()  # Ensure that search is complete


def is_matched_html(raw):
	"""Returns True if all HTML tags are a proper match; False otherwise"""
	stack = ArrayStack()
	j = raw.find('<')  # Find first opening tag
	while j != -1:  # Confirm if there is an HTML Tag
		k = raw.find('>', j + 1)  # Search for the closing tag
		if k == -1:
			return False  # Closing Tag not Found
		tag = raw[j + 1:k]  # The html tag e.g title or /title
		if not tag.startswith('/'):
			stack.push(tag)
		else:
			if stack.is_empty():
				return False  # Empty stack yet a closing tag is found means the html tag is not valid
			if tag[1:] != stack.pop():  # Access the tag from index 1 to remove / since its a closing tag
				return False  # The closing tag does not match the topmost one in the stack(Should be its opening)
		j = raw.find('<', k + 1)  # j(opening tag) is now searched for from the index k+1
	return stack.is_empty()  # If the stack is empty all tags have matches: Note how stack.pop() is used during


# comparison to make sure any matching tag in the stack is removed.


def transfer(S, T):
	"""
	Implement a function with signature transfer(S, T) that transfers all elements from stack S onto stack T, so that
	the element that starts at the top of S is the first to be inserted onto T, and the element at the bottom of S
	ends up at the top of T.
	"""
	if S.is_empty():
		raise Empty('Empty Stack')
	# for i in range(len(S)):
	# 	T.push(S.pop())
	# OR :
	while not S.is_empty():
		T.push(S.pop())

	return (S, T)


def pop_recurs(stack):
	"""
	Give a recursive method for removing all the elements from a stack
	"""
	if stack.is_empty():
		return stack
	else:
		stack.pop()
		return pop_recurs(stack)


def reverse_list_with_stack(data):
	"""
	Implement a function that reverses a list of elements by pushing them onto
	a stack in one order, and writing them back to the list in reversed order
	"""
	stack = ArrayStack()
	for elem in data:
		stack.push(elem)
	idx = 0
	while not stack.is_empty():
		data[idx] = stack.pop()
		idx += 1
	return data


if __name__ == '__main__':
	s = ArrayStack(max_len = 5)
	assert s.is_empty() is True, "Should be initialed as empty"
	t = ArrayStack()
	for i in range(5):
		s.push(i)
	# pop_recurs(s)
	# assert len(s) == 0
	print(s)
	assert s.top() == 4, "Top element in the stack should be 4"
	transfer(s, t)
	assert len(s) is 0, "Stack S should be emptied"
	assert len(t) is 5, "Stack T should hold the copied elements from S"
	assert t.top() == 0, "Top stack element should now be 0"
	# print(reverse_list_with_stack([1, 2, 3, 4, 5]))
