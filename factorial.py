def factorial(n: int) -> int:
    res = 1
    while n:
        res *= n
        n -= 1
    return res


def factorial2(n: int) -> int:
    a, res = 1, 1
    while a <= n:
        res = res * a
        a += 1
    return res

def fact(n):
    if n == 1:
        return n
    return n * fact(n-1)
