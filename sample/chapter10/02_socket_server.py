import socket
import threading

# tcp
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(("0.0.0.0", 8000))
server.listen()
'''
sock, addr = server.accept()
while True:
    data = sock.recv(1024)
    print(data.decode("utf8"))
    re_data = input()
    sock.send(re_data.encode("utf8"))
'''

def handle_sock(sock, addr):
    while True:
        data = sock.recv(1024)
        print(data.decode("utf8"))
        re_data = input()
        sock.send(re_data.encode("utf8"))

while True:
    sock, addr = server.accept()
    # 用线程去处理新接收的连接（用户）
    client_threading = threading.Thread(target=handle_sock, args=(sock,addr))
    client_threading.start()

