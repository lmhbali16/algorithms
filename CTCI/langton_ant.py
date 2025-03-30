class Langton:
	gridSize: int
	grid: list
	increaseSize: int
	pos: tuple

	def buildGrid(self) -> None:
		self.grid = []

		flag = True
		for i in range(self.gridSize * self.gridSize):
			if i % self.gridSize == 0:
				flag = not flag

			if i % 2 == 0 and flag:
				self.grid.append('O')
			elif i % 2 == 0 and not flag:
				self.grid.append('X')
			elif i % 2 != 0 and flag:
				self.grid.append('X')
			else:
				self.grid.append('O')

		self.grid[self.pos[0] * self.gridSize + self.pos[1]] = '#'

	def __init__(self, initialGridSize: int, increaseSize: int) -> None:
		self.gridSize = initialGridSize
		self.increaseSize = increaseSize
		self.grid = []
		self.pos = (0, 0)

		self.buildGrid()


	def printGrid(self) -> None:
		for j in range(self.gridSize-1):
			print(self.grid[j * self.gridSize: (j+1) *self.gridSize])

	def increaseGridSize(self) -> None:
		self.gridSize += self.increaseSize
		self.buildGrid()

	def flip(self) -> None:
		for i in range(len(self.grid)):
			if self.grid[i] == 'O':
				self.grid[i] = 'X'
			elif self.grid[i] == 'X':
				self.grid[i] = 'O'

	def move1(self) -> None:
		self.flip()

		value = 'O'
		pos = self.pos[0] * self.gridSize + self.pos[1]
		if pos % self.gridSize == 0:
			if self.grid[pos+1] == 'O':
				value = 'X'
		else:
			if self.grid[pos-1] == 'O':
				value = 'X'

		self.grid[self.pos[0] * self.gridSize + self.pos[1]] = value

		self.pos = (self.pos[0] + 1, self.pos[1])
		self.grid[self.pos[0] * self.gridSize + self.pos[1]] = '#'

	def move2(self) -> None:
		self.flip()

		value = 'O'
		pos = self.pos[0] * self.gridSize + self.pos[1]
		if pos % self.gridSize == 0:
			if self.grid[pos+1] == 'O':
				value = 'X'
		else:
			if self.grid[pos-1] == 'O':
				value = 'X'

		
		self.grid[self.pos[0] * self.gridSize + self.pos[1]] = value


		self.pos = (self.pos[0], self.pos[1] + 1)
		self.grid[self.pos[0] * self.gridSize + self.pos[1]] = '#'

	def printMoves(self, k: int) -> None:
		pos = self.pos[0]
		if pos < self.pos[1]:
			pos = self.pos[1]


		while self.gridSize < pos + k:
			self.increaseGridSize()

		flag = True
		for i in range(k):
			if flag:
				self.move1()
			else:
				self.move2()

			flag = not flag

		self.printGrid()




a = Langton(10, 4)
a.printMoves(2)

