'''
Write a method to replace all spaces in a string with '%20'.
You may assume that the string has sufficient space at the end
to hold the additional characters,
and that you are given the "true" length of the string.
'''

def urlfy(phrase: str, length: int) -> str:
	is_char = False

	result = ''

	i = 0
	phrase_idx = 0

	while phrase_idx < length and i < len(phrase):
		if phrase[i] != ' ':
			is_char = True
			result += phrase[i]

			i += 1
			phrase_idx += 1


		elif phrase[i] == ' ' and is_char:
			is_char = False
			result += '%20'
			phrase_idx += 1
			i += 1

		else:
			i += 1

	if result[-1] == " ":
		return result[:-1]

	return result


print(urlfy("    MR. Smith Orylie   df   sdf    ", 23))