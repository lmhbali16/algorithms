'''
Given a circular linked list, implement an algorithm
that returns the node at the beginning of the loop.
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
		current = self.head
		if current == None:
			self.head = node
			return

		while current.next != None:
			current = current.next

		current.next = node

def is_loop(ll):
	pointer1 = pointer2 = ll.head

	while pointer2 and pointer2.next:
		pointer1 = pointer1.next
		pointer2 = pointer2.next.next

		if pointer1 == pointer2:
			return True, pointer1

	return False, None

def find_loop(ll):
	flag, pointer2 = is_loop(ll)
	if not flag:
		return None

	pointer1 = ll.head
	print(pointer2.data)

	while pointer1 != pointer2:
		pointer1 = pointer1.next
		pointer2 = pointer2.next

	return pointer1


ll1 = LinkdedList(create_linked_list([123,123,3,432,54,61,2,34,45,3]))
ll2 = LinkdedList(create_linked_list([945,34,54]))

ll1.add_node(ll2.head)
ll2.add_node(ll2.head)

print(find_loop(ll1).data)



