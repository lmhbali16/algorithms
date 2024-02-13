GRID_SIZE = 8

def place_queens(row: int, columns: list, results: list):
	if row == GRID_SIZE:
		results.append(columns.copy())
	else:
		for col in range(GRID_SIZE):
			if check_valid(columns, row, col):
				columns[row] = col
				place_queens(row + 1, columns, results)

def check_valid(columns, row, col):
	for row2 in range(row):
		column2 = columns[row2]

		if col == column2:
			return False

		col_distance = abs(column2 - col)
		row_distance = abs(row2 - row)

		if col_distance == row_distance:
			return False

	return True

result = []

place_queens(0, [None] * GRID_SIZE, result)

print(result)

