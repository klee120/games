import random
from words import words
# import string library function 
import string 

def get_word(words):
    word = random.choice(words)     # randomly chosen word from list
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def start_game():
    valid_inputs = {'Yes', 'yes', 'Y', 'y'}
    print('Hello! Welcome to the game of Hangman!\nYou have 7 lives to guess the mystery word.\nAre you ready?\nYes or No?')

    if input() in valid_inputs:
        print("Awesome! Let's get started")
        return True
    else:
        print('Bye! See you next time')
        return False

def replay():
    valid_inputs = {'Yes', 'yes', 'Y', 'y'}
    while input('Would you like to play again? ') in valid_inputs:
        print('\n')
        hangman()
    else:
        print('Thank you for playing! Come again next time.')
        exit

# print status of game: mystery word with dashes and correctly guessed letters; already guessed letters
def status(mystery_word, used_letters, lives):
    status = 'Status: '
    for letter in mystery_word:
        if letter in used_letters:
            status += letter
        else:
            status += "-"
        status += " "
    print(status)

    guess = 'Already guessed letters: '
    for letter in used_letters:
        guess += letter
        guess += ' '
    print(guess)

    print(f'Lives: {lives}')
    return

def hangman():
    mystery_word = get_word(words)
    word_letters = set(mystery_word)    # unique letters in word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    lives = 7

    # getting user input
    while len(word_letters) > 0 and lives > 0:
        # give status update
        status(mystery_word, used_letters, lives)
        
        # user guess letter
        guess = input('Guess a letter: ').upper()
        while guess in used_letters:
            guess = input('Already guessed. Guess again: ').upper()
        used_letters.add(guess)
        
        # evaluate guess
        if guess in mystery_word:
            print('Correct letter!\n')
            word_letters.remove(guess)
        else:
            print('Wrong letter :(\n')
            lives -= 1
    
    # win game?
    if lives > 0:
        print(f'You win! The correct word was {mystery_word}.')
    else:
        print(f'Sorry you are out of lives :( The correct word was {mystery_word}.')
    return
    
def main():
    # start game
    if start_game() == False:
        exit

    # play game
    hangman()
    
    # play again
    replay()

if __name__ == '__main__':
    main()