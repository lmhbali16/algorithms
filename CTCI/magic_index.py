def magic_index_brute(array, n):
	if n >= len(array):
		return None
	if len(array) == 0 or n < 0:
		return None

	if array[n] == n:
		return array[n]
	else:
		return magic_index(array[:n], n-1)

a = [0, 1, 2, 4, 5, 6, 6, 6, 12, 123, 4234]

def magic_index(array, start, n):
	if start > n:
		return None

	mid = (n + start) // 2

	if array[mid] == mid:
		return mid
	elif array[mid] > mid:
		return  magic_index(array, start, mid - 1)
	else:
		return magic_index(array, mid + 1, n)

def magic_index_not_distinct(array, start, n):
	if start > n:
		return None

	mid = (n + start) // 2

	if array[mid] == mid:
		return mid

	leftIndex = max(mid-1, array[mid])
	left = magic_index_not_distinct(array, start, leftIndex)
	if left:
		return 	left

	rightIndex = max(mid+1, array[mid])
	right = magic_index_not_distinct(array, rightIndex, n)
	if right:
		return right

	return None

print(magic_index_not_distinct(a, 0, len(a)-1))