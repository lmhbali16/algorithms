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


print(mergeSort('jlakhfduweraswqqa:@$#a;abbvcccxc'))