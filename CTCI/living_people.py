class People:

	def __init__(self, birth: int, death: int):
		self.birth = birth
		self.death = death


def merge_sort_birth(p: list):

	if len(p) <= 1:
		return p

	mid = len(p) // 2
	left = merge_sort_birth(p[:mid])
	right = merge_sort_birth(p[mid:])

	i = 0
	j = 0

	result = []
	while i < len(left) and j < len(right):
		if left[i].birth <= right[j].birth:
			result.append(left[i])
			i += 1
		else:
			result.append(right[j])
			j += 1

	while i < len(left):
		result.append(left[i])
		i += 1

	while j < len(right):
		result.append(right[j])
		j += 1

	return result

def merge_sort_death(p: list):

	if len(p) <= 1:
		return p

	mid = len(p) // 2
	left = merge_sort_birth(p[:mid])
	right = merge_sort_birth(p[mid:])

	i = 0
	j = 0

	result = []
	while i < len(left) and j < len(right):
		if left[i].death <= right[j].death:
			result.append(left[i])
			i += 1
		else:
			result.append(right[j])
			j += 1

	while i < len(left):
		result.append(left[i])
		i += 1

	while j < len(right):
		result.append(right[j])
		j += 1

	return result


def living_people(p: list):
	birth = [i.birth for i in merge_sort_birth(p)]
	death = [i.death for i in merge_sort_death(p)]

	birth_idx = 0
	death_idx = 0

	max_alive = 0
	currently_alive = 0
	max_year = 1900


	while birth_idx < len(birth):
		if birth[birth_idx] <= death[death_idx]:
			currently_alive += 1
			if currently_alive > max_alive:
				max_alive = currently_alive
				max_year = birth[birth_idx]

			birth_idx += 1
		else:
			currently_alive -= 1
			death_idx += 1

	return max_year

p = [People(1901, 1924), People(1921, 1950), People(1912, 1930), People(1920, 1949),People(1918, 1924), People(1931, 1934), People(1950, 1984)]

print(living_people(p))




