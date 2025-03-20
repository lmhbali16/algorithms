def count_of(pattern: str, char: str) -> int:
	result = 0
	for i in pattern:
		if char == i:
			result += 1

	return result

def build_frompattern(pattern: str, first: str, second: str) -> str:
	s = ""
	f = pattern[0]

	for i in pattern:
		if i == f:
			s += first
		else:
			s += second

	return s

def matching_pattern(pattern: str, value: str) -> bool:
	if len(value) == 0:
		return len(value) == 0

	main_char = pattern[0]
	size = len(value)
	alt_char = 'b' if main_char == 'a' else 'a'
	main_char_count = count_of(pattern, main_char)
	alt_char_count = len(pattern) - main_char_count
	max_size = size // main_char_count

	first_alt = 0
	for i in pattern:
		if i != alt_char:
			first_alt += 1
		else:
			break

	for i in range(0, max_size+1):
		remaining_len = size - i * main_char_count
		first = value[:i]

		
		if alt_char_count == 0 or remaining_len % alt_char_count == 0:
			alt_idx = first_alt * i
			alt_size = 0 if alt_char_count == 0 else remaining_len // alt_char_count
			second = "" if alt_char_count == 0 else value[alt_idx: alt_size+alt_idx]

			cand = build_frompattern(pattern, first, second)
			if cand == value:
				return True

	return False



print(matching_pattern('b', 'catcatgocatgo'))