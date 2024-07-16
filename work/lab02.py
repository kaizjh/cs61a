def f(x):
    if x == 0:
        return "zero"
    elif x > 0:
        return "positive"
    else:
        return ""
    

def cake():
    print('beets')
    def pie():
        print('sweets')
        return 'cake'
    return pie
chocolate = cake()
more_chocolate, more_cake = chocolate(), cake

def snake(x, y):
    if cake == more_cake:
        return chocolate
    else:
        return x + y


def composite_identity(f, g):
    """
    Return a function with one parameter x that returns True if f(g(x)) is
    equal to g(f(x)). You can assume the result of g(x) is a valid input for f
    and vice versa.

    >>> add_one = lambda x: x + 1        # adds one to x
    >>> square = lambda x: x**2          # squares x [returns x^2]
    >>> b1 = composite_identity(square, add_one)
    >>> b1(0)                            # (0 + 1) ** 2 == 0 ** 2 + 1
    True
    >>> b1(4)                            # (4 + 1) ** 2 != 4 ** 2 + 1
    False
    """
    def h(x):
        if f(g(x)) == g(f(x)):
            return True
        else:
            return False
    return h

    # Alternate solution (better than mine)
    return lambda x: f(g(x)) == g(f(x))


from disc01 import is_prime, sum_digits
def count_fives(n):
    """Return the number of values i from 1 to n (including n)
    where sum_digits(n * i) is 5.
    >>> count_fives(10)  # Among 10, 20, 30, ..., 100, only 50 (10 * 5) has digit sum 5
    1
    >>> count_fives(50)  # 50 (50 * 1), 500 (50 * 10), 1400 (50 * 28), 2300 (50 * 46)
    4
    """
    i = 1
    counts = 0
    while i <= n:
        if sum_digits(i * n) == 5:
            counts += 1
        i += 1
    return counts
        
def count_primes(n):
    """Return the number of prime numbers up to and including n.
    >>> count_primes(6)   # 2, 3, 5
    3
    >>> count_primes(13)  # 2, 3, 5, 7, 11, 13
    6
    """
    i = 2
    counts = 0
    while i <= n:
        if is_prime(i):
            counts += 1
        i += 1
    return counts

def count_cond(condition):
    """Returns a function with one parameter N that counts all the numbers from
    1 to N that satisfy the two-argument predicate function Condition, where
    the first argument for Condition is N and the second argument is the
    number from 1 to N.

    >>> count_fives = count_cond(lambda n, i: sum_digits(n * i) == 5)
    >>> count_fives(10)   # 50 (10 * 5)
    1
    >>> count_fives(50)   # 50 (50 * 1), 500 (50 * 10), 1400 (50 * 28), 2300 (50 * 46)
    4

    >>> is_i_prime = lambda n, i: is_prime(i) # need to pass 2-argument function into count_cond
    >>> count_primes = count_cond(is_i_prime)
    >>> count_primes(2)    # 2
    1
    >>> count_primes(3)    # 2, 3
    2
    >>> count_primes(4)    # 2, 3
    2
    >>> count_primes(5)    # 2, 3, 5
    3
    >>> count_primes(20)   # 2, 3, 5, 7, 11, 13, 17, 19
    8
    """
    def f(n):
        i = 1
        counts = 0
        while i <= n:
            if condition(n, i):
                counts += 1
            i += 1
        return counts
    return f

'''
    Q: In what ways is the logic for count_fives and count_primes similar? and in what ways are they different?
    A: They both need three arguments to accomplish their job, that is n, i, counts (and both counts is the output),
       and they both need a condition statement, and within the condition statement,
       is their difference!
'''


def multiple(a, b):
    """Return the smallest number n that is a multiple of both a and b.

    >>> multiple(3, 4)
    12
    >>> multiple(14, 21)
    42
    """
    n = max(a, b)
    while True:
        if n % a == 0 and n % b == 0:
            return n
        n += 1


def cycle(f1, f2, f3):
    """Returns a function that is itself a higher-order function.

    >>> def add1(x):
    ...     return x + 1
    >>> def times2(x):
    ...     return x * 2
    >>> def add3(x):
    ...     return x + 3
    >>> my_cycle = cycle(add1, times2, add3)
    >>> identity = my_cycle(0)
    >>> identity(5)
    5
    >>> add_one_then_double = my_cycle(2)
    >>> add_one_then_double(1)
    4
    >>> do_all_functions = my_cycle(3)
    >>> do_all_functions(2)
    9
    >>> do_more_than_a_cycle = my_cycle(4)
    >>> do_more_than_a_cycle(2)
    10
    >>> do_two_cycles = my_cycle(6)
    >>> do_two_cycles(1)
    19
    """
    def g(n):
        def h(x):
            i = 1
            while i <= n:
                remaining = i % 3
                if remaining == 1:
                    x = f1(x)
                elif remaining == 2:
                    x = f2(x)
                else:
                    x = f3(x)
                i += 1
            return x
        return h
    return g

    # Alternative recurisive solution
    def g(n):
        def h(x):
            if n == 0:
                return x
            # Notice that this cycle() change the order of the three functions
            return cycle(f2, f3, f1)(n - 1)(f1(x))
        return h
    return g

