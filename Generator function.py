
def fibonacci(f):
    a = 0
    b = 1
    for i in range(f):
        i = a + b
        a = b
        b = i
        yield i

g = fibonacci(19)
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())
