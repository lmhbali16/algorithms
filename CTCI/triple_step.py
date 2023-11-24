def triple_step(n) -> int:
	if n < 0:
		return 0
	if n == 0:
		return 1
	elif n == 1:
		return 1
	elif n == 2:
		return 2

	return triple_step(n-1) + triple_step(n-2) + triple_step(n-3)