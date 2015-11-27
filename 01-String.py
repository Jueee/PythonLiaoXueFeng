print('包含中文的str')

print(ord('A'))

print(ord('中'))

print(chr(66))
print(chr(21334))


print('\u4e2d\u6587')

# 纯英文的str可以用ASCII编码为bytes，内容是一样的
print('ABC'.encode('ascii'))
# 含有中文的str可以用UTF-8编码为bytes。
print('中文'.encode('utf-8'))




# 如果我们从网络或磁盘上读取了字节流，那么读到的数据就是bytes。
# 要把bytes变为str，就需要用decode()方法
print(b'ABC'.decode('ascii'))
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))




# 要计算str包含多少个字符，可以用len()函数
print(len('ABC'))
print(len('中文'))



# len()函数计算的是str的字符数，如果换成bytes，len()函数就计算字节数
# 1个中文字符经过UTF-8编码后通常会占用3个字节，而1个英文字符只占用1个字节。
print(len(b'ABC'))
print(len(b'\xe4\xb8\xad\xe6\x96\x87'))
print(len('中文'.encode('utf-8')))


print('Hello %s' % 'world')

# 格式化整数和浮点数还可以指定是否补0和整数与小数的位数
print('%2d-%02d' % (3, 1))
print('%.2f %%' % 3.134233)


s1 = 72
s2 = 85
r = (s2 - s1)/s1 * 100
print('%02.1f%%' % r)