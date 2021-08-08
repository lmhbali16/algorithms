'''
 Given a singly linked list, we would like to traverse the
 elements of the list in reverse order.
 You are only allowed to use O(1) extra space,
 but this time you are allowed to modify the list you are traversing.
 Give an O(n) time algorithm.
'''


class Node:

	value = None
	next = None

def reverse_linkedlist(head):

	if head.next is None:
		return a

	b = head.next
	head.next = None

	while b.next is not None:
		temp = b.next
		b.next = head
		head = b
		b = temp

	b.next = head

	return b


a = Node()
a.value = 9

b = Node()
b.value = 3
c = Node()
c.value = 1
d = Node()
d.value = 4
e = Node()
e.value = 8

a.next = b
b.next = c
c.next = d
d.next = e

result = a
while result is not None:
	print(result.value)
	result = result.next

result = reverse_linkedlist(a)

print("\nreverse\n")
while result is not None:
	print(result.value)
	result = result.next