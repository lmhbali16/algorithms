'''
Describe how you could use a single array to implement three stacks.
'''

'''

'''

class MultiStack:

	def __init__(self, stackSize):
		self.numStack = 3
		self.values = [None] * (self.numStack * stackSize)
		self.size = stackSize
		self.sizes = [0] * self.numStack


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

		return self.values[self.sizes[numStack - 1] + (numStack - 1) * self.size - 1]

stacks = MultiStack(4)
stacks.push(3, 1)
stacks.push(1, 1)
stacks.push(6, 2)
stacks.push(3, 2)
stacks.push(9, 2)
print(stacks.values)
stacks.pop(2)
print(stacks.peek(2))
print(stacks.values)
