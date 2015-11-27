class Student(object):
	pass

s = Student()
s.name = 'Michael'
print(s.name)

def set_age(self, age):
	self.age = age

from types import MethodType

# 给实例绑定一个方法：
s.set_age = MethodType(set_age, s)
s.set_age(23)
print(s.age)

# 给一个实例绑定的方法，对另一个实例是不起作用的：
s2 = Student()
'''
s2.set_age(25)
'''

# 为了给所有实例都绑定方法，可以给class绑定方法：
def set_score(self, score):
	self.score = score

Student.set_score = MethodType(set_score, Student)

s.set_score(100)
print(s.score)

s2.set_score(99)
print(s2.score)

# 通常情况下，上面的set_score方法可以直接定义在class中，但动态绑定允许我们在程序运行的过程中动态给class加上功能，这在静态语言中很难实现。



'''
使用__slots__

但是，如果我们想要限制实例的属性怎么办？比如，只允许对Student实例添加name和age属性。

为了达到限制的目的，Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性：
'''
class Student(object):
	"""docstring for Student"""
	__slots__ = ('name', 'age','score')

s = Student()
s.name = 'Michael'
s.age= 25
s.score = 99


'''
__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的：


除非在子类中也定义__slots__，这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__。
'''
class GraduateStudent(Student):
	"""docstring for GraduateStudent"""
	pass

g = GraduateStudent()
g.sss  = 999
