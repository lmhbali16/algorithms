'''
Implement a function to check if a binary tree is balanced.
For the purposes of this question, a balanced tree is defined to be
a tree such that the heights of the two subtrees of any node never
differ by more than one.
'''

from binary_search_tree import bst
from binary_search_tree import show_binary_tree

import sys

class Node:

	def __init__(self, value):
		self.level = 0
		self.value = value
		self.leftChild = None
		self.rightChild = None


def is_balanced(tree):
	if tree == None:
		return -1

	left_height = is_balanced(tree.leftChild)

	if left_height == -sys.maxsize:
		return -sys.maxsize

	right_height = is_balanced(tree.rightChild)

	if right_height == -sys.maxsize:
		return -sys.maxsize

	diff = left_height - right_height

	if abs(diff) > 1:
		return -sys.maxsize
	else:
		return max(left_height, right_height) + 1

node = bst([1,2,3,4,6,7,8, 9, 10])
show_binary_tree(node)


modified_node = node
print(is_balanced(node) == -sys.maxsize)
modified_node.leftChild.rightChild.leftChild = Node(9)
modified_node.leftChild.rightChild.leftChild.rightChild = Node(12)


print(is_balanced(modified_node) == -sys.maxsize)