class Account(object):
    """Description for Account class."""
    def __init__(self,filepath):
        with open(filepath, 'r') as file:
            self.balance = int(file.read())


    def withdraw(self, amount):
        self.balance=self.balance - amount

    def deposit(self, amount):
        self.balance = self.balance + amount



account=Account("balance.txt")
print (account.balance)
account.withdraw(150)
print (account.balance)
account.deposit(1150)
print (account.balance)
