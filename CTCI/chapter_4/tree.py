class DirectedNode:

	def __init__(self, value):
		self.value = value
		self.visited = False
		self.adjacentNodes = []


	def addAdjacentNode(self, node):
		self.adjacentNodes.append(node)

	def markVisited(self):
		self.visited = True
