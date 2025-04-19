class Node:
	value: str
	key: int

	def __init__(self, key: str, value: int) -> None:
		self.value = value
		self.key = key
		self.next = None
		self.prev = None

class Cache:
	maxSize: int
	hm: map
	head: Node
	tail: Node

	def __init__(self, maxSize: int) -> None:
		self.maxSize = maxSize
		self.hm = {}
		self.head = None
		self.tail = None

	def getValue(self, key: str) -> str:
		result = 0
		if key not in self.hm.keys():
			return result

		item = self.hm[key]

		if item != self.head:
			self.removeFromLinkedList(item)
			self.insertFrontLinkedList(item)

		return item.value

	def removeFromLinkedList(self, node: Node) -> None:
		if node is None:
			return

		if node.prev is not None:
			node.prev.next = node.next
		if node.next is not None:
			node.next.prev = node.prev

		if node == self.tail:
			self.tail = node.prev

		if node == self.head:
			self.head = node.next

	def insertFrontLinkedList(self, item: Node) -> None:
		if self.head is None:
			self.head = item
			self.tail = item

		else:
			self.head.prev = item
			item.next = self.head
			self.head = item

	def removeKey(self, key: str) -> None:
		if key not in self.hm.keys():
			return

		item = self.hm[key]
		del self.hm[key]

		self.removeFromLinkedList(item)

	def setKeyValue(self, key: str, value: str) -> None:
		if key in self.hm.keys():
			removeKey(key)

		if len(self.hm) >= self.maxSize:
			return

		item = Node(key, value)

		self.insertFrontLinkedList(item)
		self.hm[key] = item


c = Cache(10)

c.setKeyValue("hello", "word")
c.setKeyValue("test", "cache")
c.setKeyValue("app", "mobile")
c.setKeyValue("hi", "my name")

c.removeKey("app")

n = c.head

while n is not None:
	print(n.key, n.value)
	n = n.next








