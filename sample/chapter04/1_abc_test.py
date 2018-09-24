class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list

    def __len__(self):
        return len(self.employee)


com = Company(["bobby1", "bobby2"])
print(hasattr(com, "__len__"))

from collections.abc import Sized
print(isinstance(com, Sized))

import abc
# 模拟一个抽象基类，类似java里的接口
class CacheBase(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get(self, key):
        pass
    @abc.abstractmethod
    def set(self, key, value):
        pass

class RedisCache(CacheBase):
    def get(self, key):
        pass

    def set(self, key, value):
        pass

redis_cache = RedisCache()