def sum_swap(listA: list, listB: list) -> list:
	sumA = 0
	for i in listA:
		sumA += i

	sumB = 0
	for j in listB:
		sumB += j

	sumAll = sumB + sumA
	mid = sumAll // 2
	
	diff = 0
	if sumB > mid:
		diff = sumB - mid
	else:
		diff = sumA - mid

	listBTable = {}
	for i in listB:
		listBTable[i] = True

	for i in listA:
		if i >= diff:
			if i-diff in listBTable.keys() and listBTable[i-diff]:
				return [i, i-diff]
		else:
			if diff+i in listBTable.keys() and listBTable[diff+i]:
				return [i, diff+i]

	return []

b = [4,1,2,1,1,2]
a = [3,6,3,3]

print(sum_swap(a, b))