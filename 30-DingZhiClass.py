'''
定制类

看到类似__slots__这种形如__xxx__的变量或者函数名就要注意，这些在Python中是有特殊用途的。
'''

'''
__str__
'''
class Student(object):
	def __init__(self, name):
		self.name = name

print(Student('Mic'))
		

class Student(object):
	def __init__(self, name):
		self.name = name
	def __str__(self):
		return 'Student object (name:%s)' % self.name

print(Student('Mic'))

# __str__()返回用户看到的字符串，而__repr__()返回程序开发者看到的字符串，也就是说，__repr__()是为调试服务的。
s = Student('Michael')
print(s)
print(s.__repr__())


'''
__iter__

如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法，该方法返回一个迭代对象
然后，Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，直到遇到StopIteration错误时退出循环。
'''

# 以斐波那契数列为例，写一个Fib类，可以作用于for循环：
class Fib(object):
	def __init__(self):
		self.a,self.b = 0,1
	def __iter__(self):
		return self
	def __next__(self):
		self.a,self.b = self.b,self.a+self.b
		if self.a > 100000:
			raise StopIteration()
		return self.a

for n in Fib():
	print(n)
		


'''
__getitem__

Fib实例虽然能作用于for循环，看起来和list有点像，但是，把它当成list来使用还是不行

print(Fib()[5])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'Fib' object does not support indexing

要表现得像list那样按照下标取出元素，需要实现__getitem__()方法：
'''
class Fib(object):
	def __getitem__(self, n):
		a,b = 1,1
		for x in range(n):
			a,b = b, a+b
		return a

f = Fib()
print(f[0])
print(f[10])
print(f[20])
print(f[30])
print(f[40])
print(f[50])



# 切片功能
# __getitem__()传入的参数可能是一个int，也可能是一个切片对象slice，所以要做判断：
class Fib(object):
	"""docstring for Fib"""
	def __getitem__(self, n):
		if isinstance(n,int):
			a,b = 1,1
			for x in range(n):
				a,b = b,a+b
			return a
		if isinstance(n,slice):
			start = n.start
			stop = n.stop
			if start is None:
				start = 0
			a,b = 1,1
			L = []
			for x in range(stop):
				if x >= start:
					L.append(a)
				a,b = b,a+b
			return L

f = Fib()
print(f[0:10])
print(f[:20])



'''
__getattr__

正常情况下，当我们调用类的方法或属性时，如果不存在，就会报错。
'''
class Student(object):
	def __init__(self):
		self.name = 'Michael'
	def __getattr__(self,attr):
		if attr == 'score':
			return 99
		return attr
s = Student()
print(s.name)
print(s.score)
print(s.asd)


# 链式调用
class Chain(object):
	def __init__(self, path = ''):
		self._path = path
	def __getattr__(self,path):
		return Chain('%s/%s' % (self._path,path))
	def __str__(self):
		return self._path
	__repr__ = __str__

print(Chain().status.user.timeline.list)



'''
__call__

一个对象实例可以有自己的属性和方法，当我们调用实例方法时，我们用instance.method()来调用。
'''
# 任何类，只需要定义一个__call__()方法，就可以直接对实例进行调用。
class Student(object):
	def __init__(self, name):
		self.name = name
	def __call__(self):
		print('My name is %s.' % self.name)
		
s = Student('Michael')
s()
Student('jue')()



# 怎么判断一个变量是对象还是函数呢？
# 其实，更多的时候，我们需要判断一个对象是否能被调用，能被调用的对象就是一个Callable对象
# 比如函数和我们上面定义的带有__call__()的类实例：
print(callable(Student('')))
print(callable(max))
print(callable([1,2,3]))
print(callable(None))
print(callable('str'))


