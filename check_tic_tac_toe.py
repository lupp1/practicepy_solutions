# Check Tic Tac Toe www.practicepython.org/exercise/2015/11/16/26-check-tic-tac-toe.html
# Your task this week: given a 3 by 3 list of lists that represents a Tic Tac Toe game board, 
# tell me whether anyone has won, and tell me which player won, if any. 
# A Tic Tac Toe win is 3 in a row - either in a row, a column, or a diagonal. 
# Don’t worry about the case where TWO people have won - assume that in every board there will only be one winner.

def checkGrid(grid):
	"""Code took from practicepy, not mine."""

	for x in range(0,3):
		row = set([grid[x][0],grid[x][1],grid[x][2]])
		if len(row) == 1 and grid[x][0] != 0:
			return grid[x][0]


	for x in range(0,3):
		column = set([grid[0][x],grid[1][x],grid[2][x]])
		if len(column) == 1 and grid[0][x] != 0:
			return grid[0][x]


	diag1 = set([grid[0][0],grid[1][1],grid[2][2]])
	diag2 = set([grid[0][2],grid[1][1],grid[2][0]])
	if len(diag1) == 1 or len(diag2) == 1 and grid[1][1] != 0:
		return grid[1][1]

	return False

winner_is_2 = [[2, 2, 0],
	[2, 1, 0],
	[2, 1, 1]]
winner_is_1 = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 1]]

winner_is_also_1 = [[0, 1, 0],
	[2, 1, 0],
	[2, 1, 1]]

no_winner = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 2]]

also_no_winner = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 0]]

print(checkGrid())