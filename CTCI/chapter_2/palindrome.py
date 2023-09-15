'''
Palindrome: Implement a function to check if a linked list is a palindrome.
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

def is_palindrome(ll):
	word_len = 0

	current = ll.head
	while current != None:
		current = current.next
		word_len += 1

	i = 0

	word_len -= 1

	current = ll.head
	while i <= word_len:
		tail = ll.head
		for j in range(word_len):
			tail = tail.next

		if current.data != tail.data:
			return False

		i += 1
		current = current.next
		word_len -= 1

	return True

head = create_linked_list(['f', 'p', 'a', 't', 't', 'p', 'f'])
ll = LinkdedList(head)

print(is_palindrome(ll))