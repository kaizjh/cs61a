class Link:
    """A linked list with a first element and the rest."""
    empty = ()
    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest
    
    def __getitem__(self, i):
        if i == 0:
            return self.first
        else:
            return self.rest[i-1] # Or: return self.rest.__getitem__(i - 1)
        
    def __repr__(self):
        if self.rest:
            return f'Link({self.first}, {self.rest})'
        else:
            return f'Link({self.first})'

"""
ones = Link(1)
ones.rest = ones
[ones.first, ones.rest.first, ones.rest.rest.first, ones.rest.rest.rest.first]
[1, 1, 1, 1]
ones.rest is ones
True
"""

def strange_loop():
    s = Link(1, Link(Link(2)))
    s.rest.first.rest = s
    return s
s = strange_loop()




def sum_rec(s):
    assert isinstance(s, Link)
    if s is Link.empty:
        return 0
    else:
        return s.first + sum_rec(s.rest)

def sum_iter(s):
    assert isinstance(s, Link)
    sum = 0
    while s is not Link.empty:
        sum, s = sum + s.first, s.rest
    return sum





def overlap(s, t):
    """For increasing s and t, count the numbers that appear in both.

    >>> a = Link(3, Link(4, Link(6, Link(7, Link(9, Link(10))))))
    >>> b = Link(1, Link(3, Link(5, Link(7, Link(8)))))
    >>> overlap(a, b)  # 3 and 7
    2
    >>> overlap(a.rest, b)  # just 7
    1
    >>> overlap(Link(0, a), Link(0, b))
    3
    """
    if s is Link.empty or t is Link.empty:
        return 0
    if s.first == t.first:
        return 1 + overlap(s.rest, t.rest)
    elif s.first < t.first:
        return overlap(s.rest, t)
    elif s.first > t.first:
        return overlap(s, t.rest)

"""
iteration:
k += 1
s = s.rest
t = t.rest

s = s.rest

t = t.rest
"""




def divide(n, d):
    """Return a linked list with a cycle containing the digits of n/d.

    >>> display(divide(5, 6))
    0.8333333333...
    >>> display(divide(2, 7))
    0.2857142857...
    >>> display(divide(1, 2500))
    0.0004000000...
    >>> display(divide(3, 11))
    0.2727272727...
    >>> display(divide(3, 99))
    0.0303030303...
    >>> display(divide(2, 31), 50)
    0.06451612903225806451612903225806451612903225806451...
    """
    """
    assert n > 0 and n < d
    r = n / d
    s = Link(0)
    # Get r's finite part, and r's infinite part
    # Turn finite into a Linked list, or get finite into Link s
    # Get infinite part into a Link t, link s and t
    # Fucking too complex
    
    # Because n < d, the first digit must be 0
    cach = {}
    while True:
        digit = int(r)
        r = (r - digit) * 10
    return s
    """
    assert n > 0 and n < d
    result = Link(0)  # The zero before the decimal point
    cache = {}
    tail = result
    while n not in cache:
        q, r = 10 * n // d, 10 * n % d
        tail.rest = Link(q)
        tail = tail.rest
        cache[n] = tail
        n = r
    tail.rest = cache[n]
    return result
divide(2, 31)


def display(s, k=10):
    """Print the first k digits of infinite linked list s as a decimal.

    >>> s = Link(0, Link(8, Link(3)))
    >>> s.rest.rest.rest = s.rest.rest
    >>> display(s)
    0.8333333333...
    """
    assert s.first == 0, f'{s.first} is not 0'
    digits = f'{s.first}.'
    s = s.rest
    for _ in range(k):
        assert s.first >= 0 and s.first < 10, f'{s.first} is not a digit'
        digits += str(s.first)
        s = s.rest
    print(digits + '...')