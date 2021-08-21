'''
 Given a string, write a function to check if it is a permutation of a palindrome.
 A palindrome is a word or phrase that is the same forwards and backwards.
 A permutation is a rearrangement of letters.
 The palindrome does not need to be limited to just dictionary words.

example:

input: Tact Coa

output: False
'''

def palindrom(word: str) -> bool:
	word_lower = word.lower()

	i = 0
	j = len(word_lower) -1
	valid_start = ord('a')
	valid_end = ord('z') 

	while i < j:
		if ord(word_lower[i]) > valid_end or ord(word_lower[i]) < valid_start:
			i += 1
			continue
		if ord(word_lower[j]) > valid_end or ord(word_lower[j]) < valid_start:
			j -= 1
			continue

		if word_lower[i] != word_lower[j]:
			return False
		i += 1
		j -= 1
	return True
