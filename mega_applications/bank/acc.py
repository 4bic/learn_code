class Account(object):
    """Description for Account class."""
    def __init__(self,filepath):
        self.filepath = filepath
        with open(filepath, 'r') as file:
            self.balance = int(file.read())

    # withraw from account
    def withdraw(self, amount):
        self.balance=self.balance - amount
    # deposit to account
    def deposit(self, amount):
        self.balance = self.balance + amount
    # save alterations to account
    def commit(self):
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))







account=Account("balance.txt")
print (account.balance)
account.withdraw(150)
print (account.balance)
account.deposit(1150)
print (account.balance)
account.commit()
