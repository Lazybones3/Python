from collections.abc import Iterator

class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list

    # def __getitem__(self, item):
    #     return self.employee[item]

    def __iter__(self):
        return MyIterator(self.employee)

#自定义迭代器
class MyIterator(Iterator):
    def __init__(self, employee_list):
        self.iter_list = employee_list
        self.index = 0

    def __next__(self):
        #真正返回迭代值的逻辑
        try:
            word = self.iter_list[self.index]
        except IndexError:
            raise StopIteration
        self.index += 1
        return word

if __name__ == "__main__":
    company = Company(["tom", "bob", "jane"])
    # 1.实现了__getitem__就可以进行遍历
    # 2.进行for循环的时候，底层会尝试调用iter()，iter首先会去找__iter__，
    # 如果没有就创建一个默认的迭代器，然后迭代器会使用__getitem__
    # my_item = iter(company)
    # for item in company:
    #     print (item)

    my_itor = iter(company)
    while True:
        try:
            print (next(my_itor))
        except StopIteration:
            pass

