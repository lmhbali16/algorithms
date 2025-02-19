def sorted_matrix(l: [], v: int) -> tuple:
	col = len(l[0]) - 1
	row = 0


	while row < len(l) and col >= 0:
		if l[row][col] == v:
			return (row, col)
		elif l[row][col] > v:
			col -= 1
		else:
			row += 1

	return (-1, -1)

matrix = [[1,2,3,4,5], [6,7,8,9,10],[11,12,13,14,15], [16,17,18,19,20]]

print(sorted_matrix(matrix, 18))