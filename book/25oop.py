class Account:
        # By convention, s should be self, but this is not enforced
        def __init__(s, account_holder):
            s.balance = 0
            s.holder = account_holder
        def deposit(s, amount):
            s.balance = s.balance + amount
            return s.balance
        
a = Account('John')
a.deposit(500)
print(a.balance)


# This new Account will override the former
class Account:
        """A bank account that has a non-negative balance."""
        interest = 0.02
        def __init__(self, account_holder):
            self.balance = 0
            self.holder = account_holder
        def deposit(self, amount):
            """Increase the account balance by amount and return the new balance."""
            self.balance = self.balance + amount
            return self.balance
        def withdraw(self, amount):
            """Decrease the account balance by amount and return the new balance."""
            if amount > self.balance:
                return 'Insufficient funds'
            self.balance = self.balance - amount
            return self.balance

# A subclass of (class) Account, class inheritance
class CheckingAccount(Account):
        """A bank account that charges for withdrawals."""
        withdraw_charge = 1
        interest = 0.01
        def withdraw(self, amount):
            return Account.withdraw(self, amount + self.withdraw_charge)