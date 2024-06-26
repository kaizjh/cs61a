primes = [2, 4, 5, 7]
iterator = iter(primes)
next(iterator)  # 2
next(iterator)  # 4
next(iterator)  # 5
next(iterator)  # 7
try:
    next(iterator)
except StopIteration:
    print("No more values")

def double_and_print(x):
    print('***', x, '=>', x * 2, '***')
    return x * 2
s = range(3, 9)
doub = map(double_and_print, s)


# With our knowledge of iterators, we can implement the execution rule of a for statement
# In terms of while, assignment, and try statements.
counts = [1, 2, 3]
items = counts.__iter__()
try:
    while True:
        item = items.__next__()
        print(item)
except StopIteration:
        pass
# Alter but more common way
for item in counts:
     print(item)
"""
1
2
3
1
2
3
"""    


a = [1, 2, 3, 2]
b = [4, 5, 6]
for pair in zip(a, b):
    print(pair)
    print(type(pair))
"""
(1, 4)
<class 'tuple'>
(2, 5)
<class 'tuple'>
(3, 6)
<class 'tuple'>
"""