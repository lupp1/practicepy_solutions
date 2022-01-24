# Make a two-player Rock-Paper-Scissors game. 
# Rock beats scissors
# Scissors beats paper
# Paper beats rock

def plays():
    while True:

        player1 = str(input('Insert player 1 move: ')).lower().strip()
        player2 = str(input('Insert player 2 move: ')).lower().strip()

        if player1 and player2 in ['rock', 'paper', 'scissors']:
            if player1 == 'rock' and player2 == 'scissors':
                print('Player 1 won.')
                break

            elif player1 == 'scissors' and player2 == 'rock':
                print('Player 2 won.')
                break

            if player1 == 'scissors' and player2 == 'paper':
                print('Player 1 won.')
                break

            elif player1 == 'paper' and player2 == 'scissors':  
                print('Player 2 won.')  
                break

            if player1 == 'paper' and player2 == 'rock':
                print('Player 1 won.')
                break
        
            elif player1 == 'rock' and player2 == 'paper':  
                print('Player 2 won.')  
                break

            if player1 == player2:
                print('Tie.')
                continue
        else:
            print('Insert a valid move.')
            plays()
            break
            
plays()