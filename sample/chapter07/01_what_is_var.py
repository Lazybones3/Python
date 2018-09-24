#python的变量本质上是一个指针
a = [1,2,3]
b = a
b.append(4)
print(a)
# 判断a和b是否是同一个对象
print(a is b)
print(id(a), id(b))

a = [1,2,3,4]
b = [1,2,3,4]
print(a is b)
# ==调用__eq__方法，判断值是否相等
print(a == b)