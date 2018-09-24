import time
import threading
from chapter11 import variables
# 一个坑
# from chapter11.variables import detail_url_list

# 1.线程通信方式：共享变量
# detail_url_list = []
def get_detail_html():
    # 爬取文章详情页
    # global detail_url_list
    detail_url_list = variables.detail_url_list
    while True:
        if len(detail_url_list):
            url = detail_url_list.pop()
            print("get detail html started")
            time.sleep(2)
            print("get detail html end")

def get_detail_url():
    # 爬取文章列表页
    # global detail_url_list
    detail_url_list = variables.detail_url_list
    while True:
        print("get detail url started")
        time.sleep(4)
        for i in range(20):
            detail_url_list.append("http://projectsedu.com/{id}".format(id=i))
        print("get detail url end")

if __name__ == "__main__":
    thread_detail_url = threading.Thread(target=get_detail_url)
    for i in range(10):
        html_thread = threading.Thread(target=get_detail_html)
        html_thread.start()