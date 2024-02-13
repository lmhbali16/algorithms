def get_subset(array, subsets, idx):
	if idx == len(array):
		return subsets

	if idx == 0:
		subsets.append({array[idx]})
		return get_subset(array, subsets, idx+1)

	finish = len(subsets)

	for i in range(finish):
		new_subset = subsets[i].copy()
		new_subset.add(array[idx])
		subsets.append(new_subset)

	subsets.append({array[idx]})

	return get_subset(array, subsets, idx+1)

print(len(get_subset([1,2,3,4], [], 0)))