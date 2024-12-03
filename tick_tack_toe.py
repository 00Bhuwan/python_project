import random

#for the board
def display_board(board):
    print(board[1], '|', board[2], '|', board[3])
    print('---------')
    print(board[4], '|', board[5], '|', board[6])
    print('---------')
    print(board[7], '|', board[8], '|', board[9])

def user_input():
    marker = ''
    while marker not in ['X', '0']:
        marker = input('Would you like to be X or 0: ').upper()

    if marker == 'X':
        return('X', '0')   #player1 is X and player2 is 0  
    
    else:
        return('0', 'X')   #player1 is 0 and player2 is X


def place_marker(board, marker, position):
    board[position] = marker

def win_check(board, mark):
    return(
        (board[4] == board[5] == board[6] == mark) or
        (board[7] == board[8] == board[9] == mark) or
        (board[1] == board[2] == board[3] == mark) or
        (board[1] == board[4] == board[7] == mark) or
        (board[2] == board[5] == board[8] == mark) or
        (board[3] == board[6] == board[9] == mark) or
        (board[1] == board[5] == board[9] == mark) or
        (board[3] == board[5] == board[7] == mark) 
    )

def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'

def space_check(board, position):
    return board[position] == ' '

def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True

def player_choice(board):
    position = 0

    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        try:
            position = int(input('Choose your next position (1-9): '))
        except ValueError:
            print("Invalid Input. Please enter a number between 1 and 9.")

    return position

def replay():
    return input('Do you want to play again? Enter Yes or No: '). lower().startswith('y')

print("Welcome to the TIC TAC TOE")
while True:
    #play the game
    the_board = [' '] * 10
    player1_marker, player2_marker = user_input()

    turn = choose_first()
    print(turn + ' will go first.')

    play_game = input('Ready to play? y or n?: ').lower()
    if play_game == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            display_board(the_board)
            #to choose a position
            position = player_choice(the_board)
            #to place marker on the position
            place_marker(the_board, player1_marker, position)
            #to check if won
            if win_check(the_board, player1_marker):
                display_board(the_board)
                print('Player 1 has won!!!')
                break
            
            #to check tie
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('TIE game!')
                    break
                else:
                    turn = 'Player 2'
        
        else:
            display_board(the_board)
            #to choose a position
            position = player_choice(the_board)
            #to place marker on the position
            place_marker(the_board, player2_marker, position)
            #to check if won
            if win_check(the_board, player2_marker):
                display_board(the_board)
                print('Player 2 has won!!!')
                break
            
            #to check tie
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('The game is draw!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break