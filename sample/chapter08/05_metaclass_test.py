# 类也是对象，type创建类的类
def create_class(name):
    if name == "user":
        class User1:
            def __str__(self):
                return "user"
        return User1
    elif name == "company":
        class Company:
            def __str__(self):
                return "company"
        return Company

#type动态创建类
# User = type("User", (继承父类), {属性})

def say(self):
    # return self.name
    return "i am user"

class BaseClass:
    def answer(self):
        return "i am baseclass"

#元类就是创建类的类 type->class->对象
class MetaClass(type):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls, *args, **kwargs)
class User3(metaclass=MetaClass):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return "user"
# python中类的实例化过程，会首先寻找metaclass，通过metaclass去创建user类

if __name__ == "__main__":
    MyClass = create_class("user")
    my_obj1 = MyClass()
    print(type(my_obj1))

    User2 = type("User2", (BaseClass,), {"name":"user", "say":say})
    my_obj2 = User2()
    print(type(my_obj2))
    print(my_obj2.say())
    print(my_obj2.answer())

    my_obj3 = User3(name="bobby")
    print(my_obj3)

