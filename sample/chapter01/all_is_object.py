def ask(name="bobby"):
    print(name)

class Person:
    def __init__(self):
        print("baby")

# 对象可以添加到集合对象中
# obj_list = []
# obj_list.append(ask)
# obj_list.append(Person)
# for item in obj_list:
#     print(item())

# 对象可以当作函数的返回值
def decorator_func():
    print("dec start")
    return ask

my_ask = decorator_func()
my_ask("tom")