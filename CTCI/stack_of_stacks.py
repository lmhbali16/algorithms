'''
 Imagine a (literal) stack of plates. If the stack gets too high,
 it might topple. Therefore, in real life, we would likely start
 a new stack when the previous stack exceeds some threshold.
 Implement a data structure SetOfStacks that mimics this.
 SetOfStacks should becomposed of several stacks
 and should create a new stack once the previous one exceeds capacity.
 SetOfStacks. push() and SetOfStacks. pop() should behave
 identically to a single stack (that is, pop() should return the same
 values as it would if there were just a single stack).
'''
import sys

class MiniStack:

	def __init__(self, stackSize):
		self.values = []
		self.size = stackSize
		self.currentSize = 0

	def peek(self):
		print(self.values)
		return self.values[-1]

	def push(self, item):
		if self.currentSize == self.size:
			return None
		else:
			self.values.append(item)
			self.currentSize += 1
			return item

	def pop(self):
		self.currentSize -= 1
		item = self.values[self.currentSize]
		self.values = self.values[:self.currentSize]
		return item, self.currentSize

	def isFull(self):
		return self.size == self.currentSize

class Stack:

	def __init__(self, stackSize):
		self.values = []
		self.size = stackSize
		self.currentSize = 0
		self.stacks = []
		self.stackLength = 0


	def push(self, item):
		if self.currentSize < self.size:
			self.values.append(item)
			self.currentSize += 1

		else:
			self.pushToNewStack(item)

	def pushToNewStack(self, item):
		if self.stackLength == 0 or self.stacks[-1].isFull():
			miniStack = MiniStack(self.size)
			miniStack.push(item)
			self.stacks.append(miniStack)
			self.stackLength += 1

		else:
			self.stacks[-1].push(item)


	def pop(self):
		if self.stackLength == 0:
			if self.currentSize == 0:
				return None
			else:
				value = self.values[self.currentSize -1]
				self.values = self.values[:self.currentSize - 2]
				self.currentSize -= 1

				return values

		else:
			return self.popLastStack()

	def popLastStack(self):
		(value, size) = self.stacks[-1].pop()

		if size == 0:
			self.stackLength -= 1
			self.stacks = self.stacks[:self.stackLength -1]

		return value

	def peek(self):
		if self.stackLength == 0:
			if self.currentSize == 0:
				return sys.maxsize
			else:
				return self.values[-1]

		else:
			return self.stacks[-1].peek()


stack = Stack(4)

stack.push(4)
stack.push(5)
stack.push(6)
stack.push(7)
stack.push(8)
stack.push(9)
stack.pop()
stack.pop()

print(stack.peek())












