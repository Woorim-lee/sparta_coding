def fact(n):
    if n <=1:
        return 1
    return n * fact(n-1)

def sum(n):
    if n<=1:
        return 1
    return n + sum(n-1)

print(sum(10))