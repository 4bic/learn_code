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


class Checking(Account):
    """checking_acc. inherits functions from
    the Account Class
    """
    def __init__(self, filepath):
        Account.__init__(self, filepath)

    def transfer(self, amount):
        self.balance = self.balance - amount


checking= Checking("balance.txt")
checking.transfer(300)
print(checking.balance)
