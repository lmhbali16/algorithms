def create_board(l: list, board: list, k) -> None:
	if k <= 0:
		l.append(board)
		return

	a = board + ['s']
	b = board + ['l']

	create_board(l, a, k-1)
	create_board(l, b, k-1)


def diving_broad(l: list, k: int) -> list:
	if k <= 0:
		return []

	
	create_board(l, ['s'], k-1)
	create_board(l, ['l'], k-1)


	return l

l = []
print(len(diving_broad(l, 4)))