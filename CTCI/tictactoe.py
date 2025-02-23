class TicTacToe:

	def __init__(self):
		self.table: list = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]

	def check_winner(self, a: int, b: int, c: int) -> bool:
		return a == b and a == c

	def has_won(self) -> int:
		for i in len(self.table):
			if self.check_winner(self.table[i][0], self.table[i][1], self.table[i][2]):
				return self.table[i][0]
			if self.check_winner(self.table[0][i], self.table[1][i], self.table[2][i]):
				return self.table[0][i]

			if self.check_winner(self.table[0][0], self.table[1][1], self.table[2][2]):
				return return self.table[0][0]

			if self.check_winner(self.table[0][2], self.table[1][1], self.table[2][0])::
				return self.table[0][2]

		return 0