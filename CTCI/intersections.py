'''
Given two (singly) linked lists,
determine if the two lists intersect. Return the intersecting node.
Note that the intersection is defined based on reference, not value.
That is, if the kth node of the first linked list is the exact same node
(by reference) as the jth node of the second linked list,
then they are intersecting.
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

def check_len(ll):
	i = 0

	current= ll.head

	while current != None:
		i += 1
		current = current.next

	return i

def check_intersect(ll_long, ll_short, moving):
	current = ll_long

	for i in range(moving):
		current = current.next

	flag = False
	while current != None:
		if current.data != ll_short.data:
			flag = False
		else:
			flag = True
		current = current.next
		ll_short = ll_short.next

	return flag


def is_intersect(ll1, ll2):

	len_ll1 = check_len(ll1)
	len_ll2 = check_len(ll2)

	current = ll1.head

	if len_ll2 > len_ll1:
		return check_intersect(ll2.head, ll1.head, len_ll2 - len_ll1)
	else:
		return check_intersect(ll1.head, ll2.head, len_ll1 - len_ll2)


ll1 = LinkdedList(create_linked_list([123,123,3,432,54,61,2,34,45,3]))
ll_intersect = LinkdedList(create_linked_list([8]))
ll2 = LinkdedList(create_linked_list([945,34,54]))

ll2.add_node(ll_intersect.head)
ll1.add_node(ll_intersect.head)

print(is_intersect(ll1, ll2))

