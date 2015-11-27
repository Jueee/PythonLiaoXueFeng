'''
IO在计算机中指Input/Output，也就是输入和输出。由于程序和运行时数据是在内存中驻留，由CPU这个超快的计算核心来执行，涉及到数据交换的地方，通常是磁盘、网络等，就需要IO接口。
'''


'''
读文件

要以读文件的模式打开一个文件对象，使用Python内置的open()函数，传入文件名和标示符：
'''

# open()函数，传入文件名和标示符
f = open('samples/sample.txt','r')
# 调用read()方法可以一次读取文件的全部内容
s = f.read()
print(s)
# 调用close()方法关闭文件
# 文件使用完毕后必须关闭，因为文件对象会占用操作系统的资源
# 并且操作系统同一时间能打开的文件数量也是有限的
f.close()



'''
由于文件读写时都有可能产生IOError，一旦出错，后面的f.close()就不会调用。
所以，为了保证无论是否出错都能正确地关闭文件，我们可以使用try ... finally来实现：
'''
try:
	f = open('samples/sample.txt','r')
	print(f.read())
except Exception as e:
	raise e
finally:
	if f:
		f.close()



'''
但是每次都这么写实在太繁琐，所以，Python引入了with语句来自动帮我们调用close()方法
'''
with open('samples/sample.txt','r') as f:
	print(f.read())




'''
调用read()会一次性读取文件的全部内容，如果文件有10G，内存就爆了
所以，要保险起见，可以反复调用read(size)方法，每次最多读取size个字节的内容。

另外，调用readline()可以每次读取一行内容，调用readlines()一次读取所有内容并按行返回list。
因此，要根据需要决定怎么调用。

1、如果文件很小，read()一次性读取最方便
2、如果不能确定文件大小，反复调用read(size)比较保险
3、如果是配置文件，调用readlines()最方便
'''
f = open('samples/sample.txt','r')
for line in f.readlines():
	print(line.strip())  # 把末尾的'\n'删掉
f.close()


# 二进制文件
f = open('samples/sample.jpg','r')
print(f.read())
f.close()


# 字符编码
# 要读取非UTF-8编码的文本文件，需要给open()函数传入encoding参数，例如，读取GBK编码的文件：
f = open('samples/sample.txt', 'r', encoding='gbk')
print(f.read())
f.close()



'''
遇到有些编码不规范的文件，你可能会遇到UnicodeDecodeError，因为在文本文件中可能夹杂了一些非法编码的字符。
遇到这种情况，open()函数还接收一个errors参数，表示如果遇到编码错误后如何处理。

最简单的方式是直接忽略：
f = open('','r',encoding='gbk',errors='ignore')
'''





'''
写文件

写文件和读文件是一样的，唯一区别是调用open()函数时，传入标识符'w'或者'wb'表示写文本文件或写二进制文件：
'''
f = open('samples/sample.txt','w')
f.write('Hello World!!!')
f.close()


with open('samples/sample.txt','w') as f:
	f.write('Jue...')
