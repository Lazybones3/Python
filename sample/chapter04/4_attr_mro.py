# 菱形继承
# class D:
#     pass
# class C(D):
#     pass
# class B(D):
#     pass
# class A(B,C):
#     pass
# print(A.__mro__)

class D:
    pass
class E:
    pass
class C(E):
    pass
class B(D):
    pass
class A(B,C):
    pass
print(A.__mro__)

# MRO查找使用C3算法
