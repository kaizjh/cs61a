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


# Inheritance and Attribute Lookup
class A:
    z = -1
    def f(self, x):
        return B(x - 1)

class B(A):
    n = 4
    def __init__(self, y):
        if y:
            self.z = self.f(y)
        else:
            self.z = C(y + 1)

class C(B):
    def f(self, x):
        return x




# L22 Composition
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
        
    def __len__(self):
        return 1 + len(self.rest)

def add(s, v):
    assert s is not Link.empty
    if s.first > v:
        s.first, s.rest = v, s
    elif s.first < v and empty(s.rest):
        s.rest = Link(v)
    elif s.first < v:
        s.rest = add(s.rest, v)
    return s




# Use data abstraction to define a tree and fib_tree, we have learned before
def tree(label, branches=[]):
    for branch in branches:
        assert is_tree(branch)
    return [label] + list(branches)

def label(tree):
    return tree [0]

def branches(tree):
    return tree [1:]

def fib_tree(n):
    if n == 0 or n == 1:
        return tree(n)
    else:
        left = fib_tree(n - 2)
        right = fib_tree(n - 1)
        fib_n = label(left) + label(right)
        return tree(fib_n, [left, right])


# Use object system to define a tree and fib_tree, there is something different between class Tree and def tree(), but def fib_tree() is almost the same.
# And we can do lots of thing more convenient with object system, like __repr__ adn __str__(invoked by print()), etc.
class Tree:
    def __init__(self, label, branches=[]):
        self.label = label
        for branch in branches:
            assert isinstance(branch, Tree)
        self.branches = list(branches)
    
    def __repr__(self):
        if self.branches:
            branch_str = ', ' + repr(self.branches)
        else:
            branch_str = ''
        return f'Tree({repr(self.label)}{branch_str})'
    
    def __str__(self):
        return '\n'.join(self.indented())
    
    def indented(self):
        lines = []
        for b in self.branches:
            for line in b.indented():
                lines.append('  ' + line)
        return [str(self.label)] + lines
    
    def is_leaf(self):
        return not self.branches

def fib_tree(n):
    if n == 0 or n == 1:
        return Tree(n)
    else:
        left = fib_tree(n - 2)
        right = fib_tree(n - 1)
        fib_n = left.label + right.label
        return Tree(fib_n, [left, right])
    
def leaves(t):
    """Return a list of leaf labels in Tree T."""
    if t.is_leaf():
        return [t.label]
    else:
        all_leaves = []
        for b in t.branches:
            all_leaves += leaves(b)
        return all_leaves

def height(t):
    """Return the number of transitions in the longest path in T."""
    if t.is_leaf():
        return 0
    else:
        return 1 + max(height(b) for b in t.branches)
    
def prune(t, n):
    """Prune all sub-trees whose label is n."""
    t.branches = [b for b in t.branches if b.label != n]
    for b in t.branches:
        prune(b, n)





def similar(self, k, similarity):
    "Return a list of the k most similar items to self, using SIMILARITY for comparison."
    others = list(Restraurant.all)
    others.remove(self)
    return sorted(others, key=lambda r: -similarity(self, r))[:k]



def fast_overlap(s, t):
    """Return the overlap between sorted list s and sorted list t."""
    i, j, count = 0, 0, 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            count, i, j = count + 1, i + 1, j + 1
        elif s[i] < t[j]:
            i += 1
        else:
            j += 1
        return count
    



def smallest_indices(s):
    """
    Return the indices of the element(s) in list S, which has(have) the smallest absolute value.
    >>> smallest_indices([1, 2, 3, 4])
    [0]
    >>> smallest_indices([4, 1, 2, 3, 1, 4])
    [1, 4]
    >>> smallest_indices([-4, -1, 2, 1, 3, 2])
    [1, 3]
    """
    smallest = abs(min(s, key=abs))
    return [i for i in range(len(s)) if abs(s[i]) == smallest]
    # Alternative solution:
    smallest = abs(min(s, key=abs))
    f = lambda i: abs(s[i]) == smallest
    return list(filter(f, range(len(s))))

def largest_adj_sum(s):
    """
    Return the sum of the largest adjacent pair of elements in list S.
    >>> largest_adj_sum([1, 2, 3, 4])
    7
    >>> largest_adj_sum([-4, -1, 2, 3, 2, -4])
    5
    """
    assert len(s) > 1
    return max([s[i] + s[i - 1] for i in range(1, len(s))])
    # Alternative solution:
    return max([a + b for a, b in zip(s[:-1], s[1:])])

def map_digit_elem(s):
    """
    Create a dictionary mapping each digit d to the lists of elements in s that end with d.
    map_digit_elem([5, 8, 21, 13, 55, 89)
    {1: [21], 3: [13], 5: [5, 55], 8: [8], 9: [89]}
    """
    return {d: [e for e in s if e % 10 == d] for d in set(e % 10 for e in s)}
    # Alternative solution:
    digits = [x % 10 for x in s]
    return {d: [e for e in s if e % 10 == d] for d in digits}

