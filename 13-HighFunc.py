'''
高阶函数英文叫Higher-order function。
'''

'''
变量可以指向函数

以Python内置的求绝对值的函数abs()为例，调用该函数用以下代码
'''
print(abs(-10))
print(abs)

f = abs
print(f(-10))




'''
既然变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数。

x = -5
y = 6
f = abs
f(x) + f(y) ==> abs(-5) + abs(6) ==> 11
return 11
'''
def add(x,y,f):
	return f(x)+f(y)

print(add(-5,6,abs))