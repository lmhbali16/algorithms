def merge_sort(l: []) -> list:
		if len(l) == 1:
			return l

		mid = len(l) // 2

		left = merge_sort(l[:mid])
		right = merge_sort(l[mid:])

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

def peak_valley(l: list) -> list:
	l = merge_sort(l)

	for i in range(1, len(l)):
		if i+1 < len(l):
			if l[i] < l[i+1] and l[i] > l[i-1]:
				l[i+1], l[i] = l[i], l[i+1]
		elif i + 1 == len(l):
			l[i], l[i-1] = l[i-1], l[i]

	return l


print(peak_valley([1,2,3,4,5,6,6,6,8]))
