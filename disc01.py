def race(x, y):
    """The tortoise always walks x feet per minute, while the hare repeatedly
    runs y feet per minute for 5 minutes, then rests for 5 minutes. Return how
    many minutes pass until the tortoise first catches up to the hare.

    >>> race(5, 7)  # After 7 minutes, both have gone 35 steps
    7
    >>> race(2, 4) # After 10 minutes, both have gone 20 steps
    10
    """
    assert y > x and y <= 2 * x, 'the hare must be fast but not too fast'
    
    minutes, tort, hare = 0, 0, 0
    
    while tort < hare or tort == 0:
        tort += x
    
        if minutes % 10 < 5:
            hare += y
    
        minutes += 1
    
    if tort == hare:
        return minutes
    else:
        # Every time tort caught up hare, it must be the time hare is resting, then we can count the last minute
        tort -= x
        return minutes - 1 + (hare - tort) / x




def fizzbuzz(n):
    """
    >>> result = fizzbuzz(16)
    1
    2
    fizz
    4
    buzz
    fizz
    7
    8
    fizz
    buzz
    11
    fizz
    13
    14
    fizzbuzz
    16
    >>> print(result)
    None
    """
    "*** YOUR CODE HERE ***"
    i = 1
    while i <= n:
        if not i % 3 and not i % 5:
            print("fizzbuzz")
        elif not i % 3:
            print("fizz")
        elif not i % 5:
            print("buzz")
        else:
            print(i)
        
        i += 1
    



from math import sqrt
def is_prime(n):
    """
    >>> is_prime(10)
    False
    >>> is_prime(7)
    True
    >>> is_prime(1) # one is not a prime number!!
    False
    """
    "*** YOUR CODE HERE ***"
    if n == 1:
        return False

    i = 2
    while i <= sqrt(n):
        if n % i == 0:
            return False
        i += 1
        
    return True




def unique_digits(n):
    """Return the number of unique digits in positive integer n.

    >>> unique_digits(8675309) # All are unique
    7
    >>> unique_digits(13173131) # 1, 3, and 7
    3
    >>> unique_digits(101) # 0 and 1
    2
    """
    "*** YOUR CODE HERE ***"
    i, uniques = 0, 0
    while i < 10:
        if has_digit(n, i):
            uniques += 1
        i += 1
    return uniques

def has_digit(n, k):
    """Returns whether k is a digit in n.

    >>> has_digit(10, 1)
    True
    >>> has_digit(12, 7)
    False
    """
    assert k >= 0 and k < 10
    "*** YOUR CODE HERE ***"
    while n > 0:
        i = n % 10
        if i == k:
            return True
        n = n // 10
    return False


def sum_digits(n):
    total = 0
    while n > 0:
        total = total + n % 10
        n = n // 10
    return total