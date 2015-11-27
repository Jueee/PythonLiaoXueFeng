'''
在绑定属性时，如果我们直接把属性暴露出去，虽然写起来很简单，但是，没办法检查参数，导致可以把成绩随便改：
'''
class Student(object):
	"""docstring for Student"""
	pass
		

s = Student()
s.score = 999


# 为了限制score的范围，可以通过一个set_score()方法来设置成绩，再通过一个get_score()来获取成绩 
# 这样，在set_score()方法里，就可以检查参数：
class Student(object):
	"""docstring for Student"""
	def get_score(self):
		return self._score
	def set_score(self, value):
		if not isinstance(value, int):
			raise ValueError('score must be an integer')
		if value < 0 or value > 100:
			raise ValueError('score must between 0~100')
		self._score = value

s = Student()
s.set_score(60)
print(s.get_score())	
'''
s.set_score(999)
'''

# 上面的调用方法又略显复杂，没有直接用属性这么直接简单。

# 既能检查参数，又可以用类似属性这样简单的方式来访问类的变量
class Student(object):
	"""docstring for Student"""
	@property
	def score(self):
		return self._score
	@score.setter
	def score(self,value):
		if not isinstance(value, int):
			raise ValueError('score must be an integer')
		if value < 0 or value > 100:
			raise ValueError('score must between 0~100')
		self._score = value
'''
@property的实现比较复杂，我们先考察如何使用。
把一个getter方法变成属性，只需要加上@property就可以了
此时，@property本身又创建了另一个装饰器@score.setter，负责把一个setter方法变成属性赋值
于是，我们就拥有一个可控的属性操作
'''
s = Student()
s.score = 60
print(s.score)
'''
s.score = 999	
'''

# 还可以定义只读属性，只定义getter方法，不定义setter方法就是一个只读属性
class Student(object):
	@property
	def birth(self):
		return self._birth
	@birth.setter
	def birth(self, value):
		self._birth = value
	@properth
	def age(self):
		return 2015 - self._birth

# 上面的birth是可读写属性，而age就是一个只读属性，因为age可以根据birth和当前时间计算出来。

		


