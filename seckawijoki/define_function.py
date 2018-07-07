import math

def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x

def empty_function():
    pass

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y + step * math.sin(angle)
    return nx, ny

def power(x, n=2):
    s = 1
    while n > 0:
        n -= 1
        s *= x
    return s

print power(5)
print power(5, 2)

x, y = move(100, 100, 60, math.pi / 6)
print x, y

def add_end(L=None):
    if L is None:
        L=[]
    L.append('END')
    return L

print add_end()
print add_end()
print add_end()

def calc(*numbers):
    sum = 0
    for n in numbers:
        sum += n*n
    return sum

print calc(1,2,3)
print calc(1,3,5,7)
nums=[1,2,3]
print calc(*nums)

def person(name, age, **kw):
    print 'name: ', name, ' | age: ', age, ' | other: ',kw

print person('Michael', 30)
print person('Bob', 35, city='Beijing')
print person('Adam', 45, gender='M', job='Engineer')
kw={'city':'Beijing', 'job':'Engineer'}
print person('Jack', 24, **kw)

def func(a, b, c=0, *args, **kw):
    print 'a = ', a, 'b = ', b, 'c = ', c, 'args = ', args, 'kw = ', kw

print func(1, 2)
print func(1, 2, c=3)
print func(1, 2, 3, 'a', 'b')
print func(1, 2, 3, 'a', 'b', x=99)
args=(1,2,3,4)
kw={'x': 99}
print func(*args, **kw)

def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)

print fact(5)
print fact(10)
print fact(100)