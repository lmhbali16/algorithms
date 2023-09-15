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

def remove_dup(linkedlist: Node) -> Node:
	table = {}
	head = linkedlist
	table[linkedlist.data] = 1

	while linkedlist.next != None:
		if linkedlist.next.data in table:
			linkedlist.next = linkedlist.next.next
		else:
			table[linkedlist.next.data] = 1
			linkedlist = linkedlist.next

	return head

linkedlist = create_linked_list([1,3,23,43,2,23,6,34,2,541,34])
dedupped_linkedlist = remove_dup(linkedlist)

while dedupped_linkedlist != None:
	print(dedupped_linkedlist.data)
	dedupped_linkedlist = dedupped_linkedlist.next
