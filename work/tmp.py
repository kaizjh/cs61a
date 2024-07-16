def o(s, key=lambda x: x * x):
    if s == 0:
        return
    print(key(s))
    o(s - 1, key)

o(10)
print("____________________________________")
o(10, key = lambda x: x)