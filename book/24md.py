# 2.4.2 Sequence Objects
chinese = ['coin', 'string', 'myriad']
suits = chinese
print(suits)

suits.pop() # Remove and return the final element(of suits)
suits.remove('string') # Remove the first element that equals the argument
print(suits)

suits.append('cup') # Add an element to the end
suits.extend(['sword', 'club']) # Add all element of a sequence to the end
print(suits)

suits[2] = 'spade' # Replace an element
print(suits)

suits[0:2] = ['heart', 'diamond'] # Replace a slice
print(suits)


# When you do not use "nonlocal balance", you can not change balance by "balance = balance - amount", if you do, then you get a UnboundLocalError.
# And use "b = b - amount" is ok, even "amount > balance" is ok, just don't change its value, otherwise, make a statement "nonlocal balance".
def make_withdraw(balance):
    def withdraw(amount):
        nonlocal balance
        if amount > balance:
            return 'Insufficient funds'
        b = balance - amount
        return b
    return withdraw

# Another version of make_withdraw(), do the same thing, but using a mutable list to store the balance.
def make_withdraw2(balance):
    b = [balance]
    def withdraw(amount):
        if amount > b[0]:
            return 'Insufficient funds'
        b[0] -= amount
        return b[0]
    return withdraw

def connector(name=None):
    """A connector between constraints."""
    informant = None
    constraints = []
    def set_value(source, value):
        nonlocal informant
        val = connector['val']
        if val is None:
            connector['val'], informant = value, source
            if name is not None:
                print(name, '=', value)
            inform_all_except(source, 'new_val', constraints)
        else:
            if val != value:
                print('Contradiction detected:', val, 'vs', value)
    
    def forget_value(source):
        nonlocal informant
        if informant == source:
            informant, connector['val'] = None, None
            if name is not None:
                print(name, 'is forgotten')
            inform_all_except(source, 'forget', constraints)
        connector = {'val': None, 'set_val': set_value, 'forget': forget_value, 
                     'has_val': lambda: connector['val'] is not None, 
                     'connect': lambda source: constraints.append(source)}
        return connector