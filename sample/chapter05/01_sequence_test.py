# +类型必须一样
a = [1,2]
c = a + [3.4]
print(c)

# 就地加
# +=只要求可迭代类型
a += (3,4)

a.extend(range(3))

a.append([1,2])
print(a)