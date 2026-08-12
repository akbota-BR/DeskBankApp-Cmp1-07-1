from bank import Bank

b = Bank()

print("Testing Bank class...")
print(f"Bank deposit state {b.balance}")
print("Bank deposit amount -> 1000")
b.deposit(1000)
print(f"Bank deposit state {b.balance}")
print("Bank withdraw amount -> 500")
b.withdraw(500)
print(f"Bank withdraw state {b.balance}")