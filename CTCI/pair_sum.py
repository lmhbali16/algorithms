def partition(l: list, low: int, high: int) -> None:
	pivot = l[high]

	i = low - 1
	for j in range(low, high):
		if l[j] <= pivot:
			i = i + 1
			l[i], l[j] = l[j], l[i]

	l[i + 1], l[high] = l[high], l[i + 1]
	return i + 1

def quickSort(l: list, low: int, high: int) -> None:
	if len(l) == 0:
		return

	if high is None:
		high = l[-1]

	if low < high:
		p = partition(l, low, high)
		quickSort(l, low, p-1)
		quickSort(l, p+1, high)

def binary_search(l: list, low: int, high: int, value: int) -> int:
	if low <= high:
		mid = low + (high - low) // 2

		if l[mid] == value:
			del l[mid]
			return value

		if l[mid] < value:
			return binary_search(l, mid + 1, high, value)
		elif l[mid] > value:
			return binary_search(l, low, mid - 1, value)

	else:
		return None

def pair_sum(l: list, s: int) -> list:
	result = []

	m = len(l) - 1

	quickSort(l, 0, m)

	# for i in l:
	# 	a = binary_search(l, 0, m, s - i)
	# 	if a is not None:
	# 		result.append((i, a))
	# 		m -= 1

	print(l)
	first = 0
	last = m

	while first < last:
		value = l[first] + l[last]
		if s == value:
			result.append((l[first], l[last]))
			first += 1
			last -= 1

		else:
			if s > value:
				first += 1
			else:
				last -= 1

	return result


array = [9, 34, 1, 43, 2, 3, 5, 5, 2, 1, 5, -13, -27, -9, 0, 7, 11]


print(pair_sum(array, 7))



