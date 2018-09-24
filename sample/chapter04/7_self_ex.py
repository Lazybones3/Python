#自省是通过一定的机制查询到对象的内部结构
class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __str__(self):
        return "{year}/{month}/{day}".format(year=self.year,month=self.month,day=self.day)

class Person:
    '''人'''
    name = "user"

class Student(Person):
    def __init__(self, school_name):
        self.school_name = school_name

if __name__ == "__main__":
    user = Student("慕课网")

    # 通过__dict__查询属性
    print(user.__dict__)    # 查询对象属性
    # name本质是Person对象的属性，这里调用的时候是向上查找
    print(user.name)
    print(Person.__dict__)  # 查询类的属性

    # user.__dict__["school_addr"] = "北京"
    # print(user.__dict__)

    # dir()列出对象中的所有属性，比__dict__更详细
    print(dir(user))

    # a = [1,2,3]
    # print(dir(a))