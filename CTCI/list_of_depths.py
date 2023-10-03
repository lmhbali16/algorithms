'''
Given a binary tree, design an algorithm which creates a linked list of
all the nodes at each depth (e.g., if you have a tree with depth D,
you'll have D linked lists).
'''

from binary_search_tree import bst

class Node:
	def __init__(self, num):
		self.data = num
		self.next = None

class LinkdedList:

	def __init__(self, head):
		self.head = head

	def addNode(self, node):
		current = self.head

		while current.next != None:
			current = current.next

		current.next = node

tree = bst([1,2,3,4,6,7,8, 9])

def lod(tree):
	list_ll = []
	current_nodes = [tree]
	current_ll = None
	count = 1
	power = 0

	while len(current_nodes) > 0:
		node = current_nodes[0]
		ll = LinkdedList(Node(node.value))

		if count == 2**power:
			list_ll.append(ll)

			current_ll = ll
			count += 1

		elif count > 2**power and count < 2**(power+1):
			current_ll.addNode(Node(node.value))
			count += 1


		if node.leftChild != None:
			current_nodes.append(node.leftChild)
		if node.rightChild != None:
			current_nodes.append(node.rightChild)


		if count > 2**power and count >= 2**(power+1):
			power += 1

		current_nodes = current_nodes[1:]

	return list_ll

list_ll = lod(tree)

for ll in list_ll:
	print('---------------')
	current = ll.head

	while current.next != None:
		print(current.data)
		current = current.next

	print(current.data)