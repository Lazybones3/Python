import socket
from urllib.parse import urlparse
from selectors import DefaultSelector, EVENT_WRITE, EVENT_READ

#使用select完成http请求
selector = DefaultSelector()

urls = []
stop = False

class Fetcher:
    def connected(self, key):
        selector.unregister(key.fd)
        self.client.send("GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(self.path, self.host).encode("utf8"))
        selector.register(self.client.fileno(), EVENT_READ, self.readable)

    def readable(self, key):
        d = self.client.recv(1024)
        if d:
            self.data += d
        else:
            selector.unregister(key.fd)
            data = self.data.decode("utf8")
            html_data = data.split("\r\n\r\n")[1]
            print(html_data)
            self.client.close()
            urls.remove(self.spider_url)
            if not urls:
                global stop
                stop = True

    def get_url(self, url):
        self.spider_url = url
        url = urlparse(url)
        self.host = url.netloc
        self.path = url.path
        self.data = b""
        if self.path == "":
            self.path = "/"

        # 建立socket连接
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 非阻塞
        self.client.setblocking(False)

        try:
            self.client.connect((self.host, 80))  # 阻塞不会消耗cpu
        except BlockingIOError as e:
            pass

        # 注册
        selector.register(self.client.fileno(), EVENT_WRITE, self.connected)

# import select
# select.select()
# 1.select本身是不支持register模式
# 2.socket状态变化以后的回调是由程序员完成的
def loop():
    #事件循环，不停地请求socket的状态并调用对应的回调函数
    # 一般模式：回调+事件循环+select(poll/epoll)
    while not stop:
        ready = selector.select()
        for key, mask in ready:
            call_back = key.data
            call_back(key)


if __name__ == "__main__":
    urls.append("http://www.baidu.com")
    fetcher = Fetcher()
    fetcher.get_url("http://www.baidu.com")
    # 整个回调是由事件循环来驱动的
    loop()

    #测速
    # import time
    # start_time = time.time()
    # for url in range(20):
    #     url = "http://shop.projectsedu.com/goods/{}/".format(url)
    #     urls.append(url)
    #     fetcher = Fetcher()
    #     fetcher.get_url(url)
    # loop()
    # print(time.time() - start_time)