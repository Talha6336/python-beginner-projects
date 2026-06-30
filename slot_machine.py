import random


def get_starting_balance():
    while True:
        try:
            balance = int(input("Enter your starting balance:  $"))
            if balance <= 0:
                print("Balance must be a positive number.")
            else:
                return balance
        except ValueError:
            print("Please enter a valid number. ")


def get_bet_amount(balance):

    while balance > 0:
        try:

            bet = int(input("Enter your bet amount: $"))
            if bet <= 0 or bet > balance:
                print(
                    f'Invalid bet amount. You can bet between $1 and ${balance}')
            else:
                return bet
        except ValueError:
            print('Please enter a valid number for the bet amount')


def spin_reels():
    symbols = ['🍒', '🍋', '🔔', '⭐', '🍉']
    return [random.choice(symbols)for _ in range(3)]


def display_reels(reels):
    print(f'{reels[0]} | {reels[1]} | {reels[2]}')


def calculate_payout(reels, bet):

    if reels[0] == reels[1] or reels[0] == reels[2] or reels[1] == reels[2]:
        return bet * 2
    if reels[0] == reels[1] == reels[2]:
        return bet*10
    return 0


def main():
    balance = get_starting_balance()
    while balance > 0:
        print('Welcome to the Slot Machine Game!')
        print(f'You start with the balance of ${balance} \n')
        bet = get_bet_amount(balance)
        reels = spin_reels()
        display_reels(reels)
        payout = calculate_payout(reels, bet)
        if payout > 0:
            print(f'You won ${payout}')
        else:
            print("You lost")
        balance = balance-bet+payout
        if balance <= 0:
            print("You are ran out of money! Game over")
            break
        play_again = input("Do you want to play again (y/n): ").lower()
        if play_again != 'y':
            print(f'You walk away with ${balance}.')
            break


if __name__ == "__main__":
    main()
