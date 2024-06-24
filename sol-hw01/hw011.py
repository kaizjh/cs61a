def hailstone(n):
    steps = 1
    while( n != 1):
        print(n)
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
        steps += 1
    
    print(n)
    return steps


from operator import add, mul
def square(x):
    return mul(x, x)
    
def sum_square(x, y):
    return add(square(x), square(y))

result = sum_square(5, 12)
print(result)