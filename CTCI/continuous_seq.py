def cont_seq(l: list) -> int:
	highest = l[0]

	mem = {}

	for i in l:
		a = str(i)
		mem[a] = i

	for i in range(2, len(l)+1):
		for j in range(i, len(l)+1):
			r = j-i

			a = " ".join(map(str, l[r: j-1]))
			new = " ".join(map(str, l[r: j]))
			prev = mem[a]

			mem[new] = prev + l[j-1]

	highest = None
	for i in mem.keys():
		if highest is None:
			highest = mem[i]

		else:
			if highest < mem[i]:
				highest = mem[i]

	return highest


print(cont_seq([2, -8, 3, -2, 4, -10]))