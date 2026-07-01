class ATM:
    def __init__(self):
        self.balance = 0

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be psoitive")

        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdraw amount must be positive")
        if amount > self.balance:
            raise ValueError("Insuffiecient Funds")

        self.balance -= amount


class ATMController:
    def __init__(self):
        self.atm = ATM()

    def get_number(self, label):
        while True:
            try:
                number = float(input(label))
                return number
            except ValueError:
                print("Please enter a valid number")

    def display_menu(self):
        print('\n Welcome to the ATM')
        print('1. Check Balance')
        print('2. Deposit')
        print('3. Withdraw')
        print('4. Exit')

    def check_balance(self):
        print(
            f'Your current balance is: ${self.atm.check_balance()}')

    def deposit(self):
        while True:
            try:
                amount = self.get_number(
                    "Enter the amount to deposited: ")
                self.atm.deposit(amount)
                print(f"Successfully depsotied {amount}")
                break

            except ValueError as error:
                print(error)

    def withdraw(self):
        while True:
            try:
                amount = self.get_number(
                    "Enter the amount to withdraw: ")

                self.atm.withdraw(amount)
                print(
                    f'Successfully withdraw the amount ${amount}')
                break
            except ValueError as error:
                print(error)

    def run(self):
        while True:
            self.display_menu()

            try:
                choice = int(input("Enter your choice: "))
                if choice == 1:
                    self.check_balance()

                elif choice == 2:
                    self.deposit()

                elif choice == 3:
                    self.withdraw()

                elif choice == 4:
                    print("Thank You for choosing the ATM")
                    break
                else:
                    print("Invalid choice please try again")

            except ValueError:
                print("Please enter a valid number")


def main():
    atm = ATMController()
    atm.run()


if __name__ == "__main__":
    main()
