def find_frequency(l: list, word: str) -> int:
	h = {}

	for i in l:
		if i in h.keys():
			h[i] = h[i] + 1
		else:
			h[i] = 1

	if word in h.keys():
		return h[word]

	else:
		return 0


print(find_frequency(['hello', 'my', 'name', 'is', 'Bali', 'hello'], 'hello'))