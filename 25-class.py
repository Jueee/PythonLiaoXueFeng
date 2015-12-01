

class Student(object):
	"""docstring for Student"""
	def __init__(self, name, score):
		self.name = name
		self.score = score
	def print_score(self):
		print('%s : %s ' % (self.name, self.score))


bart = Student('bart', 59)
lisa = Student('lisa', 78)
bart.print_score()
lisa.print_score()

print(bart.name)
bart.score=89
print(bart.score)


'''
如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__

在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问

所以，我们把Student类改一改：
'''
class Student2(object):
	"""docstring for Student"""
	def __init__(self, name, score):
		self.__name = name
		self.__score = score
	def print_score(self):
		print('%s : %s ' % (self.__name, self.__score))
	def get_name(self):
		return self.__name

bartt = Student2('bart', 59)
bartt.print_score()
bartt.swecore=89
print(bartt.swecore)
print(bartt.get_name())
'''
双下划线开头的实例变量是不是一定不能从外部访问呢？

其实也不是。
不能直接访问__name是因为Python解释器对外把__name变量改成了_Student__name

所以，仍然可以通过_Student__name来访问__name变量：
'''
print(bartt._Student2__name)