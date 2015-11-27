'''
我们来编写一个Dict类，这个类的行为和dict一致，但是可以通过属性来访问，用起来就像下面这样：
'''
class Dict(dict):
	"""docstring for Dict"""
	def __init__(self, **kw):
		super().__init__(**kw)
	def __getattr__(self,key):
		try:
			return self[key]
		except KeyError:
			raise AttributeError(r"'Dict' object has no attribute '%s'" % key)
	def __setattr__(self,key,value):
		self[key]=value

d = Dict(a=1,b=2)
print(d['a'])
print(d.a)

# 为了编写单元测试，我们需要引入Python自带的unittest模块，编写mydict_test.py如下：
import unittest

class Test(unittest.TestCase):
	def test_init(self):
		d = Dict(a=1,b='test')
		self.assertEqual(d.a,1)
		self.assertEqual(d.b,'test')
		self.assertTrue(isinstance(d,dict))
	def test_key(self):
		d = Dict()
		d['key'] = 'value'
		self.assertEqual(d.key,'value')
	def test_attr(self):
		d = Dict()
		d.key = 'value'
		self.assertTrue('key' in d)
		self.assertEqual(d['key'],'value')
	def test_keyerror(self):
		d = Dict()
		with self.assertRaises(KeyError):
			value = d['empty']
	def test_attrerror(self):
		d = Dict()
		with self.assertRaises(AttributeError):
			value = d.empty
	# 可以在单元测试中编写两个特殊的setUp()和tearDown()方法。
	# 这两个方法会分别在每调用一个测试方法的前后分别被执行。
	def setUp(self):
		print('setUp...')
	def tearDown(self):
		print('tearDown...')

'''
编写单元测试时，我们需要编写一个测试类，从unittest.TestCase继承。

以test开头的方法就是测试方法，不以test开头的方法不被认为是测试方法，测试的时候不会被执行。

对每一类测试都需要编写一个test_xxx()方法。由于unittest.TestCase提供了很多内置的条件判断，我们只需要调用这些方法就可以断言输出是否是我们所期望的。最常用的断言就是assertEqual()：

self.assertEqual(abs(-1), 1) # 断言函数返回的结果与1相等

另一种重要的断言就是期待抛出指定类型的Error，比如通过d['empty']访问不存在的key时，断言会抛出KeyError：

with self.assertRaises(KeyError):
    value = d['empty']

而通过d.empty访问不存在的key时，我们期待抛出AttributeError：

with self.assertRaises(AttributeError):
    value = d.empty
'''
unittest.main()

