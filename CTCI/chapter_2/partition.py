'''
Write code to partition a linked list around a value x,
such that all nodes less than x come before all nodes greater
than or equal to x. If x is contained within the list,
the values of x only need to be after the elements less
than x (see below). 
The partition element x can appear anywhere in the "right partition";
it does not need to appear between the left and right partitions.
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

def partition(node, x):
	next_large_head = None
	next_large_tail = None

	if node.data >= x:
		next_large_tail = node.head
		next_large_head = next_large_tail
		

	current = node
	current_head = current

	while current.next != None:
		if current.next.data < x:
			current = current.next
		else:
			if next_large_head == None:
				next_large_tail = current.next
				next_large_head = next_large_tail
				current.next = current.next.next
			else:
				next_large_tail.next = current.next
				next_large_tail = next_large_tail.next
				current.next = current.next.next
				
				next_large_tail.next = None
	current.next = next_large_head

	return current_head

head = create_linked_list([3,5,8,5,10,2,1])
result = partition(head, 5)

while result != None:
	print(result.data)
	result = result.next
