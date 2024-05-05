def search_rotated_array(numbers: list[int], search_num: int) -> int:
	i = 0

	for j in range(len(numbers) - 1):
		if numbers[j] > numbers[j+1]:
			break
		i += 1
	
	j = i
	result = 0
	while True:
		if numbers[j] == search_num:
			break
		else:
			result += 1

			if j + 1 == i:
				return None
			elif j + 1 >= len(numbers):
				j = 0
			else:
				j += 1
	return i + result

numbers = [15,16,19, 20,25,1,3,4,5,7,10,14]
print(search_rotated_array(numbers, 5))