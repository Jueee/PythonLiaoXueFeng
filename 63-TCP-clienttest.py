'''
测试服务器程序，我们还需要编写一个客户端程序：
'''
import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# 建立连接:
s.connect(('127.0.0.1',2222))
# 接收欢迎消息:
print(s.recv(1024).decode('utf-8'))
for data in [b'Michael',b'Tracy',b'Jue']:
    # 发送数据:
    s.send(data)
    print(s.recv(1024).decode('utf-8'))
s.send(b'exit')
s.close()
