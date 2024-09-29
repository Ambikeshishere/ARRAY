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
account2 = Account(120,4888451574828)
account3 = Account(12630,4888451574818)
account4 = Account(125600,4888451574218)
account5 = Account(15900,4888451574218)


account1.debit(1000)
account1.credit(5600)

account2.debit(100)
account2.credit(56000)

account3.debit(15000)
account3.credit(120)

account4.debit(1990)
account4.credit(5)

account5.credit(150000000000)
account5.debit(10)



