# the game board
# take user input
# check for win or tie
# switch
# check for win or tie
import random

board = ["-"]* 10
current_player = 'X'
game_on = True

def disp_board(board):
    print(board[1] + '|' + board[2] + '|' + board[3])
    print('--------')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('--------')
    print(board[7] + '|' + board[8] + '|' + board[9])

def user_input(board):
    try:
        choice = int(input('Enter a number (1-9): '))
        if choice >=1 and choice <=9 and board[choice] =='-':
            board[choice] = current_player
        else:
            print('The position is already occupied.')

    except ValueError:
        print('Enter valid input')
    
def check_win(board):
    
    if(
        (board[4] == board[5] == board[6] == 'X') or
        (board[7] == board[8] == board[9] == 'X') or
        (board[1] == board[2] == board[3] == 'X') or
        (board[1] == board[4] == board[7] == 'X') or
        (board[2] == board[5] == board[8] == 'X') or
        (board[3] == board[6] == board[9] == 'X') or
        (board[1] == board[5] == board[9] == 'X') or
        (board[3] == board[5] == board[7] == 'X') 
    ):
        print('THe winner is X')
    
    elif(
        (board[4] == board[5] == board[6] == 'O') or
        (board[7] == board[8] == board[9] == 'O') or
        (board[1] == board[2] == board[3] == 'O') or
        (board[1] == board[4] == board[7] == 'O') or
        (board[2] == board[5] == board[8] == 'O') or
        (board[3] == board[6] == board[9] == 'O') or
        (board[1] == board[5] == board[9] == 'O') or
        (board[3] == board[5] == board[7] == 'O') 
    ):
        print('THe winner is O ')


def check_tie(board):
    if '-' not in board:
        disp_board(board)
        print('Tie game!!')

def switch_player():
    global current_player
    if current_player == 'X':
        current_player = 'O'
    else:
        current_player = 'X'

def comp(board):
    while current_player == 'O':
        position = random.randint(0, 8)
        if board[position] == '-':
            board[position] = 'O'
            switch_player()

while game_on:
    disp_board(board)
    user_input(board)
    check_tie(board)
    check_win(board)
    switch_player()
    comp(board)
    check_tie(board)
    check_win(board)
