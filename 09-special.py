L = []
n = 1
while n<=99:
	L.append(n)
	n = n + 2
print(L)

print(list(range(100))[1::2])

L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print(L[0],L[1],L[2])
print(L[:3])

d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
	print(key,d.get(key))

# 判断一个对象是可迭代对象:通过collections模块的Iterable类型判断
from collections import Iterable
print(isinstance('abc',Iterable))
print(isinstance([1,2,3],Iterable))
print(isinstance(123,Iterable))


# 如果要对list实现类似Java那样的下标循环怎么办
# Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身
for i,value in enumerate(['A','B','C']):
	print(i,value)

d={'a':1,'b':2,'c':3}
for key , value in d.items():
    print (key,value )