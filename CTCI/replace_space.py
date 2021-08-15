'''
Write a method to replace all spaces in a string with '%20'.
You may assume that the string has sufficient space at the end to hold
the additional characters,and that you are given the "true" length of the string.
'''

def replace_string(word: str, length: int) -> str:
	result = ""
	iterate = len(word)

	if len(word) > length:
		iterate = length

	for i in range(iterate):
		if word[i] == " ":
			result += '%20'
		else:
			result += word[i]


	return result

print(replace_string("Mr John Smith      ", 13))