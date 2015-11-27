'''
reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，其效果就是：

reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
'''
from functools import reduce

def add(x,y):
	return x + y

print(reduce(add, [1,3,5,7,9]))
print(sum([1,3,5,7,9]))


def fn(x,y):
	return x * 10 + y

print(reduce(fn, [1,3,5,6,7]))

def char2num(s):
	return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]

print(list(map(char2num,'13579')))
print(reduce(fn,map(char2num,'13579')))


# 整理成一个str2int的函数就是：
def str2int(s):
	def fn(x,y):
		return x * 10 + y
	def char2num(s):
		return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]
	return reduce(fn,map(char2num,s))

print(str2int('2323234'))



# 还可以用lambda函数进一步简化成：
def char2num(s):
	return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]

def str2int(s):
	return reduce(lambda x,y : x * 10 + y, map(char2num,s))

print(str2int('2122323'))



def normalize(name):
	return name[0].upper()+name[1:].lower()

L1 = ['adam','LISA','barT']
L2 = list(map(normalize, L1))
print(L2)

def prod(s):
	def fn(x,y):
		return x * y
	return reduce(fn,s)
print('3*5*7*9=',prod([3,5,7,9]))


def str2float(s):
	def f1(x,y):
		return x * 10 + y
	def f2(x,y):
		return x * 0.1 + y
	def char2num(s):
		return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]
	str1,str2 = s.split('.')
	return reduce(f1,map(char2num,str1)) + reduce(f2,map(char2num,str2[::-1]))/10

print(str2float('23232.0004'))

