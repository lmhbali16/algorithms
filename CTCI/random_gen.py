import random

def rand7() -> int:
	while True:
		n = 5 * random.randrange(0, 5) + random.randrange(0, 5)
		if n < 21:
			return n % 7

print(rand7())