def remove(n, digit):
    kept, digits = 0, 0
    while n > 0 :
        n, last = n // 10, n % 10
        if last != digit :
            kept = kept + last * (10 ** digits)
            digits = digits + 1
    return kept
    
a = remove(243132, 2)
print(a)




def trace1(fn):
    """
        Returns a version of fn that first print before it is called.
        fn - a function of 1 argument
    """

    def traced(x):
        print('Calling', fn, 'on argument', x)
        return fn(x)
    return traced

def square(x):
    return x * x
# @trace1 ahead of the function does the same thing as this line below, and we always use this shortcut for transforming a function into another, which is called a decorator @...
square = trace1(square) 


@trace1
def sum_squares_up_to(n):
    k = 1
    total = 0
    while k <= n:
        total, k = total + square(k), k+1
    return total




# Luhn's algorithm for validating credit cards, if the result's last digit is 0, then this credit card is legit.

# Irving's version using "normal" recursion in python
def luhn(n):
    last = n % 100
    all_but_last = n // 100

    if last == 0 and all_but_last == 0:
        return 0
    
    double = last // 10 * 2
    if double > 9:
        return last % 10 + double - 9 + luhn(all_but_last)
    else:
        return last % 10 + double + luhn(all_but_last)
    
a = luhn(4003600000000014)


# The cs61a video version using mutual recursion, and he codes more functions, makes every function does less things, but has to type some same codes.
def split(n):
    return n // 10, n % 10

def sum_digits(n):
    if n < 10:
        return n
    else:
        all_but_last, last = split(n)
        return sum_digits(all_but_last) + last
    
def luhn_sum(n):
    if n < 10:
        return n
    else:
        # Some repetitive work
        all_but_last, last = split(n)
        
        return luhn_sum_double(all_but_last) + last
    
def luhn_sum_double(n):
    all_but_last, last = split(n)
    luhn_digit = sum_digits(2 * last)
    if n < 10:
        return luhn_digit
    else:
        return luhn_sum(all_but_last) + luhn_digit

b = luhn_sum(32)
c = luhn_sum(4003600000000014)




def cascade(n):
    if n < 10:
        print(n)
    else:
        print(n)
        cascade(n // 10)
        print(n)
a = cascade(12345)


def inverse_cascade(n):
    grow(n)
    print(n)
    shrink(n)

def f_then_g(f, g, n):
    if n:
        f(n)
        g(n)

grow = lambda n: f_then_g(grow, print, n // 10)
shrink = lambda n: f_then_g(print, shrink, n // 10)
b = inverse_cascade(12345)




def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    



pairs = [[1,2], [1, 3], [2, 2], [2, 3]]




def tree(label, branches=[]):
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [label] + list(branches)

def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_leaf(tree):
    return not branches(tree)

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def count_paths(t, total):
    if label(t) == total:
        found = 1
    else:
        found = 0
    return found + sum([count_paths(b, total - label(t)) for b in branches(t)]) 

def count_leaves(tree):
    if is_leaf(tree):
        return [label(tree)]
    else:
        return sum([count_leaves(b) for b in branches(tree)], [])

def increment(t):
    """Return a tree like t but with all labels incremented. No base case!"""
    return tree(label(t) + 1, [increment(b) for b in branches(t)])


haste = tree('h', [tree('a', [tree('s'), 
                              tree('t')])
                   , tree('e')])


# L15 Mutability
from datetime import date
today = date(2024, 6, 22)
random = date(2343, 2, 2)

sub = random - today
year = today.year
month = today.month
strftime = today.strftime("%B,%d,%Y,%A")

from unicodedata import name, lookup
a = name('郑')
b = lookup(a)
c = b.encode()

# Generator
def yield_partitions(n, m):
    """
    >>> for p in yield_partitions(6, 4): print(p)
    2 + 4
    1 + 1 + 4
    3 + 3
    1 + 2 + 3
    1 + 1 + 1 + 3
    2 + 2 + 2
    1 + 1 + 2 + 2
    1 + 1 + 1 + 1 + 2
    1 + 1 + 1 + 1 + 1 + 1
    """
    if n > 0 and m > 0:
        if n == m:
            yield str(m)
        for p in yield_partitions(n - m, m):
            yield p + ' + ' + str(m)
        yield from yield_partitions(n, m - 1)
