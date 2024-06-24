# 1.6.1 Functions as Arguments

def summation(n, term):
    total, k = 0, 1
    while k <= n:
        total, k = total + term(k), k + 1
    return total

def identity(x):
    return x * x * x

def pi_term(x):
    return 8/((4 * x - 3) * (4 * x - 1))


# 1.6.2 Funcitons as General Methods
def improve(update, close, guess=1):
    '''
    >>> improve(golden_update, square_close_to_successor)
    1.6180339887498951
    '''
    while not close(guess):
        guess = update(guess)
    return guess

def golden_update(guess):
    return 1/guess + 1

def square_close_to_successor(guess):
    return approx_eq(guess * guess, guess + 1)

def approx_eq(x, y, tolerance=1e-15):
    return abs(x - y) < tolerance

# A test for improve(), no news is good news
from math import sqrt
phi = 1 / 2 + sqrt(5) / 2
def improve_test():
    approx_phi = improve(golden_update, square_close_to_successor)
    assert approx_eq(phi, approx_phi), 'phi differs from its approximation'


# 1.6.3 Defining Functions III:Nested Definitions
def average(x, y):
    return (x + y)/2

def improve(update, close, guess=1):
    while not close(guess):
        guess = update(guess)
    return guess

def approx_eq(x, y, tolerance=1e-3):
    return abs(x - y) < tolerance

def sqrt(a):
    def sqrt_update(x):
        return average(x, a/x)
    def sqrt_close(x):
        return approx_eq(x * x, a)
    return improve(sqrt_update, sqrt_close)

result = sqrt(256)


# 1.6.4 Functions as Returned Values
def square(x):
    return x * x

def successor(x):
    return x + 1

def compose1(f, g):
    def h(x):
        return f(g(x))
    return h

def f(x):
    """Never called."""
    return -x

square_successor = compose1(square, successor)
result = square_successor(12)


# 1.6.5 Example: Newton's Method
def newton_update(f, df):
    def update(x):
        return x - f(x) / df(x)
    return update

def find_zero(f, df):
    def near_zero(x):
        return approx_eq(f(x), 0)
    return improve(newton_update(f, df), near_zero)

def square_root_newton(a):
    def f(x):
        return x * x - a
    
    def df(x):
        return 2 * x
    
    return find_zero(f, df)

def power(x, n):
    '''
        Return x * x * x * ... * x for x repeated n times
    '''
    product, k = 1, 0
    while k < n:
        product, k = product * x, k + 1
    
    return product

def nth_root_of_a(n, a):
    def f(x):
        return power(x, n) - a
    
    def df(x):
        return n * power(x, n - 1)
    
    return find_zero(f, df)

# 1.6.6 Currying
def curried_pow(x):
    def h(y):
        return pow(x, y)
    return h

def map_to_range(start, end, f):
    while start < end:
        print(f(start))
        start = start + 1

def curry2(f):
    '''Return a curried version of the given two-argument function.'''
    def g(x):
        def h(y):
            return f(x, y)
        return h
    return g

def uncurry2(g):
    '''Return a two-argument version of the given curried function.'''
    def f(x, y):
        return g(x)(y)
    return f

# 1.6.7 Lambda Expressions
def compose1(f, g):
    return lambda x: f(g(x))

f = compose1(lambda x: x * x, lambda y: y + 1)
result = f(12)

 compose1 = lambda f,g: lambda x: f(g(x))
# assign compose1 with a function that takes f, g (two functions) and return a function that takes x and returns function f that takes funciton g that takes x

