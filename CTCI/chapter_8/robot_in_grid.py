def visit(grid, row, col, path, visited) -> bool:
	if row >= len(grid) or col >= len(grid[0]) or row < 0 or col < 0:
		return False

	if (row, col) in path:
		return False

	isTopLeft = row == 0 and col == 0

	if isTopLeft or visit(grid, row-1, col, path, visited) or visit(grid, row, col-1, path, visited):
		path.append((row, col))
		return True

	visited.append((row, col))

	return False


def find_path(grid, row, col) -> list:
	if grid == None or len(grid) == 0:
		return path

	path = []
	visited = []

	if visit(grid, len(grid)-1 , len(grid[-1])-1, path, visited):
		return path

	return []