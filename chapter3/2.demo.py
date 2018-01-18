# -*- coding:utf-8 -*-
__author__ = 'gjw'
__time__ = '2018/1/18 0018 下午 3:29'
# 3-1 如何实现可迭代对象和迭代器对象

import requests

# 可以实现延迟访问
from collections import Iterable, Iterator
"""
    实现一个迭代器对象WeatherIterator，__next__方法每次返回一个城市气温
"""


class WeatherIterator(Iterator):
    def __init__(self, cities):
        self.cities = cities
        self.index = 0

    # 获取城市天气
    def getWeather(self, city):
        r = requests.get(u'http://wthrcdn.etouch.cn/weather_mini?city=' + city)
        data = r.json()['data']['forecast'][0]
        return '{}:{},{}'.format(city, data['low'], data['high'])

    def __next__(self):
        if self.index == len(self.cities):
            raise StopIteration
        city = self.cities[self.index]
        self.index += 1
        return self.getWeather(city)


"""
    实现一个可迭代对象WeatherIterable，__iter__方法返回一个迭代器对象
"""


class WeatherIterable(Iterable):
    def __init__(self, cities):
        self.cities = cities

    def __iter__(self):
        return WeatherIterator(self.cities)


c = ['北京', '上海', '广州', '长春']
for x in WeatherIterable(c):
    print(x)
