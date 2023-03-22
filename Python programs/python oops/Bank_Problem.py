
class Account():

    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance

    def deposit(self,amount):
        self.balance=self.balance+amount
    
    def withdrawal(self,amount):
        if amount>self.balance:
            return "Oops insufficent balance"
        else:
            self.balance=self.balance-amount
            return "Withdrawal successful"


new_account=Account('nikhil',1000)

print(new_account.withdrawal(700))

print(new_account.balance)


