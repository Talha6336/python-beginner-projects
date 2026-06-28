# Generate a random number
# Ask the user to make guess
# If not a valid number
#   print error
# if number< guess
# print too low
# if number> guess
# print too high
# else
# print well done

import random
numbers_to_guess = random.randint(1, 100)
while True:
    try:
        guess = int(input("Guess the number between 1-100: "))

        if (guess < numbers_to_guess):
            print("Too Low")
        elif (guess > numbers_to_guess):
            print("Too High")
        else:
            print("Congratulation you guess the nummber")
            break
    except ValueError:
        print("Please enter a valid number")
