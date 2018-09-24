# 列表生成式（列表推导式）
odd_list = [i for i in range(21) if i % 2 == 0]
print(odd_list)

# 逻辑复杂的情况
def handle_item(item):
    return item * item
odd_list = [handle_item(i) for i in range(21) if i % 2 == 0]
print(odd_list)

# 生成器表达式
odd_list = (i for i in range(21) if i % 2 == 0)

# 字典推导式
my_dict = {"a":1, "b":2, "c":3}
reversed_dict = {value:key for key,value in my_dict.items()}
print(reversed_dict)

# 集合推导式
my_set = {key for key,value in my_dict.items()}
print(my_set)