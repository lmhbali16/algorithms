class Listy:

	def __init__(self, l: []) -> None:
		self.list = l

	def elementAt(self, x: int) -> int:
		if x >= len(self.list) or x < 0:
			return -1

		return self.list[x]


def find_length(listNum: Listy, num: int) -> int:
	lower_bound = 1

	while listNum.elementAt(lower_bound - 1) != -1 and listNum.elementAt(lower_bound - 1) < num:
		lower_bound *= 2


	return lower_bound

def binary_search(listNum: Listy, low: int, high: int, num: int) -> int:
	if low > high:
		return -1

	mid = (low + high) // 2
	if listNum.elementAt(mid) == num:
		return mid


	if listNum.elementAt(mid) > num:
		return binary_search(listNum, low, mid-1, num)
	elif listNum.elementAt(mid) < num:
		return binary_search(listNum, mid+1, high, num)


def sorted_search(listNum: Listy, num: int) -> int:
	idx = find_length(listNum, num)

	if listNum.elementAt(idx) == -1:
		return 1

	return binary_search(listNum, idx // 2, idx, num)


test = Listy([2,2,4,5,5,6,7,7,7,8,9,12])

print(sorted_search(test, 7))