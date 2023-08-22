def isSubstring(s1: str, s2: str) -> bool:
	start_idx = 0

	if len(s1) != len(s2):
		return False

	for i in range(len(s2)):
		if s2[i] == s1[0]:
			start_idx = i

	
	current_idx = start_idx

	for i in range(len(s1)):
		if current_idx >= len(s2):
			current_idx = 0

		if s1[i] != s2[current_idx]:
			return False

		current_idx += 1

	return True

print(isSubstring('waterbottle', 'efbottlewat'))