def f(n):
    if n > 0:
        prev = f(n - 1)
        print(prev)
    return[n]

l = f(5)
print(l)