def hit(guess: str, solution: str) -> tuple:
	placement = {}
	exist = {}

	for i in range(len(solution)):
		exist[solution[i]] = True
		placement[i] = solution[i]

	pseudo = 0
	hit = 0

	already_guessed = {}

	for i in range(len(guess)):
		if guess[i] in exist.keys():
			if placement[i] == guess[i]:
				hit += 1
			elif guess[i] not in already_guessed.keys():
				pseudo += 1

	return (pseudo, hit)


print(hit('GRYB', 'BRYY'))
