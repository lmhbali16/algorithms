class Node:

	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None
		self.parent = None

	def addParent(self, parent):
		self.parent = parent

	def addLeft(self, child):
		self.left = child

	def addRight(self, child):
		self.right = child


def create_binary_tree(numbers: list):
	root = Node(numbers[0])
	numbers = numbers[1:]
	leaves = [root]

	while len(numbers) > 0 and len(leaves) > 0:
		leaf = leaves[0]
		new_leaf = Node(numbers[0])
		if leaf.left != None and leaf.right != None:
			leaves = leaves[1:]
			continue

		elif leaf.left == None:
			leaf.addLeft(new_leaf)
			numbers = numbers[1:]
			leaves.append(new_leaf)

		elif leaf.right == None:
			leaf.addRight(new_leaf)
			numbers = numbers[1:]
			leaves.append(new_leaf)

	return root

tree = create_binary_tree([2,3,4,6,64,76,8,34,234,13,123])

def print_binary_tree(tree):
	nodes = [tree]

	while len(nodes) > 0:
		node = nodes[0]
		print(node.value)
		nodes = nodes[1:]

		if node.left != None:
			nodes.append(node.left)
		if node.right != None:
			nodes.append(node.right)

def bfs(tree, value):
	nodes = [tree]

	while len(nodes) > 0:
		node = nodes[0]

		if node.value == value:
			return True

		if node.left != None:
			nodes.append(node.left)
		if node.right != None:
			nodes.append(node.right)

		nodes = nodes[1:]

	return False

def first_common_ancestor(tree, value1, value2):
	if tree.left == None and tree.right == None:
		return None
	elif tree.left != None and tree.right == None:
		return first_common_ancestor(tree.left, value1, value2)
	elif tree.right != None and tree.left == None:
		return first_common_ancestor(tree.right, value1, value2)

	if bfs(tree.left, value1) and bfs(tree.right,value2):
		return tree
	elif bfs(tree.right, value1) and bfs(tree.left, value2):
		return tree
	elif bfs(tree.right, value1) and bfs(tree.right, value2):
		return first_common_ancestor(tree.right, value1, value2)
	elif bfs(tree.left, value1) and bfs(tree.left, value2):
		return first_common_ancestor(tree.left, value1, value2)

	print(tree.value)
	return None

print(first_common_ancestor(tree, 13, 123).value)






