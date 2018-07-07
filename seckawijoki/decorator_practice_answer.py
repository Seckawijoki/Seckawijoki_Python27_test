#-*- coding:utf-8 -*-
import functools
import types
'''
请编写一个decorator，能在函数调用的前后打印出
'begin call'和'end call'的日志。
'''
#这个不难
def logt(text):
    def log(func):
        @functools.wraps(func)
        def wrapper(*args,**kw):
            print '%s %s():'% (text,func.__name__)
            func(*args,**kw)
            print 'finish %s():'% func.__name__
        return wrapper
    return log
@logt('execute')
def current3():
    print 'nihaoa'
current3()

'''
再思考一下能否写出一个@log的decorator，使它
既支持：
@log
def f():
    pass
又支持：
@log('execute')
def f():
    pass
'''
#这个就有点难为我了,我就在此沦陷啦
#首先要使用默认值,这一点还是比较清楚的
#以下代码为模仿别人的
def log(text='execute'):
    def logdecorate(func):
        @functools.wraps(func)
        def wrapper(*args,**kw):
            '''
            如果text有值,那就要打印出该值
            如果没值,那就打印默认值,所以都是
            text
            '''
            print '%s %s()' % (text,func.__name__)
            return func(*args,**kw)
        return wrapper
    '''
    如果text参数有传值过来的话,
    说明用的是log('text'),即log('text')(now)
    这个时候要将log('text')转成logdecorate才成
    即函数原型,然后才能变为log('text')(now)==logdecorate(now)
    所以有参数时直接返回logdecorate函数
    '''
    #判断text是否属于函数类型
    if not isinstance(text,types.FunctionType):
        #为log('text')
        return logdecorate
    '''
    如果没有传值过来的话,说明用的是log,即log(now).
    text==now,其实就是要调用logdecorate(now)
    所以无参数时,直接返回调用logdecorate(now)的结果
    '''
    if isinstance(text,types.FunctionType):
        #为log形式
        return logdecorate(text)

@log
def func_one():
    print 'log has no args'
@log('diff')
def func_two():
    print 'log has args'
func_one()
func_two()
print func_one.__name__
print func_two.__name__


#然后有人用一个程序包含了上面2道题,
#我只能在地上挖矿啦.贴出这位前辈的代码
#才疏学浅,解释不清
def log(text='execute'):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print "begin call %s():" %(func.__name__)
            result = func(*args, **kw)
            if isinstance(text,types.StringType) and len(text) != 0:
                print 'text 的值为字符串类型'
                print "%s %s()" %(text, func.__name__)
            else:
                print "end call %s()" %(func.__name__)
            return result
        return wrapper
    if isinstance(text, types.FunctionType):
        print text
        print 'text 的值为函数类型'
        return decorator(text)
    else:
        print text
        print 'text的值不为函数类型，无参调用函数'
        return decorator

@log
def now():
    print 'mult'
print 'log 无参数:'
now()

@log('test')
def again():
    print 'you args'
print 'log 带参数:'
again()

#log('test')(now)
#我还有救么
