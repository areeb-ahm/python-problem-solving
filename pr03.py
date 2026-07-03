# Write class BankAccount:

# __init__(self, owner, balance=0)
# deposit(amount) — adds to balance, rejects negative amount (print error, don't crash)
# withdraw(amount) — subtracts if sufficient balance, else print "Insufficient funds"
# __str__ — returns "Owner: <name>, Balance: <balance>"

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("ERROR: Enter a valid amount!")
        else:
            self.balance += amount

    def withdraw(self, amount):
        if self.balance < amount:
            print("ERROR: Insufficient funds!")
        else:
            self.balance -= amount

    def __str__(self):
        return f"Owner: {self.owner}, Balance: {self.balance}"
    
    
acc = BankAccount("Areeb", 1000)
acc.deposit(500)
acc.withdraw(2000)
acc.withdraw(300)
print(acc)