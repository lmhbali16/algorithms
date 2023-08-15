'''
Given an image represented by an NxN matrix,
where each pixel in the image is 4 bytes,
write a method to rotate the image by 90 degrees.
Can you do this in place?
'''

# We will assume the matrix input is in the corrext format. Otherwise just check.
def rotate_matrix(matrix: list) -> list:
	#rotate counter-clockwise
	result = []
	n = len(matrix)
	for i in range(n-1, -1, -1):
		result_row = [j[i] for j in matrix]
		result.append(result_row)

	return result


# We will assume the matrix input is in the corrext format. Otherwise just check.
def rotate_matrix_clockwise(matrix: list) -> list:
	#rotate clockwise
	result = []
	n = len(matrix)
	for i in range(n-1, -1, -1):
		result_row = [matrix[j][n-1-i] for j in range(n-1, -1, -1)]
		result.append(result_row)

	return result

def rotate_matrix_45(matrix: list) -> list:

	result = []

	for i in range(0, len(matrix)):

		row = []
		for j in range(len(matrix)-1, -1, -1):
			row.append(matrix[j][i])
		result.append(row)

	return result


			

test = [[1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15], [16,17,18,19,20], [21,22,23,24,25]]
print(test)
print('\n')
test_45 = rotate_matrix_45(test)
print(test_45)
print('\n')
test_90 = rotate_matrix_45(test_45)
print(test_90)
	