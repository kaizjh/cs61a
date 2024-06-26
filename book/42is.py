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
d = map(double_and_print, s)
"""
>>> next(d)
*** 3 => 6 ***
6
>>> next(d)
*** 4 => 8 ***
8
"""


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

# Built-in functions for Iteration
a = [1, 2, 3, 4, 3, 2, 1]
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

for r in reversed(a):
     print(r)
"""
1
2
3
4
3
2
1
"""
"""
>>> reversed(a)
<list_reverseiterator object at 0x7f171222ae00>
>>> list(reversed(a))
[1, 2, 3, 4, 3, 2, 1]
>>> list(reversed(a)) == a
True
>>> reversed(a) == a    # a iterator can not == a list
False

>>> list(reversed(a))
[4, 3, 2, 1]
>>> tuple(reversed(a))
(4, 3, 2, 1)
>>> sorted(reversed(a))
[1, 2, 3, 4]
>>> tuple(zip(a, b))
((1, 4), (2, 5), (3, 6))
"""

# Generators and Yield Statements
def letters_generator():
     current = 'a'
     while current <= 'd':
          yield current
          current = chr(ord(current) + 1)

letters = letters_generator()
"""
>>> type(letters)
<class 'generator'>
>>> letters.__next__()
'a'
>>> letters.__next__()
'b'
>>> letters.__next__()
'c'
>>> letters.__next__()
'd'
>>> letters.__next__()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
"""


class Letters:
    def __init__(self, start='a', end='e'):
          self.start = start
          self.end = end
    def __iter__(self):
        return LetterIter(self.start, self.end)

class LetterIter:
        """An iterator over letters of the alphabet in ASCII order."""
        def __init__(self, start='a', end='e'):
            self.next_letter = start
            self.end = end
        def __next__(self):
            if self.next_letter == self.end:
                raise StopIteration
            letter = self.next_letter
            self.next_letter = chr(ord(letter)+1)
            return letter
        

class Stream:
        """A lazily computed linked list."""
        class empty:
            def __repr__(self):
                return 'Stream.empty'
        empty = empty()
        def __init__(self, first, compute_rest=lambda: empty):
            assert callable(compute_rest), 'compute_rest must be callable.'
            self.first = first
            self._compute_rest = compute_rest
        @property
        def rest(self):
            """Return the rest of the stream, computing it if necessary."""
            if self._compute_rest is not None:
                self._rest = self._compute_rest()
                self._compute_rest = None
            return self._rest
        def __repr__(self):
            return (f'Stream({repr(self.first)}, <...>)')
            return 'Stream({0}, <...>)'.format(repr(self.first))
        
def integer_stream(first):
        def compute_rest():
            return integer_stream(first+1)
        return Stream(first, compute_rest)
p = integer_stream(1)