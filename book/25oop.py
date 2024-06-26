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