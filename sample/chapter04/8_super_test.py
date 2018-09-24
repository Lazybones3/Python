class A:
    def __init__(self):
        print("A")

class B(A):
    def __init__(self):
        print("B")
        # python2中调用父类初始化方法
        # super(B,self).__init__()
        # python3中调用父类初始化方法
        super().__init__()
        # 注：多继承中super()调用的顺序是mro中的下一个类

if __name__ == "__main__":
    b = B()