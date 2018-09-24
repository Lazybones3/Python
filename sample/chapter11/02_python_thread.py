#对于io操作来说，多线程和多进程性能差别不大

import time
import threading
'''
def get_detail_html(url):
    print("get detail html started")
    time.sleep(2)
    print("get detail html end")

def get_detail_url(url):
    print("get detail url started")
    time.sleep(4)
    print("get detail url end")

if __name__ == "__main__":
    # 1.通过Thread类实例化
    thread1 = threading.Thread(target=get_detail_html, args=("",))
    thread2 = threading.Thread(target=get_detail_url, args=("",))
    # 设置为守护线程：当主线程退出的时候，守护线程直接kill掉
    # thread1.setDaemon(True)
    # thread2.setDaemon(True)
    start_time = time.time()
    thread1.start()
    thread2.start()

    # 阻塞主线程，等待thread1和thread2完成再继续执行
    thread1.join()
    thread2.join()

    print("last time: {}".format(time.time()-start_time))
'''

# 2.通过集成Thread来实现多线程
class GetDetailHtml(threading.Thread):
    def __init__(self, name):
        super().__init__(name=name)

    def run(self):
        print("get detail html started")
        time.sleep(2)
        print("get detail html end")

class GetDetailUrl(threading.Thread):
    def __init__(self, name):
        super().__init__(name=name)

    def run(self):
        print("get detail url started")
        time.sleep(4)
        print("get detail url end")

if __name__ == "__main__":
    # 2
    thread1 = GetDetailHtml("get_detail_html")
    thread2 = GetDetailUrl("get_detail_url")
    start_time = time.time()
    thread1.start()
    thread2.start()

    # 阻塞主线程，等待thread1和thread2完成再继续执行
    thread1.join()
    thread2.join()

    print("last time: {}".format(time.time()-start_time))