# Create account class with 2 attributes - balance and account no. Create methods for debit,credit and printing the balance.

class Account:
    def __init__(self, balance, account):
        self.balance = balance
        self.account = account
    
    #debit method
    def debit(self, amount):
        self.balance -= amount
        print("An amount of $", amount, "has been DEBITED to your account", account1.account, "Total Avail.bal $", self.get_balance())
        
    
    def credit(self, amount):
        self.balance += amount
        print("An amount of $", amount, "has been CREDITED to your account", account1.account, "Total Avail.bal $", self.get_balance())

    def get_balance(self):
        return self.balance


account1 = Account(15000,4888410551548)
account1.debit(1000)
account1.credit(5600)