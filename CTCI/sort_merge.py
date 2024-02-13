def sort_merge(list1, list2):
	# assume list1 is longer

	idx_last = -1

	j = len(list2) - 1

	combined = len(list1) - 1

	for i in list1:
		if i is not None:
			idx_last += 1

	while j >= 0:
		if idx_last >= 0 and list1[idx_last] > list2[j]:
			list1[combined] = list1[idx_last]
			idx_last -= 1
		else:
			list1[combined] = list2[j]
			j -= 1
		combined -= 1

a = [1,4,5,6,7,9,11,14, None, None, None, None, None]

b = [2,3, 8, 16, 18]

sort_merge(a, b)

print(a)