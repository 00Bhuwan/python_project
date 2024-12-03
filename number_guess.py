import random
random = random.randrange(10)
print(random)

count = 0
try:
    while True:
        guess = int(input('Guess a number between 0 to 9: '))
        count += 1
        if guess == random:
            print('Correct guess')
            break
        else:
            print('Incorrect guess! try again')
        
    print("The no of guess for correct guess is ", count)
except(ValueError):
    print('Enter a number')