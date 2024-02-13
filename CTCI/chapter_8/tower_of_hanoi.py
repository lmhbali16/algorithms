class Disk:

	def __init__(self, size):
		self.size = size

class Tower:

	def __init__(self):
		self.stack = []

	def add(self, disk):
		if disk == None:
			return False

		if len(self.stack) == 0:
			self.stack = [disk] + self.stack
			return True		

		topItem = self.stack[0]
		if topItem.size <= disk.size:
			return False
		else:
			self.stack = [disk] + self.stack
			return True

	def pop(self):
		if len(self.stack) == 0:
			return None

		item = self.stack[0]
		self.stack = self.stack[1:]

		return item

	def peek(self):
		if len(self.stack) == 0:
			return -1
		else:
			return self.stack[0].size

class TowerOfHanoi:

	def __init__(self, N):
		self.N = N
		self.tower1 = Tower()
		self.tower2 = Tower()
		self.tower3 = Tower()

		for i in range(1, N+1):
			self.tower1.add(Disk(N+1 - i))

	def move(self, num, towerOrigin, towerDestination, towerBuffer):
		if num == 0:
			return
		
		self.move(num - 1, towerOrigin, towerBuffer, towerDestination)
		towerDestination.add(towerOrigin.pop())

		self.move(num-1, towerBuffer, towerDestination, towerOrigin)

tower_of_hanoi = TowerOfHanoi(9)

tower_of_hanoi.move(9, tower_of_hanoi.tower1, tower_of_hanoi.tower3, tower_of_hanoi.tower2)

print(tower_of_hanoi.tower3.stack[0].size)


