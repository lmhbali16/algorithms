'''
Write a program to sort a stack such that the smallest items are on the top.
You can use an additional temporary stack, but you may not copy
the elements into any other data structure (such as an array).
The stack supports the following operations: push, pop, peek, and isEmpty.
'''

class Stack:

	def __init__(self, stackSize):
		self.values = []
		self.size = stackSize
		self.currentSize = 0

	def peek(self):
		return self.values[-1]

	def push(self, item):
		if self.currentSize == self.size:
			return None
		else:
			self.values.append(item)
			self.currentSize += 1
			return item

	def pop(self):
		if self.currentSize == 0:
			return None

		self.currentSize -= 1
		item = self.values[self.currentSize]
		self.values = self.values[:self.currentSize]
		return item

	def isFull(self):
		return self.size == self.currentSize

	def isEmpty(self):
		return self.currentSize == 0

def sort_stack(stack):
	temporary_stack = Stack(stack.size)
	temp_value = None
	temporary_stack.push(stack.pop())

	while not stack.isEmpty():
		if temporary_stack.peek() >= stack.peek():
			temporary_stack.push(stack.pop())

		else:
			temp_value = stack.pop()

			while not temporary_stack.isEmpty() and temporary_stack.peek() < temp_value:
				stack.push(temporary_stack.pop())

			temporary_stack.push(temp_value)

	while not temporary_stack.isEmpty():
		stack.push(temporary_stack.pop())


stack = Stack(6)
stack.push(4)
stack.push(7)
stack.push(2)
stack.push(1)
stack.push(45)
stack.push(32)

print(stack.values)

sort_stack(stack)

print(stack.values)