'''
Given a string, write a function to check if it is a permutation of a palindrome.
A palindrome is a word or phrase that is the same forwards and backwards.
A permutation is a rearrangement of letters.
The palindrome does not need to be limited to just dictionary words.
'''
def partition(phrase: list, low: int, high: int) -> int:
	pivot = phrase[high]

	j = low - 1

	for i in range(low, high):
		if phrase[i] <= pivot:
			j += 1

			phrase[i], phrase[j] = phrase[j], phrase[i]

	phrase[j + 1], phrase[high] = phrase[high], phrase[j + 1]

	return j + 1

def quicksort(phrase_list: list, low: int, high: int):
	if low > high:
		return

	pi = partition(phrase_list, low, high)

	quicksort(phrase_list, low, pi - 1)
	quicksort(phrase_list, pi + 1, high)


def palindrom_perm(phrase: str) -> bool:
	phrase_list = list(phrase.lower())
	quicksort(phrase_list, 0, len(phrase_list) - 1)

	phrase_list = [ i for i in phrase_list if i != ' ']

	if len(phrase_list) % 2 == 0:
		is_even = False
		current_char = phrase_list[0]

		for i in phrase_list[1:]:
			if i == current_char:
				is_even = not is_even

			elif i != current_char and is_even:
				is_even = False
				current_char = i

			elif i != current_char and not is_even:
				return False

	else:
		uneven_char = ''
		is_even = False
		current_char = phrase_list[0]

		for i in phrase_list[1:]:
			if i == current_char:
				is_even = not is_even

			elif i != current_char and is_even:
				is_even = False
				current_char = i

			elif i != current_char and not is_even:
				if uneven_char == '':
					uneven_char = current_char
					current_char = i
				else:
					current_char = i

		if uneven_char != '' and not is_even:
			return False
	return True


def palindrom_perm_hash(phrase: list) -> bool:
	phrase = [i.lower() for i in phrase if i != ' ']

	table = {}

	for i in phrase:
		if i in table:
			table[i] = table[i] + 1
		else:
			table[i] = 1

	if len(phrase) % 2 == 0:
		for key, value in table.items():
			if value % 2 != 0:
				return False

		return True

	else:
		uneven_char = ''

		for key, value in table.items():
			if value % 2 != 0:
				if uneven_char == '':
					uneven_char = key
				else:
					return False

		return True


print(palindrom_perm_hash('Tact Co'))
