'''
序列化

我们把变量从内存中变成可存储或传输的过程称之为序列化，在Python中叫pickling，在其他语言中也被称之为serialization，marshalling，flattening等等.

序列化之后，就可以把序列化后的内容写入磁盘，或者通过网络传输到别的机器上。

反过来，把变量内容从序列化的对象重新读到内存里称之为反序列化，即unpickling。



Python提供了pickle模块来实现序列化。
'''
import pickle

d = dict(name = 'Bob', age = 20, score = 88)
# pickle.dumps()方法把任意对象序列化成一个bytes
print(pickle.dumps(d))

'''
1、可以把这个bytes写入文件。
2、用另一个方法pickle.dump()直接把对象序列化后写入一个file-like Object：
'''
f = open('samples/pickle.txt','wb')
pickle.dump(d,f)
f.close()




'''
当我们要把对象从磁盘读到内存时，可以先把内容读到一个bytes，然后用pickle.loads()方法反序列化出对象，也可以直接用pickle.load()方法从一个file-like Object中直接反序列化出对象。

我们打开另一个Python命令行来反序列化刚才保存的对象：
'''
f = open('samples/pickle.txt','rb')
d = pickle.load(f)
f.close()
print(d)

f = open('samples/pickle.txt','rb')
d = pickle.loads(f.read())
f.close()
print(d)
