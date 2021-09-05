'''
Implement a method to perform basic string compression using the counts of repeated characters.
For example, the string aabcccccaaa would become a2blc5a3. If the "compressed" string would not
become smaller than the original string, your method should return
the original string. You can assume the string has only uppercase and lowercase letters (a - z).
'''

def pick_shortest(word_number: str, word_original: str) -> str:
	if len(word_original) < len(word_number):
		return word_original

	else:
		return word_number

# Okay, this is not the task but harder
def string_compression(word: str) -> str:
	result = ""
	current_letter = word[0]
	count = 0

	i = 0
	j = 0

	while i < len(word):

		if word[i] == current_letter:
			count += 1

		else:

			new_string = current_letter + str(count)
			new_string = pick_shortest(new_string, word[j:i])
			result += new_string
			count = 1
			current_letter = word[i]
			j = i
		i += 1

	return result
	

def string_compression_original(word: str) -> str:
	result = ""
	current_letter = word[0]
	count = 0

	i = 0
	j = 0

	while i < len(word):

		if word[i] == current_letter:
			count += 1

		else:

			new_string = current_letter + str(count)
			result += new_string
			count = 1
			current_letter = word[i]
			j = i
		i += 1

	if len(result) < len(word):
		return result
	return word

print(string_compression('aaaabbbffFFFLLDDDWW'))
print(string_compression_original('abdfDFE'))