def multiply(smaller, bigger) -> int:
	if smaller == 0:
		return 0
	elif smaller == 1:
		return bigger

	if smaller % 2 == 1:
		half = (smaller - 1) >> 1

		halfprod = multiply(half, bigger)

		return halfprod + halfprod + bigger
	else:
		half = smaller >> 1
		halfprod = multiply(half, bigger)

		return halfprod + halfprod



def recursive_multiply(x, y) -> int:
	smaller = x if x < y else y
	bigger = x if x >= y else y

	return multiply(smaller, bigger)

print(recursive_multiply(9, 15))