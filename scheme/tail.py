def thunk_factorial(n, so_far=1):
    def thunk():
        if n == 0:
            return so_far
        return thunk_factorial(n - 1, so_far * n)
    return thunk

def factorial(n):
    value = thunk_factorial(n)
    while callable(value): # While value is still a thunk (function)
        value = value() # Overwirte function value (thunk_factorial), save the space during the recurion
    return value

def f(n):
    if n == 1:
        return 1
    return f(n - 1)

def of(f):
    def y(x):
        print(x)
        return f(x)
    return y

f = of(f)
"""
>>> f(4)
4
3
2
1
1
"""