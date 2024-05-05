def merge_sort(phrase: str) -> str:
	if len(phrase) == 1:
		return phrase

	mid_idx: int = len(phrase) // 2

	left_phrase: str = phrase[:mid_idx]
	right_phrase: str = phrase[mid_idx:]

	sorted_left_phrase = merge_sort(left_phrase)
	sorted_right_phrase = merge_sort(right_phrase)

	j = 0
	i = 0

	result = ""

	while i < len(sorted_left_phrase) and j < len(sorted_right_phrase):
		if ord(sorted_left_phrase[i]) < ord(sorted_right_phrase[j]):
			result += sorted_left_phrase[i]
			i += 1
		else:
			result += sorted_right_phrase[j]
			j += 1

	while i < len(sorted_left_phrase):
		result += sorted_left_phrase[i]
		i += 1

	while j < len(sorted_right_phrase):
		result += sorted_right_phrase[j]
		j += 1

	return result

def group_anagrams(anagrams: list[str]) -> list[str]:
	phrases_map: dict = {}

	for idx in range(len(anagrams)):
		sorted_phrase = merge_sort(anagrams[idx])
		if sorted_phrase in phrases_map:
			phrases_map[sorted_phrase].append(idx)
		else:
			phrases_map[sorted_phrase] = [idx]

	result = []

	for keys in phrases_map.keys():
		list_idx = phrases_map[keys]
		for idx in list_idx:
			result.append(anagrams[idx])

	return result

anagrams = ['fdefds', 'ewfdw', 'ffedds', 'wdefw', 'dasf', 'efdfds']

print(group_anagrams(anagrams))

