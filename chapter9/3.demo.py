# -*- coding:utf-8 -*-
__author__ = 'gjw'
__date__ = '2018/2/19 11:40'
# 9-3 如何定义带参数的装饰器

# 实现一个装饰器，它用来检查被装饰函数的参数类型，
# 装饰器可以通过参数指明函数参数的类型，
# 调用时如果检测出类型不匹配则抛出异常

# @typeassert(str, int, int)
# def f(a,b,c):
#     pass
#
# @typessert(y=list)
# def g(x,y):
#     pass

"""
    提取函数签名：inspect.signature()
    带参数的装饰器，也就是根据参数定制化一个装饰器，可以看成生产装饰器的工厂，
    每次调用typeassert，返回一个特定的装饰器，然后用它去修饰其他函数。
"""
from inspect import signature


def typeassert(*ty_args, **ty_kargs):
    def decorator(func):
        # 获取函数参数和类型的映射关系
        sig = signature(func)
        btypes = sig.bind_partial(*ty_args, **ty_kargs).arguments

        def wrapper(*args, **kargs):
            for name, obj in sig.bind(*args, **kargs).arguments.items():
                if name in btypes:
                    if not isinstance(obj, btypes[name]):
                        raise TypeError('"%s" must be "%s"' % (name, btypes[name]))
            return func(*args, **kargs)

        return wrapper

    return decorator


@typeassert(int, str, list)
def f(a, b, c):
    print(a, b, c)


f(1, 'abc', [1, 2, 3])
f(1, 2, [1, 2, 3])
