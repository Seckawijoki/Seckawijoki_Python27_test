def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum
f = lazy_sum(*range(1,10,2))
print f
print f()

f1 = lazy_sum(*range(1,10,2))
f2 = lazy_sum(*range(1,10,2))
print f1 == f2
print f1(), f2()

def count():
    fs = []
    for i in range(1,4):
        def f():
            return i*i
        fs.append(f)
    return fs
f1, f2, f3 = count()
print f1(), f2(), f3()

def count2():
    fs = []
    for i in range(1,4):
        def f(j):
            def g():
                return j*j
            return g
        fs.append(f(i))
    return fs
f1, f2, f3 = count2()
print f1(), f2(), f3()