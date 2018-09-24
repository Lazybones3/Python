#1.epoll并不代表一定比select好
#在并发高的情况下，连接活跃度不是很高，epoll比select好
#并发性不高，同时连接很活跃，select比epoll好

import socket
from urllib.parse import urlparse


#使用非阻塞IO实现http请求
def get_url(url):
    # 通过socket请求html
    url = urlparse(url)
    host = url.netloc
    path = url.path
    if path == "":
        path = "/"

    # 建立socket连接
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 非阻塞
    client.setblocking(False)
    try:
        client.connect((host, 80))  #阻塞不会消耗cpu
    except BlockingIOError as e:
        pass

    # 通过while循环不断检查连接是否建立好，需要消耗cpu
    while True:
        try:
            client.send("GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(path,host).encode("utf8"))
            break
        except OSError as e:
            pass

    data = b""
    while True:
        try:
            d = client.recv(1024)
        except BlockingIOError as e:
            continue

        if d:
            data += d
        else:
            break
    data = data.decode("utf8")
    print(data)
    client.close()