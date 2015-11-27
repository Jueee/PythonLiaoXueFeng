'''
type()

动态语言和静态语言最大的不同，就是函数和类的定义，不是编译时定义的，而是运行时动态创建的。

'''
class Hello(object):
	def hello(self, name = 'world'):
		print('Hello， %s' % name)

h = Hello()
h.hello()

print(type(Hello))

print(type(h))

print('--------------------------')
'''
我们说class的定义是运行时动态创建的，而创建class的方法就是使用type()函数。

type()函数既可以返回一个对象的类型，又可以创建出新的类型
比如，我们可以通过type()函数创建出Hello类，而无需通过class Hello(object)...的定义：

要创建一个class对象，type()函数依次传入3个参数：
1、class的名称；
2、继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
3、class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。

通过type()函数创建的类和直接写class是完全一样的，因为Python解释器遇到class定义时，仅仅是扫描一下class定义的语法，然后调用type()函数创建出class。
'''
def fn(self,name = 'world'):
	print('Hello，%s' % name)

Hello = type('Hello',(object,),dict(hello = fn))
h = Hello()
h.hello()

print(type(Hello))

print(type(h))


'''
使用元类

阅读: 95912
type()

动态语言和静态语言最大的不同，就是函数和类的定义，不是编译时定义的，而是运行时动态创建的。

比方说我们要定义一个Hello的class，就写一个hello.py模块：

class Hello(object):
    def hello(self, name='world'):
        print('Hello, %s.' % name)
当Python解释器载入hello模块时，就会依次执行该模块的所有语句，执行结果就是动态创建出一个Hello的class对象，测试如下：

>>> from hello import Hello
>>> h = Hello()
>>> h.hello()
Hello, world.
>>> print(type(Hello))
<class 'type'>
>>> print(type(h))
<class 'hello.Hello'>
type()函数可以查看一个类型或变量的类型，Hello是一个class，它的类型就是type，而h是一个实例，它的类型就是class Hello。

我们说class的定义是运行时动态创建的，而创建class的方法就是使用type()函数。

type()函数既可以返回一个对象的类型，又可以创建出新的类型，比如，我们可以通过type()函数创建出Hello类，而无需通过class Hello(object)...的定义：

>>> def fn(self, name='world'): # 先定义函数
...     print('Hello, %s.' % name)
...
>>> Hello = type('Hello', (object,), dict(hello=fn)) # 创建Hello class
>>> h = Hello()
>>> h.hello()
Hello, world.
>>> print(type(Hello))
<class 'type'>
>>> print(type(h))
<class '__main__.Hello'>
要创建一个class对象，type()函数依次传入3个参数：

class的名称；
继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。
通过type()函数创建的类和直接写class是完全一样的，因为Python解释器遇到class定义时，仅仅是扫描一下class定义的语法，然后调用type()函数创建出class。

正常情况下，我们都用class Xxx...来定义类，但是，type()函数也允许我们动态创建出类来，也就是说，动态语言本身支持运行期动态创建类，这和静态语言有非常大的不同，要在静态语言运行期创建类，必须构造源代码字符串再调用编译器，或者借助一些工具生成字节码实现，本质上都是动态编译，会非常复杂。

metaclass

除了使用type()动态创建类以外，要控制类的创建行为，还可以使用metaclass。

metaclass，直译为元类，简单的解释就是：

当我们定义了类以后，就可以根据这个类创建出实例，所以：先定义类，然后创建实例。

但是如果我们想创建出类呢？那就必须根据metaclass创建出类，所以：先定义metaclass，然后创建类。

连接起来就是：先定义metaclass，就可以创建类，最后创建实例。


__new__()方法接收到的参数依次是：
1、当前准备创建的类的对象；
2、类的名字；
3、类继承的父类集合；
4、类的方法集合。
'''
# metaclass是类的模板，所以必须从`type`类型派生：
class ListMetaclass(type):
	"""docstring for ListMetaclass"""
	def __new__(cls,name,bases,attrs):
		attrs['add'] = lambda self,value : self.append(value)
		return type.__new__(cls,name,bases,attrs)

# 有了ListMetaclass，我们在定义类的时候还要指示使用ListMetaclass来定制类，传入关键字参数metaclass：
class MyList(list, metaclass = ListMetaclass):
	pass
		
L = MyList()
L.add(1)
print(L)





'''
ORM全称“Object Relational Mapping”，即对象-关系映射，就是把关系数据库的一行映射为一个对象，也就是一个类对应一个表，这样，写代码更简单，不用直接操作SQL语句。

要编写一个ORM框架，所有的类都只能动态定义，因为只有使用者才能根据表的结构定义出对应的类来。

让我们来尝试编写一个ORM框架。
'''
class Field(object):
	def __init__(self, name, column_type):
		self.name = name
		self.column_type = column_type
	def __str__(self):
		return '<%s:%s>' % (self.__class__.__name__, self.name)

class StringField(Field):
	def __init__(self, name):
		super(StringField, self).__init__(name,'varchar(100)')

class IntegerField(Field):
	def __init__(self, name):
		super(IntegerField, self).__init__(name,'bigint')
'''
在ModelMetaclass中，一共做了几件事情：
1、排除掉对Model类的修改；
2、在当前类（比如User）中查找定义的类的所有属性，如果找到一个Field属性，就把它保存到一个__mappings__的dict中，同时从类属性中删除该Field属性，否则，容易造成运行时错误（实例的属性会遮盖类的同名属性）；
3、把表名保存到__table__中，这里简化为表名默认为类名。
'''
class ModelMetaclass(type):
	def __new__(cls,name,bases,attrs):
		if name == 'Model':
			return type.__new__(cls,name,bases,attrs)
		print('Found model:%s' % name)
		mappings = dict()
		for k,v in attrs.items():
			if isinstance(v,Field):
				print('Found mappings:%s ==> %s' % (k,v))
				mappings[k] = v
		for k in mappings.keys():
			attrs.pop(k)
		attrs['__mappings__'] = mappings
		attrs['__table__'] = name
		return type.__new__(cls,name,bases,attrs)
# 在Model类中，就可以定义各种操作数据库的方法，比如save()，delete()，find()，update等等。
class Model(dict,metaclass=ModelMetaclass):
	def __init__(self, **kw):
		super(Model, self).__init__(**kw)
	def __getattr__(self,key):
		try:
			return self[key]
		except KeyError:
			raise AttributeError(r"'Model' object has no attribute '%s'" % key)
	def __setattr__(self,key,value):
		self[key] = value
	def save(self):
		fields = []
		params = []
		args = []
		for k,v in self.__mappings__.items():
			fields.append(v.name)
			params.append('?')
			args.append(getattr(self,k,None))
		sql = 'indert into %s (%s) values (%s)' % (self.__table__,','.join(fields),','.join(params))
		print('SQL:%s' % sql)
		print('ARGS:%s'% str(args))
		
class User(Model):
	# 定义类的属性到列的映射：
	id = IntegerField('id')
	name = StringField('username')
	email = StringField('email')
	password = StringField('password')

u = User(id=12345,name='Michael',email='weiyq10580@hundsun.com',password='my-pwd')
u.save()
		









