'''
Write an algorithm to find the "next" node (i.e., in-order successor)
of a given node in a binary search tree. You may assume that each
node has a link to its parent.
'''

class Tree:

	def __init__(self, value, leftChild, righChild, parent):
		self.value = value
		self.leftChild = leftChild
		self.righChild = righChild
		self.parent = parent


def left_most_child(node):
	if node == None:
		return None

	while node.leftChild != None:
		node = node.leftChild

	return node

def successor(node):
	if node == None:
		return None

	if node.righChild != None:
		return left_most_child(node.righChild)
	else:
		temp = node
		t = node.parent

		while t != None and t.leftChild != temp:
			temp = t
			t = t.parent

		return t


