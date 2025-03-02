def sub_sort(l: list) -> tuple:
	current_high = l[-1]
	highest = None

	for i in range(1, len(l)+1):
		idx = len(l) - i
		value = l[idx]

		if current_high >= value:
			current_high = value
		else:
			if (highest is not None and value > highest) or highest is None:
				highest = value
			
			current_high = value
			
			
	m = len(l) - 1
	if highest is None:
		return ()

	for i in range(1, len(l)+1):
		idx = len(l) - i
		if l[idx] >= highest:
			m -= 1
		else:
			break

	current_low = l[0]
	lowest = None

	for i in range(len(l)):
		value = l[i]

		if current_low <= value:
			current_low = value
		else:
			if (lowest is not None and value < lowest) or lowest is None:
				lowest = value
			current_low = value

	n = 0

	print(lowest)

	for i in range(len(l)):
		value = l[i]
		if value <= lowest:
			n += 1
		else:
			break


	return (n, m)

print(sub_sort([1, 2, 4, 7, 8, 9, 11, 12, 10, 14, 16, 18, 19]))

