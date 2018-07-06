g =  (x * x for x in range(10))
print g
for n in g:
    print n

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a+b
        n = n + 1
print fib(6)

def odd():
    print 'step 1'
    yield 1
    print 'step 2'
    yield 3
    print 'step 3'
    yield 5
o = odd()
print o.next()
print o.next()
print o.next()

for n in fib(6):
    print n