def equal_some_other(s):
    """
    Return True if there is some element e in s such that e is equal to some other element in s.
    >>> equal_some_other([1, 2, 1, 4])
    False
    >>> equal_some_other([1, 2, 3, 3, 1, 2])
    True
    """
    return all(s[i] in s[:i] + s[i+1:] for i in range(len(s)))




# L25 Data Examples
def ordered(s, key=lambda x: x):
    """
    Is Link s ordered?
    >>> ordered(Link(1, Link(2, Link(3))))
    True
    >>> ordered(Link(1, Link(3, Link(2))))
    False
    >>> ordered(Link(1, Link(-3, Link(4))))
    False
    >>> ordered(Link(1, Link(-3, Link(4))), key=abs)
    True
    >>> ordered(Link(1, Link(4, Link(2))), key=abs)
    False
    """
    if s is Link.empty or s.rest is Link.empty:
        return True
    elif key(s.first) > key(s.rest.first):
        return False
    else:
        return ordered(s.rest, key)
    



def cumulative_mul(t):
    """Mutates t so that each node's label becomes the product of its own
    label and all labels in the corresponding subtree rooted at t.

    >>> t = Tree(1, [Tree(3, [Tree(5)]), Tree(7)])
    >>> cumulative_mul(t)
    >>> t
    Tree(105, [Tree(15, [Tree(5)]), Tree(7)])
    >>> otherTree = Tree(2, [Tree(1, [Tree(3), Tree(4), Tree(5)]), Tree(6, [Tree(7)])])
    >>> cumulative_mul(otherTree)
    >>> otherTree
    Tree(5040, [Tree(60, [Tree(3), Tree(4), Tree(5)]), Tree(42, [Tree(7)])])
    """
    "*** YOUR CODE HERE ***"
    def helper(t):
        if t.is_leaf():
            return t.label
        else:
            for b in t.branches:
                t.label =  t.label * helper(b)
            return t.label
    # helper(t) helps me use recursion to solve the problem with cumulative_mul return nothing
    helper(t)
    return None

    # Alternative solution, better solution, no return, no base case
    # Because t.branches is a list, and default=[], if b is a leaf, then for loop do nothing (b.branches=[])
    for b in t.branches:
        cumulative_mul(b)
        t.label *= b.label


def prune_small(t, n):
    """Prune the tree mutatively, keeping only the n branches
    of each node with the smallest labels.

    >>> t1 = Tree(6)
    >>> prune_small(t1, 2)
    >>> t1
    Tree(6)
    >>> t2 = Tree(6, [Tree(3), Tree(4)])
    >>> prune_small(t2, 1)
    >>> t2
    Tree(6, [Tree(3)])
    >>> t3 = Tree(6, [Tree(1), Tree(3, [Tree(1), Tree(2), Tree(3)]), Tree(5, [Tree(3), Tree(4)])])
    >>> prune_small(t3, 2)
    >>> t3
    Tree(6, [Tree(1), Tree(3, [Tree(1), Tree(2)])])
    >>> t4 = Tree(6, [Tree(1), Tree(5, [Tree(1), Tree(2), Tree(3)]), Tree(3, [Tree(3), Tree(4), Tree(2)])])
    >>> prune_small(t4, 2)
    >>> t4
    Tree(6, [Tree(1), Tree(3, [Tree(2), Tree(3)])])
    """
    if len(t.branches) > n:
        t.branches = sorted(t.branches, key=lambda x: x.label)[:n]
    for b in t.branches:
        prune_small(b, n)


def delete(t, x):
    """Remove all nodes labeled x below the root within Tree t. When a non-leaf
    node is deleted, the deleted node's children become children of its parent.

    The root node will never be removed.

    >>> t = Tree(3, [Tree(2, [Tree(2), Tree(2)]), Tree(2), Tree(2, [Tree(2, [Tree(2), Tree(2)])])])
    >>> delete(t, 2)
    >>> t
    Tree(3)
    >>> t = Tree(1, [Tree(2, [Tree(4, [Tree(2)]), Tree(5)]), Tree(3, [Tree(6), Tree(2)]), Tree(4)])
    >>> delete(t, 2)
    >>> t
    Tree(1, [Tree(4), Tree(5), Tree(3, [Tree(6)]), Tree(4)])
    >>> t = Tree(1, [Tree(2, [Tree(4), Tree(5)]), Tree(3, [Tree(6), Tree(2)]), Tree(2, [Tree(6),  Tree(2), Tree(7), Tree(8)]), Tree(4)])
    >>> delete(t, 2)
    >>> t
    Tree(1, [Tree(4), Tree(5), Tree(3, [Tree(6)]), Tree(6), Tree(7), Tree(8), Tree(4)])
    """
    new_branches = []
    for b in t.branches:
        delete(b, x)
        if b.label == x:
            new_branches.extend(b.branches)
        else:
            new_branches.append(b)
    t.branches = new_branches

t = Tree(1, [Tree(3, [Tree(6), Tree(2)]), Tree(4)])
delete(t, 2)



