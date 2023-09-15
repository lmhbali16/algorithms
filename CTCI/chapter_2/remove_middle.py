'''
Delete Middle Node: Implement an algorithm to delete a node in the middle
(i.e., any node but the first and last node, not necessarily the exact middle)
of a singly linked list, given only access to that node.
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

def remove_middle(ll):
	k = 0
	current = ll.head

	while current != None:
		current = current.next
		k += 1

	middle = k // 2

	t = ll.head

	for i in range(middle -1):
		t = t.next

	t.next = t.next.next

head = create_linked_list([3,3,34,54,2,6,564,45,65765,76])
ll = LinkdedList(head)

remove_middle(ll)

while head != None:
	print(head.data)
	head = head.next