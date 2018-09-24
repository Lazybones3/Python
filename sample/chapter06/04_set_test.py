s = set("abcdee")
# s = set(['a','b','c','d','e'])
print(s)

# frozenset 创建后不能更改，可以作为dict的key
# fs = frozenset("abcde")

# 向set添加数据
another_set = set("cef")
# s.update(another_set)
# print(s)

# 差集
re_set = s.difference(another_set)
# re_set = s - another_set
# re_set = s | another_set    #并集
# re_set = s & another_set    #交集
print(re_set)
