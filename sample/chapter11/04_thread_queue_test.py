# 1.线程通信方式：queue
import time
import threading
from queue import Queue

from chapter11 import variables

def get_detail_html(queue):
    # 爬取文章详情页
    detail_url_list = variables.detail_url_list
    while True:
        url = queue.get()
        print("get detail html started")
        time.sleep(2)
        print("get detail html end")

def get_detail_url(queue):
    # 爬取文章列表页
    detail_url_list = variables.detail_url_list
    while True:
        print("get detail url started")
        time.sleep(4)
        for i in range(20):
            queue.put("http://projectsedu.com/{id}".format(id=i))
        print("get detail url end")

if __name__ == "__main__":
    detail_url_queue = Queue(maxsize=1000)
    thread_detail_url = threading.Thread(target=get_detail_url,args=(detail_url_queue,))
    for i in range(10):
        html_thread = threading.Thread(target=get_detail_html,args=(detail_url_queue,))
        html_thread.start()
    start_time = time.time()
    detail_url_queue.task_done()
    detail_url_queue.join()
    print("last time: {}".format(time.time()-start_time))