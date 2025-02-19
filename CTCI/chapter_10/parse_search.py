def binary_search(l: [], lower: int, high: int, s: str) -> int:
	if lower > high:
		return -1

	mid = (lower + high) // 2

	if l[mid] == "":
		lower_mid = mid - 1
		upper_mid = mid + 1
		
		while True:
			if lower_mid < lower and upper_mid > high:
				return -1

			if lower_mid >= lower and l[lower_mid] != "":
				mid = lower_mid
				break
			elif upper_mid <= high and l[upper_mid] != "":
				mid = upper_mid
				break

			lower_mid += 1
			upper_mid += 1


	if l[mid] == s:
		return mid

	elif l[mid] < s:
		return binary_search(l, mid + 1, high, s)
	elif l[mid] > s:
		return binary_search(l, lower, mid-1, s)






def parse_search(l: [], s: str) -> int:
	return binary_search(l, 0, len(l), s)

print(parse_search(["at", "", "", "", "ball", "", "", "car", "", "dad", "", ""], "car"))