import random

def play():
    print("let 'r' be rock, 'p' be paper and 's' be scissors")
    user = input("Enter your choice: ")
    computer = random.choice(['r', 'p' , 's'])
    print(f'the computer played {computer}')

    if user == computer:
        print('is tie')

    else:
        if user == 'r' and computer == 's' or user == 'p' and computer == 'r' or user == 's' and computer == 'p':
            print('You won!')
        else:
            print("You lost!!")


play()

def tim():
    user_wins = 0
    comp_wins = 0
    option = ['rock', 'paper', 'scissor']
    while True:
        user_input = input("type rock/ paper/ scissor or q to quit: ").lower()
        if user_input == 'q':
            break
        if user_input not in option:
            continue

        random_number = random.randint(0, 2)
        computer_pick = option[random_number]
        print(f'computer picked {computer_pick}')

        if user_input == computer_pick:
            print('Its a tie')
        elif user_input == 'rock' and computer_pick == 'scissor':
            print('You win')
        elif user_input == 'paper' and computer_pick == 'rock':
            print("You win")
        elif user_input == 'scissor' and computer_pick == 'paper':
            print("You win")
        else: 
            print('You lost!!')
tim() 