'''
How would you design a stack which,
in addition to push and pop,
has a function min which returns the minimum element?
Push, pop and min should all operate in 0(1) time.
'''

import sys

class MinStack:

	def __init__(self, stackSize): 
		self.numStack = 3
		self.values = [None] * (self.numStack * stackSize)
		self.size = stackSize
		self.sizes = [0] * self.numStack

	def pop(self, numStack):
		if numStack > self.numStack or numStack <= 0:
			return

		if self.isEmpty(numStack):
			return

		value = self.values[self.sizes[numStack - 1] + (numStack - 1) * self.size - 1]
		self.values[self.sizes[numStack - 1] + (numStack - 1) * self.size - 1] = None
		self.sizes[numStack - 1] -= 1

		return value

	def push(self, item, numStack):
		if numStack > self.numStack or numStack <= 0:
			return

		if self.isFull(numStack):
			return

		self.values[self.sizes[numStack - 1] + (numStack - 1) * self.size] = item
		self.sizes[numStack - 1] += 1

	def isFull(self, numStack):
		if self.sizes[numStack - 1] == self.size - 1:
			return True

		return False

	def pop(self, numStack):
		if numStack > self.numStack or numStack <= 0:
			return

		if self.isEmpty(numStack):
			return

		value = self.values[self.sizes[numStack - 1] + (numStack - 1) * self.size - 1]
		self.values[self.sizes[numStack - 1] + (numStack - 1) * self.size - 1] = None
		self.sizes[numStack - 1] -= 1

		return value

	def isEmpty(self, numStack):
		if numStack > self.numStack or numStack <= 0:
			return

		return self.sizes[numStack - 1] == 0

	def peek(self, numStack):
		if numStack > self.numStack or numStack <= 0:
			return

		if self.isEmpty(numStack):
			return sys.maxsize

		return self.values[self.sizes[numStack - 1] + (numStack - 1) * self.size - 1]

class MultiStack:

	def __init__(self, stackSize):
		self.numStack = 3
		self.values = [None] * (self.numStack * stackSize)
		self.size = stackSize
		self.sizes = [0] * self.numStack
		self.minStacks = MinStack(stackSize)


	def push(self, item, numStack):
		if numStack > self.numStack or numStack <= 0:
			return

		if self.isFull(numStack):
			return

		self.values[self.sizes[numStack - 1] + (numStack - 1) * self.size] = item
		self.sizes[numStack - 1] += 1

		if self.minStacks.peek(numStack) >= item:
			self.minStacks.push(item, numStack)

	def isFull(self, numStack):
		if self.sizes[numStack - 1] == self.size - 1:
			return True

		return False

	def pop(self, numStack):
		if numStack > self.numStack or numStack <= 0:
			return

		if self.isEmpty(numStack):
			return

		value = self.values[self.sizes[numStack - 1] + (numStack - 1) * self.size - 1]
		self.values[self.sizes[numStack - 1] + (numStack - 1) * self.size - 1] = None
		self.sizes[numStack - 1] -= 1

		if self.minStacks.peek(numStack) == value:
			self.minStacks.pop(numStack)

		return value

	def isEmpty(self, numStack):
		if numStack > self.numStack or numStack <= 0:
			return

		return self.sizes[numStack - 1] == 0

	def peek(self, numStack):
		if numStack > self.numStack or numStack <= 0:
			return

		return self.values[self.sizes[numStack - 1] + (numStack - 1) * self.size - 1]

	def min(self, numStack):
		if numStack > self.numStack or numStack <= 0:
			return

		return self.minStacks.peek(numStack)

stacks = MultiStack(4)
stacks.push(3, 1)
stacks.push(3, 1)
stacks.push(1, 1)
stacks.push(6, 2)
stacks.push(3, 2)
stacks.push(9, 2)
stacks.pop(2)
stacks.pop(1)
print(stacks.min(2))
print(stacks.minStacks.values)
