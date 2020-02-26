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

	def __repr__(self):
		"""Returns representational str of the array"""
		return str(self._data)

	def is_empty(self):
		return self._data == []

	def push(self, val):
		"""Adds a value to the top of the stack"""
		return self._data.append(val)

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
			stack.append(c)
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
		k = raw.find('>', j+1)  # Search for the closing tag
		if k == -1:
			return False  # Closing Tag not Found
		tag = raw[j+1:k]  # The html tag e.g title or /title
		if not tag.startswith('/'):
			stack.append(tag)
		else:
			if stack.is_empty():
				return False  # Empty stack yet a closing tag is found means the html tag is not valid
			if tag[1:] != stack.pop():  # Access the tag from index 1 to remove / since its a closing tag
				return False  # The closing tag does not match the topmost one in the stack(Should be its opening)
		j = raw.find('<', k+1)  # j(opening tag) is now searched for from the index k+1
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


if __name__ == '__main__':
	s = ArrayStack()
	t = ArrayStack()
	for i in range(5):
		s.push(i)
	print(s)
	print(transfer(s, t))
