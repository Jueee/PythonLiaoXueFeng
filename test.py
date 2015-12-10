import socket

myname = socket.gethostname()
myaddr = socket.gethostbyname(myname)
print(myaddr,myname)