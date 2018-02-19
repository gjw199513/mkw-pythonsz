# -*- coding:utf-8 -*-
__author__ = 'gjw'
__date__ = '2018/2/19 10:53'
# 9-2 如何为被装饰的函数保存元数据

# 我们在使用装饰器后，再使用上面这些属性访问时，
# 看到的是内部包裹函数的元数据，原来函数的元数据
# 便丢失掉了，应该如何解决？


"""
    使用标准库functools中的装饰器wraps装饰内部包裹函数，
    可以制定将原函数的某些属性，更新到包裹函数上面。
"""
from functools import update_wrapper, wraps, WRAPPER_ASSIGNMENTS, WRAPPER_UPDATES


def mydecorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        """wrapper function"""
        print('In wrapper')
        func(*args, **kwargs)

    # 直接修改函数的名字
    # wrapper.__name__ = func.__name__

    # 使用update_wrapper函数来更新
    # update_wrapper(wrapper, func)
    return wrapper


@mydecorator
def example():
    """example function"""
    print('In example')


print(example.__name__)
print(example.__doc__)
# 打印默认参数
print(WRAPPER_ASSIGNMENTS)
print(WRAPPER_UPDATES)
