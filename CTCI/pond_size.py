def find_water(pond: list, visited: dict, y: int, x: int) -> int:
	if x < 0 or x >= len(pond[0]):
		return 0

	if y < 0 or y >= len(pond):
		return 0


	if pond[y][x] != 0:
		return 0

	if (x, y) in visited:
		return 0

	visited.add((x, y))



	return 1 + find_water(pond, visited, y + 1, x) + find_water(pond, visited, y - 1, x) + find_water(pond, visited, y, x + 1) + find_water(pond, visited, y, x - 1) + find_water(pond, visited, y + 1, x + 1) + find_water(pond, visited, y + 1, x - 1) + find_water(pond, visited, y - 1, x + 1) + find_water(pond, visited, y - 1, x - 1)

def pond_size(pond: list) -> list:
	visited = set()

	if len(pond) == 0:
		return []

	c = len(pond[0])
	r = len(pond)

	result = []

	for i in range(r):
		for j in range(c):
			p = find_water(pond, visited, i, j)
			if p != 0:
				result.append(p)

	return result

a = [[0,2,1,0], [0,1,0,1], [1,1,0,1], [0,1,0,1]]

print(pond_size(a))



