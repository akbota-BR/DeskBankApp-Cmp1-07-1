class Customer:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def get_details(self):
        return {
            "name": self.name,
            "balance": self.balance
        }

c = Customer("", 10000)
print(c.get_details())