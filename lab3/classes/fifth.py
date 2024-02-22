class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit of ${amount} accepted.")
        
    
    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrawal of ${amount} accepted.")
            else:
                print("Not enough money on your account")
        else:
            print("Withdrawal amount must be greater than zero.")

"""
account = Account("Maxim", 1000)


account.deposit(500)
account.withdraw(200)
account.withdraw(1000) 


print(f"Owner: {account.owner}, Balance: ${account.balance}")
"""