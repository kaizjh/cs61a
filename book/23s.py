odds = [1, 3, 5, 7, 9]
o = [x for x in odds if 25 % x == 0]


def divisors(n):
    return [1] + [x for x in range(2, n) if n % x == 0]

perfect_number = [n for n in range(1, 1000) if sum(divisors(n)) == n]


def width(area, height):
    assert area % height == 0
    return area // height

def perimeter(width, height):
    return 2 * width + 2 * height

def minimum_perimeter(area):
    heights = divisors(area)
    perimeters = [perimeter(width(area, h), h)for h in heights]
    return min(perimeters)

area = 80
a = minimum_perimeter(area)

from operator import mul
def reduce(reduce_fn, s, initial):
    reduced = initial
    for x in s:
        reduced = reduce_fn(reduced, x)
    return reduced

# 2.3.6 Tree
def tree(root_label, branches=[]):
        for branch in branches:
            assert is_tree(branch), 'branches must be trees'
        return [root_label] + list(branches)
def label(tree):
    return tree[0]
def branches(tree):
    return tree[1:]
def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True
def is_leaf(tree):
        return not branches(tree)

t = tree(3, [tree(1), tree(2, [tree(1), tree(1)])])
is_tree(t)

def fib_tree(n):
    if n == 0 or n == 1:
        return tree(n)
    else:
        left, right = fib_tree(n-2), fib_tree(n-1)
        fib_n = label(left) + label(right)
        return tree(fib_n, [left, right])
fib_tree(5)

def partition_tree(n, m):
    """Return a partition tree of n using parts of up to m."""
    if n == 0:
        return tree(True)
    elif n < 0 or m == 0:
        return tree(False)
    else:
        left = partition_tree(n-m, m)
        right = partition_tree(n, m-1)
        return tree(m, [left, right])
a = partition_tree(6, 4)

def print_parts(tree, partition=[]):
    if is_leaf(tree):
        if label(tree):
            print(' + '.join(partition))
    else:
        left, right = branches(tree)
        m = str(label(tree))
        print_parts(left, partition + [m])
        print_parts(right, partition)

print_parts(a)