# Is Unique: Implement an algorithm to determine if a string has all unique characters.
# What if you cannot use additional data structures?

def mergeSort(word: str) -> str:
    '''
    Merge sort a string.

    Parameter:
        word (str): a string character

    Returns:
        str: returns a sorted string
    '''

    if len(word) == 1:
        return word


    mid = len(word) // 2

    left = word[:mid]
    right = word[mid:]
    result = ''

    left = mergeSort(left)
    right = mergeSort(right)
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result += left[i]
            i += 1

        else:
            result += right[j]
            j+=1

    while i < len(left):
        result += left[i]
        i += 1

    while j < len(right):
        result += right[j]
        j += 1

    return result

def unique1(word: str) -> bool:
	table = {}

	for char in word:
		if char not in table:
			table[char] = 1

		else:
			return False

	return True


def unique2(word: str) -> bool:
	sorted_word = mergeSort(word)

	for i in range(len(sorted_word) - 1):
		if sorted_word[i] == sorted_word[i + 1]:
			return False

		return True


print(unique2('sfgawetasdfqpoui'))

