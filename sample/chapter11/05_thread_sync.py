# 1.分析字节码
def add1(a):
    a += 1
def desc1(a):
    a -= 1
'''
add
1. load a   a=0
2. load 1   1
3. +        +1
4. 赋值给a  a=1   

desc
1. load a   a=0
2. load 1   1
3. -        -1
4. 赋值给a  a=-1
'''
import dis
# print(dis.dis(add1))
# print(dis.dis(desc1))

# 2.线程同步
from threading import Lock

total = 0
lock = Lock()
def add():
    global total
    global lock
    for i in range(1000000):
        # 获取锁
        lock.acquire()
        # lock.acquire()  #还没释放又获取会引起死锁
        total += 1
        # 释放锁
        lock.release()

def desc():
    global total
    global lock
    for i in range(1000000):
        lock.acquire()
        total -= 1
        lock.release()

import threading
thread1 = threading.Thread(target=add)
thread2 = threading.Thread(target=desc)
thread1.start()
thread2.start()

thread1.join()
thread2.join()
print(total)

# 1.用锁会影响性能
# 2.锁会引起死锁
'''
死锁的情况，线程A和B
A(a, b)
acquire(a)
acquire(b)

B(a, b)
acquire(b)
acquire(a)
'''

# Rlock可重入的锁：在同一个线程中可以调用多次acquire，但要注意acquire的次数和release的次数要相同