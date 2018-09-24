# python中函数的工作原理
import inspect
frame = None
def foo():
    bar()
def bar():
    global frame
    frame = inspect.currentframe()
'''
python.exe会用一个叫做PyEval_EvalFramEx(c函数)去执行foo函数
首先会创建一个栈帧(stack_frame)
在调用foo时，首先会生成一个栈帧对象，然后在栈帧的上下文中运行字节码
当foo调用子函数bar，又会创建一个栈帧
所有的栈帧都是分配在堆内存上，这就决定了栈帧可以独立于调用者存在
'''
# import dis
# # 查看字节码对象
# print(dis.dis(foo))

foo()
# 打印frame的栈帧
print(frame.f_code.co_name)
caller_frame = frame.f_back
# 打印调用frame的栈帧
print(caller_frame.f_code.co_name)

def gen_func():
    yield 1
    name = "bobby"
    yield 2
    age = 30
    return "imooc"
import dis
gen = gen_func()
print(dis.dis(gen))

# f_lasti保存上一次yield的状态
print(gen.gi_frame.f_lasti)
print(gen.gi_frame.f_locals)
next(gen)
print(gen.gi_frame.f_lasti)
print(gen.gi_frame.f_locals)
next(gen)
print(gen.gi_frame.f_lasti)
print(gen.gi_frame.f_locals)

# UserList通过生成器完成迭代
# from collections import UserList