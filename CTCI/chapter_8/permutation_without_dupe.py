def premutation(phrase: str, prem_list: list):
	if len(phrase) == 0:
		return prem_list
	elif len(phrase) == 1:
		prem_list.append(phrase)

		return prem_list
	else:
		sub_perm = premutation(phrase[:-1], prem_list)
		letter = phrase[-1]
		result = []
		for perm in sub_perm:
			result.append(letter + perm)
			result.append(perm + letter)
			for i in range(1, len(perm)):
				fp = perm[:i]
				result.append(perm[:i] + letter + perm[i:])

		return result

def permutate(prefix, remainder, result):
	if remainder == "":
		result.append(prefix)

	for i in range(len(remainder)):
		before = remainder[:i]
		after = remainder[i+1:]
		letter = remainder[i]

		permutate(prefix+letter, before+after, result)

def permutation_better(phrase):
	result = []

	permutate("", phrase, result)
	return result

print(len(premutation('hitr', [])))
print(len(permutation_better('hitr')))