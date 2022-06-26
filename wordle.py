
import random

print('Welcome to the word guessing game!')

name = input('What is your name? ')
print(f'Good luck ! {name}')
words = ['sacraments', 'scriptures', 'testimony', 'faith']
secret_word = random.choice(words)
word_len = len(secret_word)
guess_word = ''
spaces = ' _ '* word_len
guess_count = 0


while guess_word.lower() != secret_word:
    guess_count += 1
    print()
    print(f'Your hint is: {spaces}')
    guess_word = input('What is your guess? ')

    spaces = ''

    for i, letter in enumerate(guess_word):
        if letter in secret_word:
            if i >= word_len or letter != secret_word[i]:
                spaces += letter.lower() + ' '
            else:
                spaces += letter.upper() + ' '

        else:
            spaces += '_ '

print() 

print('Congratulations! You guessed it!')
print(f'It took you {guess_count} guesses')   








