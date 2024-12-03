import random
import string
from words import words

def valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
        
    return word.upper()


def hangman():
    word = valid_word(words)
    print(word)
    word_letters = set(word) #letters in word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    lives = 6

    while len(word_letters) > 0 and lives > 0:
        print('You have', lives, 'lives left and You have used these letters: ', ' '.join(used_letters))

        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("Current word: ", ' '.join(word_list))
        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                 lives = lives - 1
                 print('not in word')
            
        elif user_letter in used_letters:
            print("already guessed.")

        else:
            print("you didn't type valid word.")
    if lives == 0:
        print("You died, the word was ", word)
    else:
        print('You have quessed the word', word, '!!')

hangman() 