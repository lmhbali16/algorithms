def zero_matrix(matrix) -> list:
	row_index = set()
	column_index = set()

	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			if matrix[i][j] == 0:
				row_index.add(i)
				column_index.add(j)

	result = []

	for i in range(len(matrix)):
		row = []
		for j in range(len(matrix[0])):
			value = matrix[i][j]
			if i in row_index:
				value = 0
			if j in column_index:
				value = 0
			row.append(value)

		result.append(row)

	return result

def zero_matrix_better(matrix) -> list:

	flag_row = False
	flag_col = False

	for i in range(len(matrix[0])):
		if matrix[0][i] == 0:
			flag_row = True

	for i in range(len(matrix)):
		if matrix[i][0] == 0:
			flag_col = True

	for i in range(1, len(matrix)):
		for j in range(1, len(matrix[0])):
			if matrix[i][j] == 0:
				matrix[0][j] = 0
				matrix[j][0] = 0

	for i in range(1, len(matrix)):
		for j in range(1, len(matrix[0])):
			if matrix[0][j] == 0:
				matrix[i][j] = 0
			if matrix[i][0] == 0:
				matrix[i][j] = 0

	if flag_row:
		for i in range(len(matrix[0])):
			matrix[0][i] = 0

	if flag_col:
		for i in range(len(matrix)):
			matrix[i][0] = 0

	return matrix

matrix = [[1,2,35, 4, 4], [0,3,4,3,2], [0, 4,3, 4, 6], [4,0,3,4,5], [4,5,6,76,45]]

result = zero_matrix_better(matrix)

for i in result:
	print(i)