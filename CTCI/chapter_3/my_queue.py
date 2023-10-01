'''
 Implement a MyQueue class which implements a queue using two stacks.
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


class MyQueue:

	def __init__(self, size):
		self.currentSize = 0
		self.size = size
		self.stack1 = Stack(size)
		self.stack2 = Stack(size)

	def peek(self):
		if not self.stack1.isEmpty():
			while not self.stack1.isEmpty():
				self.stack2.push(self.stack1.pop())

			value = self.stack2.peek()

			while not self.stack2.isEmpty():
				self.stack1.push(self.stack2.pop())

			return value

		elif not self.stack2.isEmpty():
			while not self.stack2.isEmpty():
				self.stack1.push(self.stack2.pop())

			value = self.stack1.peek()

			while not self.stack1.isEmpty():
				self.stack2.push(self.stack1.pop())

			return value

	def add(self, item):
		if self.currentSize == self.size:
			return

		if self.stack2.isEmpty() and not self.stack1.isFull():
			self.stack1.push(item)
			self.currentSize += 1
		elif self.stack1.isEmpty() and not self.stack2.isFull():
			self.stack2.push(item)
			self.currentSize += 1
		elif self.stack1.isEmpty() and self.stack2.isEmpty():
			self.stack1.push(item)
			self.currentSize += 1

	def remove(self):
		if not self.stack1.isEmpty():
			while not self.stack1.isEmpty():
				self.stack2.push(self.stack1.pop())

			value = self.stack2.pop()

			while not self.stack2.isEmpty():
				self.stack1.push(self.stack2.pop())

			self.currentSize -= 1

			return value

		elif not self.stack2.isEmpty():
			while not self.stack2.isEmpty():
				self.stack1.push(self.stack2.pop())

			value = self.stack1.pop()

			while not self.stack1.isEmpty():
				self.stack2.push(self.stack1.pop())

			self.currentSize -= 1

			return value

	def isEmpty(self):
		return self.stack2.isEmpty() and self.stack1.isEmpty()



queue = MyQueue(8)
print(queue.isEmpty())
queue.add(3)
queue.add(2)
queue.add(5)
queue.add(6)
queue.add(8)
queue.remove()
print(queue.isEmpty())
print(queue.peek())
print(queue.stack1.values)