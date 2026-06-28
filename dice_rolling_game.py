import random
# Ask a user to roll the dice
# if user enter y
#   Generate two random number
#  if user enter n
# print thank you message
# terminate
# else
# print invalid choice
while True:
    choice = input("Roll the dice? (y/n): ").lower()
    if choice == "y":
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        print(f"({die1}, {die2})")
    elif choice == "n":
        print("Thank you for playing")
        break
    else:
        print("Invalid Choice")
