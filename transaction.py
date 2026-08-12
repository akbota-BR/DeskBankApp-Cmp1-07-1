from account import Account

class Transaction:
    def __init__(self, sender: Account, recipient: Account, amount):
        self.sender: Account = sender
        self.recipient: Account = recipient
        self.amount = amount


    def make_transaction(self):
        self.sender.withdraw(self.amount)
        self.recipient.deposit(self.amount)
