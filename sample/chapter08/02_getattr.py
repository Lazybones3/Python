from datetime import date

class User:
    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday

    #__getattr__在查找不到属性的时候调用
    def __getattr__(self, item):
        return "not find attr"

    #__getattribute__无论属性存不存在都会调用
    # def __getattribute__(self, item):
    #     return "bobby"

if __name__ == "__main__":
    user = User("bobby", date(1987,1,1))
    print(user.age)

