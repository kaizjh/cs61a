def count(f):
    def counted(*args):
        counted.call_count += 1
        return f(*args)
    counted.call_count = 0
    return counted

@count
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-2) + fib(n-1)

# Without @count (decorator):
fib = count(fib) # One fib is counted() and another fib is f()
fib(19) # 4181
fib.call_count # 13529

# With @count, then without: fib = count(fib)
# fib(19) # 4181
# fib.call_count # 13529


def memo(f):
    cache = {}
    def memoized(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]
    return memoized