import random

# number = int(input('Please type a positive number: '))

# while number < 0:
#     print('Sorry, that is a negative number. Please try again. ')
#     number = int(input('Please type a positive number: '))

# print(f'The number is: {number}')  

print('Play the magic number guess:')

# play_again = 'yes'
# while play_again == 'yes':
#     magic_number = random.randint(1, 100)

# counter = 0
# guess = 0

# while guess != magic_number:
#     guess = int(input("What is your guess? "))
#     guess_count = guess_count + 1

#     if guess < magic_number:
#         print("Higher")
#     elif guess > magic_number:
#         print("Lower")
#     else:
#         print("You guessed it!")

# print(f"It took you {guess_count} guesses")

# play_again = input("Would you like to play again (yes/no)? ")

# print("Thank you for playing. Goodbye.")        

keep_playing = "yes"

# As long as they say "yes" we will keep playing
while keep_playing == "yes":
    magic_number = random.randint(1, 100)

    # this variable will keep track of how many guesses it took
    guess_count = 0

    guess = -1

    # Keep going as long as the guess doesn't match the magic number
    while guess != magic_number:
        guess = int(input("What is your guess? "))
        guess_count = guess_count + 1

        if guess < magic_number:
            print("Higher")
        elif guess > magic_number:
            print("Lower")
        else:
            print("You guessed it!")

    # At this point, they have guessed it correctly
    print(f"It took you {guess_count} guesses")

    keep_playing = input("Would you like to play again (yes/no)? ")

print("Thank you for playing. Goodbye.")









