from collections.abc import Iterable, Iterator
a = [1,2]
# 可迭代对象：实现__iter__
print(isinstance(a, Iterable))
# 迭代器：实现__next__和__iter__
print(isinstance(a, Iterator))

iter_rator = iter(a)
print(isinstance(iter_rator, Iterator))