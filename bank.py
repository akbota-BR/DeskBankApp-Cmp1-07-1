class Bank:
    def __init__(self):
        self.balance = 1000

    def get_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount


bank = Bank()

while True:
    print("Welcome to the Bank App")
    print("1. Check Balance: Enter s")
    print("2. Deposit: Enter d")
    print("3. Withdraw: Enter w")
    print("4. Exit: Enter x")

    choice = input("Enter your choice: ")

    

    if choice.lower() == 's':
        print(f"Your balance is: ${bank.get_balance()}")
    elif choice.lower() == 'd':
        amount = float(input("Enter amount to deposit: "))
        bank.deposit(amount)
        print(f"Deposited ${amount}. New balance is: ${bank.get_balance()}")
    elif choice.lower() == 'w':
        amount = float(input("Enter amount to withdraw: "))
        try:
            bank.withdraw(amount)
            print(f"Withdrew ${amount}. New balance is: ${bank.get_balance()}")
        except ValueError as e:
            print(e)
    elif choice.lower() == 'x':
        print("Thank you for using the Bank App!")
        break
    else:
        print("Invalid choice. Please try again.")