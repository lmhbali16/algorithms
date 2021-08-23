'''
There are three types of edits that can be performed on strings:
insert a character, remove a character, or replace a character.
Given two strings, write a function to check if they are one edit (or zero edits) away.

Example:

pale, ple -> true
pales, pale -> true
pale, bale -> true
pale, bake -> false
'''

def one_away(word: str, edit: str) -> bool:
	diff = 0
	if abs(len(word) - len(edit)) > 1:
		return False


	j = 0
	i = 0
	while diff < 2 and i < len(word) and j < len(edit):
		if word[i] != edit[j]:
			diff += 1

			if i + 1 < len(word):
				if word[i+1] == edit[j]:
					i += 1

			if j + 1 < len(edit):
				if word[i] == edit[j+1]:
					j += 1

		i += 1
		j += 1
	if j < len(edit) and i >= len(word):
		diff += 1
	if diff > 1:
		return False


	return True

print(one_away("apple", "apple"))
print(one_away("pale", "ple"))
print(one_away("pales", "pale"))
print(one_away("pale", "bale"))
print(one_away("pale", "bake"))