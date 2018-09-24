class A:
    pass

class B(A):
    pass

b = B()
# isinstance会顺着继承的链查找，所以判断类型尽量用isinstance
print(isinstance(b, B))
print(isinstance(b, A))
print(type(b))

# is是判断id是否相等，==是判断值是否相等
print(type(b) is B)
print(type(b) is A)
print(type(b) == B)
