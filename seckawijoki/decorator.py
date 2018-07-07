#-*- coding: UTF-8 -*-
#coding=utf-8
def now():
    print '21:00'

print now.__name__
f = now
print f.__name__

import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print 'call %s():' % func.__name__
        return func(*args, **kw)
    return wrapper

@log
def now():
    print '7-6 21:00'
print now()

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print '%s %s():' % (text, func.__name__)
            return func(*args, **kw)
        return wrapper
    return decorator

@log('execute')
def now():
    print '2018-7-6 21:00'
print now()

print now.__name__

#practice
'''
请编写一个decorator，能在函数调用的前后打印出'begin call'和'end call'的日志。
'''
def head_tail():
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print 'begin call %s():' % func.__name__
            result = func(*args, **kw)
            print 'end call %s():' % func.__name__
            return result
        return wrapper
    return decorator
@head_tail()
def now():
    print '2018-7-6 21:00:56.24'
print now()
'''
能否写出一个@log的decorator，使它既支持：
@log
def f():
    pass
又支持：
@log('execute')
def f():
    pass
'''
import types
def log(string_or_function):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print '%s %s():' % (string_or_function, func.__name__)
            return func(*args, **kw)
        return wrapper
    if isinstance(string_or_function, types.StringType) and len(string_or_function) != 0:
        return decorator
    else:
        @functools.wraps(string_or_function)
        def emptyDecorator(*args, **kw):
            print 'practice empty log text: call %s():' % string_or_function.__name__
            return string_or_function(*args, **kw)
        return emptyDecorator


@log
def now():
    print '2018-7-6 21:00 Friday'
print now()

@log('practice log: execute')
def now():
    print '2018-7-6 9:00pm Friday'
print now()

