'''
Given two strings,write a method to decide if one is a permutation of the
other.

'''



def check_permutation1(string1: str, string2: str) -> bool:
	'''
	Using dictionary, check permutation

	Parameters:
		string1 (str): first word
		string2 (str): second word

	Returns:
		bool: whether they are each other's permutation

	'''
	map_string1 = {}

	for i in string1:
		if i not in map_string1:
			map_string1[i] = 1

		else:
			map_string1[i] = map_string1[i] + 1

	for i in string2:
		if i in map_string1:
			if map_string1[i] == 1:
				del map_string1[i]
			else:
				map_string1[i] = map_string1[i] - 1

		else:
			return False

	if len(map_string1) > 0:
		return False

	return True

def merge_sort(word: str) -> bool:
	'''
	Merge sort algorithm of string

	Parameter:
		word (str): word to be sorted

	Returns:
		str: sorted string

	'''

	if len(word) == 1:
		return word

	middle = len(word) // 2
	right = word[middle:]
	left = word[:middle]


	sorted_left = merge_sort(left)
	sorted_right = merge_sort(right)
	i = 0
	j = 0
	

	result = ""
	while i < len(sorted_right) and j < len(sorted_left):
		if sorted_left[j] > sorted_right[i]:
			result += sorted_right[i]
			i += 1
		else:
			result += sorted_left[j]
			j += 1

	while i < len(sorted_right):
		result += sorted_right[i]
		i += 1

	while j < len(sorted_left):
		result += sorted_left[j]
		j += 1

	return result

def check_permutation2(string1, string2):
	'''
	check permutation of two strings without dictionary

	Parameters:
		string1 (str): first word
		string2 (str): second word

	Returns:
		bool: whether the two words are permutations of each other

	'''
	sorted_string1 = merge_sort(string1)
	sorted_string2 = merge_sort(string2)

	if len(sorted_string1) != len(sorted_string2):
		return False

	for i in range(len(sorted_string1)):
		if sorted_string1[i] != sorted_string2[i]:
			return False

	return True

string1 = "sdfasdfdfaaasf"

string2 = "asasdfasafdf"

print(check_permutation1(string1, string2))
print(check_permutation2(string1, string2))