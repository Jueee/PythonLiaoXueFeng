'''
JSON

如果我们要在不同的编程语言之间传递对象，就必须把对象序列化为标准格式，比如XML，但更好的方法是序列化为JSON，因为JSON表示出来就是一个字符串，可以被所有语言读取，也可以方便地存储到磁盘或者通过网络传输。JSON不仅是标准格式，并且比XML更快，而且可以直接在Web页面中读取，非常方便。

'''

'''
JSON表示的对象就是标准的JavaScript语言的对象，JSON和Python内置的数据类型对应如下：

JSON类型	Python类型
{}			dict
[]			list
"string"	str
1234.56		int或float
true/false	True/False
null		None
'''


# 把Python对象变成一个JSON：
import json

d = dict(name='bob',age=20,score=88)
# dumps()方法返回一个str，内容就是标准的JSON。
print(json.dumps(d))


'''
要把JSON反序列化为Python对象，
1、用loads()：把JSON的字符串反序列化
2、对应的load()方法，从file-like Object中读取字符串并反序列化：
'''
json_str = '{"age": 20, "name": "bob", "score": 88}'
print(json.loads(json_str))




import json

class Student(object):
	def __init__(self, name, age, score):
		self.name = name
		self.age = age
		self.score = score

def student2dict(std):
	return{
		'name':std.name,
		'age':std.age,
		'score':std.score
	}

# 为Student专门写一个转换函数，再把函数传进去即可：
s = Student('Bob',20,88)
print(json.dumps(s, default=student2dict))


# 要把JSON反序列化为一个Student对象实例，loads()方法首先转换出一个dict对象，然后，我们传入的object_hook函数负责把dict转换为Student实例：

def dict2student(d):
	return Student(d['name'],d['age'],d['score'])

json_str='{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str,object_hook=dict2student))