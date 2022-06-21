
from cmath import e
import random
from unicodedata import is_normalized

print('Welcome to the word guessing game!')

name = input('What is your name? ')
print(f'Good luck ! {name}')
words = ['sacraments', 'scriptures', 'testimony', 'faith']
secret_word = random.choice(words)
guess_count = 0
spaces = ' _ '* len(secret_word)
guess_word = ''


while guess_word != secret_word:
    print(f'Your hint is: {spaces}')
    guess_word = input('What is your guess? ')
    guess_count = guess_count + 1

    for letter in secret_word:
        if letter.lower() == guess_word.lower():
            print(letter.upper())
        else:
            print(letter.lower(), end=' ')      

print() 

   


print(f'Congratulations! You guessed it!')
print(f'It took you {guess_count} guesses')   








