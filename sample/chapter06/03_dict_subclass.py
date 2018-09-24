# 不建议继承list和dict
from collections import UserDict

class Mydict(UserDict):
    def __setitem__(self, key, value):
        super().__setitem__(key, value * 2)


my_dict = Mydict(one=1)
print(my_dict)


from collections import defaultdict
my_dict = defaultdict(list)
my_value = my_dict["bobby"]
print(my_value)