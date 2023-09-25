'''
An animal shelter, which holds only dogs and cats,
operates on a strictly"first in, first out" basis.
People must adopt either the"oldest" (based on arrival time) of all
animals at the shelter, or they can select whether they would prefer
a dog or a cat (and will receive the oldest animal of that type).
They cannot select which specific animal they would like.
Create the data structures to maintain this system and implement
operations such as enqueue, dequeueAny, dequeueDog, and dequeueCat.
You may use the built-in Linked list data structure.
'''

class Queue:

	def __init__(self, stackSize):
		self.values = []
		self.size = stackSize
		self.currentSize = 0

	def peek(self):
		if self.currentSize == 0:
			return None
		return self.values[0]

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
		item = self.values[0]
		self.values = self.values[1:]
		return item

	def isFull(self):
		return self.size == self.currentSize

	def isEmpty(self):
		return self.currentSize == 0


class Node:

	def __init__(self, animalType, name):
		self.animalType = animalType
		self.order = None
		self.name = name
		self.prev = None
		self.next = None

	def addPrev(self, node):
		self.prev = node

	def addNext(self, node):
		self.next = node

class LinkedList:

	def __init__(self, head):
		self.head = head

	def add(self, node):

		current = self.head

		while current.next != None:
			current = current.next

		current.next = node
		node.prev = current


class AnimalShelter:

	def __init__(self):
		self.dogs = Queue(10)
		self.cats = Queue(10)
		self.currentNum = 0
		self.queue = None

	def enqueue(self, animalType, name):
		if animalType == 'dog':
			dog = Node(animalType, name)
			dog.order = self.currentNum
			self.dogs.push(dog)

			if self.queue == None or self.queue.head == None:
				self.queue = LinkedList(dog)

			elif not self.dogs.isFull():
				self.queue.add(dog)

			self.currentNum += 1

		elif animalType == 'cat':
			cat = Node(animalType, name)
			cat.order = self.currentNum
			self.cats.push(cat)

			if self.queue == None or self.queue.head == None:
				self.queue = LinkedList(cat)

			elif not self.cats.isFull():
				self.queue.add(cat)

			self.currentNum += 1

	def dequeueAny(self):
		if self.queue == None or self.queue.head == None:
			return

		if self.dogs.isEmpty() and self.cats.isEmpty():
			return None

		if (not self.dogs.isEmpty() and self.cats.isEmpty()) or (self.dogs.peek().order < self.cats.peek().order):
			self.queue.head = self.queue.head.next

			if self.queue.head != None:
				self.queue.head.prev = None

			dog = self.dogs.pop()
			dog.next = None
			dog.prev = None

			return dog

		if (self.dogs.isEmpty() and not self.cats.isEmpty()) or (self.cats.peek().order < self.dogs.peek().order):
			self.queue.head = self.queue.head.next

			if self.queue.head != None:
				self.queue.head.prev = None

			cat = self.cats.pop()
			cat.next = None
			cat.prev = None

			return cat

	def dequeueCat(self):
		if self.queue == None or self.queue.head == None:
			return

		cat = self.cats.pop()

		prev = None
		current = self.queue.head
		nextNode = self.queue.head

		while current != cat:
			prev = current
			current = current.next
			nextNode = current.next

		prev.next = nextNode
		nextNode.prev = prev

		return cat

	def dequeueDog(self):
		if self.queue == None or self.queue.head == None:
			return

		dog = self.dogs.pop()

		prev = None
		current = self.queue.head
		nextNode = self.queue.head.next

		if current == dog:
			self.queue.head = self.queue.head.next

			if self.queue.head != None:
				self.queue.head.prev = None

			return dog

		while current != dog:
			prev = current
			current = current.next
			nextNode = current.next

		prev.next = nextNode
		nextNode.prev = prev

		return dog




animalShelter = AnimalShelter()

animalShelter.enqueue('dog', 'rex')
animalShelter.enqueue('dog', 'dug')
animalShelter.enqueue('cat', 'kitty')
animalShelter.enqueue('cat', 'mia')
animalShelter.enqueue('cat', 'teemo')
animalShelter.enqueue('dog', 'ekko')
animalShelter.enqueue('cat', 'buddy')
animalShelter.enqueue('dog', 'bella')

print(animalShelter.dequeueAny().name)
print(animalShelter.dequeueCat().name)
print(animalShelter.dequeueCat().name)
print(animalShelter.dequeueDog().name)
print(animalShelter.dequeueDog().name)
print(animalShelter.dequeueAny().name)



