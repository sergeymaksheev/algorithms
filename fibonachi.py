def fibonachi():
    a, b = 0, 1
    while 1:
        a, b = b, a + b
        yield a

s = fibonachi(100)
next(s)

