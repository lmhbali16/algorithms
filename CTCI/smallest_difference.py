def merge_sort(l: list) -> list:

	if len(l) <= 1:
		return l

	mid = len(l) // 2
	left = merge_sort(l[:mid])
	right = merge_sort(l[mid:])

	i = 0
	j = 0

	result = []

	while i < len(left) and j < len(right):
		if left[i][0] <= right[j][0]:
			result.append(left[i])
			i += 1
		else:
			result.append(right[j])
			j += 1

	while i < len(left):
		result.append(left[i])
		i += 1

	while j < len(right):
		result.append(right[j])
		j += 1

	return result

def format(l: list, f: str) -> list:
	result = []
	for i in l:
		result.append((i, f))

	return result


def smallest_diff(n: list, m: list) -> tuple:
	merged = merge_sort(format(n, 'l') + format(m, 'r'))

	if len(merged) <= 2:
		return ()

	

	i = 1
	j = 0

	while merged[i][1] == merged[j][1]:
		i += 1

	if i != 1:
		j = 1

	result = (merged[i], merged[j])

	while i < len(merged):
		if merged[i][1] != merged[j][1]:
			if merged[i][0] - merged[j][0] <= result[0][0] - result[1][0]:
				result = (merged[i], merged[j])
				
			if j + 1 < i:
				j += 1
			else:
				j += 1
				i += 1
		else:
			i += 1 

	return (result[0][0], result[1][0])


print(smallest_diff([23, 127, 235, 19, 1],[1, 3,15, 11, 2]))

