print abs
def f(x):
    return x*x

def add(x, y, f=None):
    if f is not None:
        return f(x) + f(y)
    else:
        return x+y

print add(-5, 6, abs)

print map(f, range(1,10))
print map(str, range(1,10))

print reduce(add, range(1,10,2))

def fn(x, y):
    return x*10+y
print reduce(fn, range(1,10,2))

def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

print reduce(fn, map(char2num, '13579'))

def str2int(s):
    def fn(x, y):
        return x*10+y
    def char2num(c):
        return {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}[c]
    return reduce(fn, map(char2num, s))
print str2int('13579')

def str2int_(s):
    return reduce(lambda x, y: x*10+y, map(char2num, s))
print(str2int_('13579'))

#practice
def correctName(s):
    s = s.lower()
    s = str.capitalize(s)
    return s

def correctNameList(L):
    return map(correctName, L)
print correctNameList(['adam', 'LISA', 'barT'])

def prod(L=None):
    if L is None:
        pass
    else:
        return reduce(lambda x, y: x*y, L)
print prod(range(1,7))