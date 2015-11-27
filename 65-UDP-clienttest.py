'''
客户端使用UDP时，首先仍然创建基于UDP的Socket


然后，不需要调用connect()，直接通过sendto()给服务器发数据：
'''
import socket

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)


for data in [b'Jue',b'asd',b'rer']:
    s.sendto(data,('127.0.0.1',9999))
    print(s.recv(1024).decode('utf-8'))
s.close()
