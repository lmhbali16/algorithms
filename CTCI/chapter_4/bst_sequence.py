'''
Not correct. I have to retry it later
'''

class TreeNode:

	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

class Node:

	def __init__(self, value):
		self.value = value
		self.next = None

class LinkedList:

	def __init__(self, nodeHead):
		self.head = nodeHead

	def append(self, node):

		current = self.head
		while current.next != None:
			current = current.next

		current.next = node

	def appendAll(self, linkedList):
		current = self.head
		while current.next != None:
			current = current.next

		node = linkedList.head
		while node != None:
			current.next = node
			node = node.next

	def copy(self):
		result = LinkedList(self.head)

		if self.head == None:
			return result

		current = self.head.next
		while current != None:
			result.append(current)
			current = current.next

		return result

	def pop_first(self):
		head = self.head
		self.head = self.head.next

		return head

	def remove_last(self):
		current = self.head
		while current.next != None and current.next.next != None:
			current = current.next

		if current != None:
			current.next = None

	def add_first(self, node):
		current_head = self.head
		self.head = node
		self.head.next = current_head

	def length(self):
		counter = 0

		current = self.head
		while  current != None:
			counter += 1
			current = current.next

		return counter

def weave_list(left_seq, right_seq, weaved, prefix):
	if left_seq.length() == 0 or right_seq.length() == 0:
		result = prefix.copy()
		result.appendAll(left_seq)
		result.appendAll(right_seq)
		weaved.append(result.head)
		return

	first = left_seq.pop_first()
	prefix.append(first.head)
	weave_list(left_seq, right_seq, weaved, prefix)
	prefix.remove_last()
	left_seq.add_first(first)

	second = right_seq.pop_first()
	prefix.append(second.head)
	weave_list(left_seq, right_seq, weaved, prefix)
	prefix.remove_last()
	left_seq.add_first(second)

def all_sequences(tree_node):
	result = []

	if tree_node == None:
		result.append(LinkedList(None).head)
		return result

	prefix = LinkedList(Node(tree_node.value))

	left_seq = all_sequences(tree_node.left)
	right_seq = all_sequences(tree_node.right)

	for left_sub_seq in left_seq:
		for right_sub_seq in right_seq:
			weaved = []
			weave_list(left_sub_seq, right_sub_seq, weaved, prefix)
			result += weaved

	return result

def bst(sorted_list):
	if len(sorted_list) == 1:
		return TreeNode(sorted_list[0])

	if len(sorted_list) == 2:
		node = TreeNode(sorted_list[1])
		node.left = TreeNode(sorted_list[0])

		return node

	middle = len(sorted_list) // 2

	node = TreeNode(sorted_list[middle])
	node.left = bst(sorted_list[:middle])
	node.right = bst(sorted_list[middle + 1:])

	return node

tree_node = bst([1,2,3,4,6,7,8, 9, 10, 11])


result = all_sequences(tree_node)

