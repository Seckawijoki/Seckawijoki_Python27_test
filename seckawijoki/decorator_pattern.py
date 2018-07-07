import types
import functools
def decorator(func):
    if not isinstance(func, types.FunctionType):
        pass
    else:
        def wrapper(*args, **kw):
            i=0
            def decoratorDepth(j):
                def increaseDecoratorDepth():
                    return ++j
                return increaseDecoratorDepth()
            print 'call %s() depth = %i ' % (func.__name__, decoratorDepth(i))
            return func(*args, **kw)
        return wrapper

def now():
    print '2018-7-7 11:57'
decor = decorator(now)
decor = decorator(decor)
decor = decorator(decor)
decor = decorator(decor)
print decor()
