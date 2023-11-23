def locker():
	n = [True] * 100

	for i in range(2,101):
		t = i - 1
		for j in range(t, 100, i):
			n[j] = not n[j]

	result = 0

	for i in n:
		if i == True:
			result += 1

	print(result)
locker()