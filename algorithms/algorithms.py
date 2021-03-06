"""Analysis of Algorithms and Algorithmic complexities"""


# Asymptotic analysis

# Proposition 3.7: The algorithm, find max, for computing the maximum element of a list of n numbers, runs in O(n) time.
def find_max(data):
	"""Find the maximum element from a non-empty python list"""
	biggest = data[0]  # 0(1) time
	for val in data:  # 0(n) -> dependent on the length of the list
		if val > biggest:
			biggest = val
	return biggest


# Prefix averages 1 on 0(n2)
def prefix_average1(input_list):
	"""Return a list such that, for all j , A[j] equals average of S[0], ... S[j] """
	n = len(input_list)
	prefix_avg = [0] * n
	for j in range(n):
		total = 0
		for i in range(j + 1):
			total += input_list[i]
		prefix_avg[j] = total / (j + 1)
	return prefix_avg


# 0(n2)
def prefix_avg2(input_list):
	""""""
	n = len(input_list)  # Constant 0(1)
	prefix_avg = [0] * n  # Linear 0(n)
	for j in range(n):  # 0(n) too for loop computation
		prefix_avg[j] = sum(input_list[0:j + 1]) / (j + 1)  # The statement input_list[0:j+1] takes 0(j+1) therefore
	# 0(n) too
	return prefix_avg


# Linear 0(n)
def prefix_3(input_list):
	n = len(input_list)
	prefix_avg = [0] * n
	total = 0
	for j in range(n):
		total += input_list[j]
		prefix_avg[j] = total / (j + 1)
	return prefix_avg


# Three way Disjointness
def disjoint(a, b, c):
	"""Return True if there is no element common to all three arrays."""
	for i in range(a):
		for j in range(b):
			for k in range(c):
				if a == b == c:
					return False
	return True


# An improvement on the above 0(n3) approach is realising that you only need to check i and j against j if they match
def disjoint_2(a, b, c):
	"""Return True if there is no element common to all three arrays."""
	for i in range(a):
		for j in range(b):
			if a == b:
				for k in range(c):
					if a == c:
						return False
	return True


# Element uniqueness problem
# In the element uniqueness problem, we are given a single sequence s with n elements and asked
# whether all elements of that collection are distinct from each other
def unique1(s):
	"""Return True if there are no duplicate elements in sequence s."""
	for i in range(len(s)):
		for j in range(i + 1, len(s)):
			if s[i] == s[j]:
				return False
	return True  # The solution is obviously 0(n2)


def unique2(s):
	"""Return True if there are no duplicate elements in sequence s."""
	sort = sorted(s)
	for i in range(len(sort) - 1):
		if s[i] == s[i + 1]:
			return False
	return True  # Due to sorting action the complexity of this operation is 0(nlogn)


if __name__ == '__main__':
	print(unique2([3, 35, 5, 6, 2, 2, 34, 54, 465, 656, 6, 73, 24, 23243, 545, 65]))
