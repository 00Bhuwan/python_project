print("Welcome to the quiz")

playing = input("Do you want to play? ").lower()
if playing != "yes":
    quit()

score = 0

one = input("Qno1. What is your name? ").lower()
if one == 'ram':
    print('Right Answer!!!')
    score += 1
else:
    print('Wrong Answer!')

two = input("Qno2. Who is your favourite football player? ").lower()
if two == 'ronaldo':
    print('Right Answer!!!')
    score += 1
else:
    print('Wrong Answer!')

three = input("Qno3. Which fruit is best to eat in Summmer? ").lower()
if three == 'watermelon':
    print('Right Answer!!!')
    score += 1
else:
    print('Wrong Answer!')

four = input("Full form of CU? ").lower()
if four == 'control unit':
    print('Right Answer!!!')
    score += 1
else:
    print('Wrong Answer!')

print('Your total score is ', score)