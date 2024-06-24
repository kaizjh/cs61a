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