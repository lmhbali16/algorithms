def calculate(n, denoms, current, storage):
	if storage[n][current] > 0:
		return storage[current][current]

	if current >= len(denoms) - 1:
		return 1

	denom_amount = denoms[current]

	w = 0
	i = 0
	while i * denom_amount <= n:
		amount_remaining = n - i * denom_amount
		w += calculate(amount_remaining, denoms, current + 1, storage)
		i += 1

	storage[n][current] = w
	return w

def coin_num(n):
	denoms = [25, 10, 5, 1]
	storage = []
	for i in range(n+1):
		storage.append([0 for j in range(len(denoms))])

	return calculate(n, denoms, 0, storage)

print(coin_num(10))