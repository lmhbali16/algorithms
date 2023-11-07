class Node:

	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None
		self.list_sets = []
		self.visited = False

	def update_list(self, list_sets):
		for s in list_sets:
			s = s + (self.value,)
			self.list_sets.append(s)

		self.list_sets.append((self.value,))

def bst(sorted_list):
	if len(sorted_list) == 1:
		return Node(sorted_list[0])

	if len(sorted_list) == 2:
		node = Node(sorted_list[1])
		node.left = Node(sorted_list[0])

		return node

	middle = len(sorted_list) // 2

	node = Node(sorted_list[middle])
	node.left = bst(sorted_list[:middle])
	node.right = bst(sorted_list[middle + 1:])

	return node

def calculate(tree, list_sets):
	if tree == None:
		return

	tree.update_list(list_sets)
	calculate(tree.left, tree.list_sets)
	calculate(tree.right, tree.list_sets)

def path_to_sum(tree, num):
	calculate(tree, [])

	result = 0
	d = [tree]
	while len(d) > 0:
		a = d[0]
		if a.left != None:
			d.append(a.left)
		if a.right != None:
			d.append(a.right)

		for s in a.list_sets:
			temp_s = list(s)
			temp_result = 0
			for i in temp_s:
				temp_result += i

			if temp_result == num:
				result += 1

		d = d[1:]


	return result

t1 = bst([3,2,1,2,3,3,0])

result = path_to_sum(t1, 6)
print(result)

