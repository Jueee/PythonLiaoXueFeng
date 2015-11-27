'''
正则表达式
'''
'''
re模块
'''
s = 'ABC\\-001'
print(s)
# 使用Python的r前缀，就不用考虑转义的问题了
s = r'ABC\-001'
print(s)


'''
匹配
'''
# match()方法判断是否匹配，如果匹配成功，返回一个Match对象，否则返回None
import re
t = re.match(r'^\d{3}\-\d{3,8}$','010-12345')
print(t)
t = re.match(r'^\d{3}\-\d{3,8}$','010 12345')
print(t)

# 常见的判断方法就是：
test = '010-12345'
if re.match(r'^\d{3}\-\d{3,8}$',test):
	print('ok')
else:
	print('false')


'''
切分字符串
'''
print('a b   c'.split(' '))

print(re.split(r'\s+','a b   c'))

print(re.split(r'[\s\,]+','a,, , ,,b, c  d,  '))

print(re.split(r'[\s\,\;]','a,b;;;c,; ,; dda  '))

print(re.split(r'[\s\,]+', 'a,   b ,  c    d,,         ,'))

'''
分组
除了简单地判断是否匹配之外，正则表达式还有提取子串的强大功能。
用()表示的就是要提取的分组（Group）。
'''
m = re.match(r'^(\d{3})-(\d{3,8})$','010-1234523')
print(m)
print(m.group(0))
print(m.group(1))
print(m.group(2))



'''
贪婪匹配

最后需要特别指出的是，正则匹配默认是贪婪匹配，也就是匹配尽可能多的字符。
'''
print(re.match(r'^(\d+)(0*)$','102300').groups())

# 必须让\d+采用非贪婪匹配（也就是尽可能少匹配），才能把后面的0匹配出来
# 加个?就可以让\d+采用非贪婪匹配：
print(re.match(r'^(\d+?)(0*)$','102300').groups())



'''
编译

当我们在Python中使用正则表达式时，re模块内部会干两件事情：
1、编译正则表达式，如果正则表达式的字符串本身不合法，会报错；
2、用编译后的正则表达式去匹配字符串。

如果一个正则表达式要重复使用几千次，出于效率的考虑，我们可以预编译该正则表达式
接下来重复使用时就不需要编译这个步骤了，直接匹配：
'''
import re

re_telephone = re.compile(r'^(\d{3}-(\d{3,8}))$')
print(type(re_telephone))
print(re_telephone.match('010-12345').groups())
print(re_telephone.match('010-2345').groups())

