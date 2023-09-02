class Node:
	def __init__(self, num):
		self.data = num
		self.next = None

def create_linked_list(l: list) -> Node:
	if len(l) == 0:
		return None

	head = Node(l[0])
	current = head
	for i in range(1, len(l)):
		new = Node(l[i])
		current.next = new
		current = new

	return head

def kth_to_last(k, node):
	current = node
	for i in range(k):
		if node.next == None:
			break

		current = current.next

	node_i = node


	while current != None:
		current = current.next
		node_i = node_i.next

	return node_i

head = create_linked_list([3,3,34,54,2,557,6,564,45,65765,76])

print(kth_to_last(9, head).data)