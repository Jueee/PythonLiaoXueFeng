# 判断对象类型，使用type()函数：
print(type(1233))
print(type('str'))
print(type(None))

# 如果一个变量指向函数或者类，也可以用type()判断：
print(type(abs))
print(type(type(1)))

print(type(123)==type(234))
print(type(123)==int)
print(type('abs')==str)
print(type('abc')==type(123))


print('---------------------------------')

# 判断基本数据类型可以直接写int，str等，但如果要判断一个对象是否是函数怎么办？可以使用types模块中定义的常量：
import types

def fn():
	pass

print(type(fn)==types.FunctionType)
print(type(abs)==types.BuiltinFunctionType)
print(type(lambda x : x)==types.LambdaType)
print(type((x for x in range(10)))==types.GeneratorType)


print('---------------------------------')


# 如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list
print(dir('abc'))

print('and'.__len__())
print(len('abcd'))

class MyDog(object):
	"""docstring for MyDog"""
	def __len__(self):
		return 100

dog = MyDog()
print(len(dog))


print('---------------------------------')


class MyObject(object):
	"""docstring for MyObject"""
	def __init__(self):
		self.x = 9
	def power(self):
		return self.x * self.x

obj = MyObject()
print(hasattr(obj, 'x'))  # 有属性'x'吗？
print(obj.x)              # 获取属性'x'
print(hasattr(obj, 'y'))  # 有属性'y'吗？
setattr(obj, 'y', 19)     # 设置一个属性'y'
print(hasattr(obj, 'y'))  # 有属性'y'吗？
print(obj.y)              # 获取属性'y'

# 可以传入一个default参数，如果属性不存在，就返回默认值：
print(getattr(obj, 'z', 404)) # 获取属性'z'，如果不存在，返回默认值404

# 也可以获得对象的方法：
print(hasattr(obj, 'power'))
print(getattr(obj, 'power'))
fn = getattr(obj, 'power')
print(fn)
print(fn())


def readImage(fp):
	if hasattr(fp, 'read'):
		return readData(fp)
	return None
	