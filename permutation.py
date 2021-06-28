
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


def permutation_stack(n):
	