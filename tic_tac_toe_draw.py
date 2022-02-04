# Tic Tac Toe Draw wwww.practicepython.org/exercise/2015/11/26/27-tic-tac-toe-draw.html

def player_1_move():
    move_1 = input('Player 1, what is your move? Type the coordinates - (1, 1), (1, 2)...\n')
    return move_1

def player_2_move():
    move_2 = input('Player 2, what is your move? Type the coordinates - (1, 1), (1, 2)...\n')
    return move_2

def play_game(board):
    """Tic-tac-toe Game
    Can't return tie games
    """
    while True: 
        
        print(board[0], board[1], board[2], sep='\n')
        x = player_1_move().strip().split(',')
        y = player_2_move().strip().split(',')
        board[int(x[0]) - 1][int(x[1]) - 1] = 'X'
        board[int(y[0]) - 1][int(y[1]) - 1] = 'O'

        if x == y:
            print('Please, insert your move into another coordinate.')
            restart()

        if checkGrid(board) == 'X':
            print('Player 1 won.')
            break
        
        elif checkGrid(board) == 'O':
            print('Player 2 won')
            break    

        
def checkGrid(grid):
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

def restart():
    cleaner_board = [[0, 0, 0],
	[0, 0, 0],
	[0, 0, 0]]
    play_game(cleaner_board)
    
if __name__ == '__main__':
    start_board = [[0, 0, 0],
	[0, 0, 0],
	[0, 0, 0]]
    play_game(start_board)
    