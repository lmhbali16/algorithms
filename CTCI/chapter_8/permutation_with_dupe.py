def permutate(prefix, remainder, result):
	if remainder == "" and prefix not in result:
		result.append(prefix)

	for i in range(len(remainder)):
		before = remainder[:i]
		fp = remainder[i]
		after = remainder[i+1:]

		permutate(prefix+fp, before+after, result)



def permutate_with_dupe(phrase: str):
	if len(phrase) == 0:
		return []

	result = []

	permutate("", phrase, result)

	return result

print(len(permutate_with_dupe("aabcdd")))