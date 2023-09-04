'''
Sum Lists: You have two numbers represented by a linked list,
where each node contains a single digit.
The digits are stored in reverse order,
such that the 1 's digit is at the head of the list.
Write a function that adds the two numbers and returns the sum as a linked list.


Input:(7-> 1 -> 6) + (5 -> 9 -> 2).
That is,617 + 295.
Output:2 -> 1 -> 9.
That is,912.
'''

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

class LinkdedList:

	def __init__(self, head):
		self.head = head

	def add_node(self, node):
		tail = self.head

		while tail.next != None:
			tail = tail.next

		tail.next = node

def sum_lists(node1, node2):
	digit = 1
	node1_sum = 0
	node2_sum = 0

	while node1 != None:
		node1_sum = node1_sum + node1.data * digit
		node1 = node1.next
		digit *= 10

	digit = 1

	while node2 != None:
		node2_sum = node2_sum + node2.data * digit
		node2 = node2.next
		digit *= 10

	sum_nodes = str(node1_sum + node2_sum)

	result = LinkdedList(Node(int(sum_nodes[-1])))

	i = len(sum_nodes) - 2
	while i >= 0:
		result.add_node(Node(int(sum_nodes[i])))
		i -= 1

	return result

node1 = create_linked_list([3, 4, 5, 6, 1])
node2 = create_linked_list([1, 1, 2, 3, 9])

result = sum_lists(node1, node2)

t = result.head

while t != None:
	print(t.data)
	t = t.next




