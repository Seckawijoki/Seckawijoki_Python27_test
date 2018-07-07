print map(lambda x: x*x, range(1,10))

f = lambda x: x*x
print f
print f(5)

def build(x, y):
    return lambda: x*x+y*y
print build
print build(3, 4)
f=build
print f(3,4)