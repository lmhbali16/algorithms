
'''
Consider the problem of given an integer n,
generating all possible permutations of the numbers {1, 2, . . . , n}.

Provide a recursive algorithm for this problem.

Provide a non-recursive algorithm for this problem using a stack

'''

def permutation(n):
	b = [i for i in range(1, n+1)]
	def helper(a: list, i: int):
		if i == n-1:
			print(a)

		for j in range(i, n):
			temp = a[i]
			a[i] = a[j]
			a[j] = temp
			helper(a, i + 1)

			temp = a[i]
			a[i] = a[j]
			a[j] = temp


	helper(b, 0)

# I still don't understand how this works
def permutation_stack(n):
	b = [i for i in range(1, n+1)]
	stack = [('start', 0, 0)]

	while len(stack) > 0:
		c, i, j = stack.pop()
		if c == 'start':
			if i == n:
				print(b)
			else:
				temp = b[i]
				b[i] = b[j]
				b[j] = temp
				stack.append(('finish', i, j))
				stack.append(('start', i+1, i+1))

		elif c == 'finish':
			temp = b[i]
			b[i] = b[j]
			b[j] = temp

			if j < n-1:
				stack.append(('start', i, j+1))

n= 3
permutation_stack(n)