import time
from multiprocessing import Process, Queue, Manager, Pipe
from multiprocessing.pool import Pool

'''
# 1.使用multiprocessing中的Queue
def producer(queue):
    queue.put("a")
    time.sleep(2)

def consumer(queue):
    time.sleep(2)
    data = queue.get()
    print(data)

if __name__ == "__main__":
    queue = Queue(10)
    my_producer = Process(target=producer,args=(queue,))
    my_consumer = Process(target=consumer,args=(queue,))
    my_producer.start()
    my_consumer.start()
    my_producer.join()
    my_consumer.join()


#2.共享全局变量通信不能用于多进程编程，只能用于多线程
def producer(a):
    a += 1
    time.sleep(2)

def consumer(a):
    time.sleep(2)
    print(a)

if __name__ == "__main__":
    a = 1
    my_producer = Process(target=producer,args=(a,))
    my_consumer = Process(target=consumer,args=(a,))
    my_producer.start()
    my_consumer.start()
    my_producer.join()
    my_consumer.join()


#3.multiprocessting中的Queue不能用于pool进程池
# pool进程池中的进程通信要用Manager中的Queue
def producer(queue):
    queue.put("a")
    time.sleep(2)

def consumer(queue):
    time.sleep(2)
    data = queue.get()
    print(data)

if __name__ == "__main__":
    queue = Manager().Queue(10)
    pool = Pool(2)
    pool.apply_async(producer,args=(queue,))
    pool.apply_async(consumer,args=(queue,))
    pool.close()
    pool.join()


#4.通过pipe实现进程间通信
#pipe性能高于queue
def producer(pipe):
    pipe.send("bobby")

def consumer(pipe):
    print(pipe.recv())

if __name__ == "__main__":
    #pip只能用于两个进程
    receive_pip, send_pip = Pipe()
    my_producer = Process(target=producer,args=(receive_pip,))
    my_consumer = Process(target=consumer,args=(send_pip,))
    my_producer.start()
    my_consumer.start()
    my_producer.join()
    my_consumer.join()
'''

#5.用Manager中的dict实现内存共享
def add_data(p_dict, key, value):
    p_dict[key] = value

if __name__ == "__main__":
    progress_dict = Manager().dict()

    first_progress = Process(target=add_data, args=(progress_dict,"bobby1",22))
    second_progress = Process(target=add_data, args=(progress_dict,"bobby2",23))
    first_progress.start()
    second_progress.start()
    first_progress.join()
    second_progress.join()
    print(progress_dict)