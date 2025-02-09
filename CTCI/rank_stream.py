class Stream:

	def merge_sort(self, l: []) -> list:
		if len(l) == 1:
			return l

		mid = len(l) // 2

		left = self.merge_sort(l[:mid])
		right = self.merge_sort(l[mid:])

		i = 0
		j = 0
		idx = 0

		while i < len(left) and j < len(right):
			if left[i] <= right[j]:
				l[idx] = left[i]
				i += 1
				idx += 1
			else:
				l[idx] = right[j]
				j += 1
				idx += 1

		while i < len(left):
			l[idx] = left[i]
			idx += 1
			i += 1

		while j < len(right):
			l[idx] = right[j]
			idx += 1
			j += 1

		return l



	def __init__(self) -> None:
		self.order = {}

	def Track(self, x: int) -> None:
		if len(self.order) == 0:
			self.order[x] = 0

		if x in self.order.keys():
			return

		s = -1
		for i in self.order.keys():
			if i > x:
				self.order[i] = self.order[i] + 1

			if i < x and i > s:
				s = i

		if s == -1:
			self.order[x] = 0
		else:
			self.order[x] = self.order[s] + 1

	def GetRankNumber(self, x: int) -> int:
		try:
			result = self.order[x]
			return result
		except KeyError:
			return -1

l = [5, 1, 4, 4, 5, 9, 7, 13, 3]
a = Stream()
a.Track(5)
a.Track(1)
a.Track(4)
a.Track(4)
a.Track(5)
a.Track(9)
a.Track(7)
a.Track(13)
a.Track(3)

print(a.GetRankNumber(13))
a.Track(12)

print(a.GetRankNumber(13))

