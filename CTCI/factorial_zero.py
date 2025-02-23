def factorial_zero(n: int) -> int:
	result = 0

	if n < 5:
		return 0

	i = 5

	while n // i > 0:
		result += (n // i)
		i *= 5

		print(result)

	return int(result)

def factor5(i: int) -> int:

	count  = 0

	while i // 5 > 0:
		count += 1
		i //= 5

	return count

def factorial_zero2(n: int) -> int:
	result = 0

	for i in range(n):
		if i % 5 == 0:
			result += factor5(i)

	return int(result)
	


print(factorial_zero2(40))