from concurrent.futures import ThreadPoolExecutor,as_completed
from concurrent.futures import ProcessPoolExecutor
import time
#多进程编程
#对于耗费cpu的操作，用多进程编程；
#对于io操作，用多线程编程，因为进程的切换代价大于线程

# 1.cpu操作，多进程优于多线程
'''
def fib(n):
    if n <= 2:
        return 1
    return fib(n-1) + fib(n-2)

if __name__ == "__main__":
    with ThreadPoolExecutor(3) as executor:
    # with ProcessPoolExecutor(3) as executor:
        all_task = [executor.submit(fib, (num)) for num in range(25,35)]
        start_time = time.time()
        for future in as_completed(all_task):
            data = future.result()
            print("exe result: {}".format(data))
        print("last time is: {}".format(time.time()-start_time))
'''

#2.io操作，多线程优于多进程
def random_sleep(n):
    time.sleep(n)
    return n

if __name__ == "__main__":
    # with ThreadPoolExecutor(3) as executor:
    with ProcessPoolExecutor(3) as executor:
        all_task = [executor.submit(random_sleep, (num)) for num in [2]*30]
        start_time = time.time()
        for future in as_completed(all_task):
            data = future.result()
            print("exe result: {}".format(data))
        print("last time is: {}".format(time.time()-start_time))