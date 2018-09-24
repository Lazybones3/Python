class A:
    # 类变量
    aa = 1
    def __init__(self, x, y):
        # 对象变量
        self.x = x
        self.y = y

a = A(2,3)
A.aa = 11
# 修改对象变量，会在对象中新建一个变量aa
a.aa = 100
print(a.x, a.y, a.aa)
print(A.aa)
# 类变量是所有实例共享的
b = A(3,4)
print(b.aa)