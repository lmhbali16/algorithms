class Node:

	def __init__(self, value):
		self.value = value
		self.leftChild = None
		self.rightChild = None

def binary_search_tree(sorted_list):
	if len(sorted_list) == 1:
		return Node(sorted_list[0])

	if len(sorted_list) == 2:
		node = Node(sorted_list[1])
		node.leftChild = Node(sorted_list[0])

		return node

	middle = len(sorted_list) // 2

	node = Node(sorted_list[middle])
	node.leftChild = binary_search_tree(sorted_list[:middle])
	node.rightChild = binary_search_tree(sorted_list[middle + 1:])

	return node

node = binary_search_tree([1,2,3,4,6,7,8])

def show_binary_tree(node):
	list_nodes = [node]

	while len(list_nodes) > 0:
		a = list_nodes[0]
		print(a.value)
		if a.leftChild != None:
			list_nodes.append(a.leftChild)

		if a.rightChild != None:
			list_nodes.append(a.rightChild)

		list_nodes = list_nodes[1:]

show_binary_tree(node)


