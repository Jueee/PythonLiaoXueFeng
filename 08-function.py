print(abs(0))

print(max(1,4,5,6))


print(int('2322'))
print(int(13.23))
print(int(float('13.98')))
print(float('23.24'))

print(str(121))
print(bool(1))
print(bool(0))
print(bool(-1))
print(bool(''))


# 函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量
# 相当于给这个函数起了一个“别名”
a = abs        # 变量a指向abs函数
print(a(-1))   # 所以也可以通过a调用abs函数


n1 = 255
n2 = 1000
print(hex(n1))
print(hex(n2))


'''
在Python中，定义一个函数要使用def语句，依次写出函数名、括号、括号中的参数和冒号:，然后，在缩进块中编写函数体，函数的返回值用return语句返回。
'''
def my_abs(x):
	# 数据类型检查可以用内置函数isinstance()实现
	if not isinstance(x, (int, float)):
		raise TypeError('bad operand type')
	if x >= 0:
		return x
	else:
		return -x

print(my_abs(-9.7))





import math

def move(x, y, step, angle = 0):
	nx = x + step * math.cos(angle)
	ny = y - step * math.sin(angle)
	return nx, ny

x, y = move(100,100,60,math.pi/6)
print(x,y)
# 原来返回值是一个tuple
r = move(100,100,60,math.pi/6)
print(r)
print(r[0],r[1])


def quadratic(a,b,c):
	B = (b * b - 4 * a * c)
	if B >= 0:
		ans1 = (-1 * b + math.sqrt(B)) / (2 * a) 
		ans2 = (-1 * b - math.sqrt(B)) / (2 * a) 
	return ans1,ans2

print(quadratic(2,3,1))
print(quadratic(1,3,-4))


def power(x,n=2):
	s = 1
	while n > 0:
		n = n - 1
		s = s * x
	return s

print(power(5))
print(power(15))
print(power(5,4))


def add_end(L=[]):
	L.append('END')
	return L

print(add_end([1,2,3]))

print(add_end())
print(add_end())
print(add_end())

def addend(L=None):
	if L is None:
		L = []
	L.append('END')
	return L

print(addend())
print(addend())
print(addend())


def calc(numbers):
	sum = 0
	for n in numbers:
		sum = sum + n * n
	return sum
print(calc([1,2,3,4,5]))

def calc2(* numbers):
	sum = 0
	for n in numbers:
		sum = sum + n * n
	return sum
print(calc2(12,32,32,42))
nums = [1,2,3]
print(calc2(nums[0],nums[1],nums[2]))
print(calc2(*nums))



def person(name,age,**kw):
	if 'city' in kw:
		print('has city', '==',end = '')
	if 'job' in kw:
		print('has job', '==',end = '')
	print('name:',name,'age:',age,'other:',kw)

person('Min',30)
person('Bob',35,city='Beijing')
person('Bob',35,city='Beijing',job='Ern')

extra = {'city':'Beijing','job':'Eng'}
person('Jack',24,**extra)


def fact(n):
	if n == 1:
		return 1
	return n * fact(n-1)

print(fact(5))
print(fact(100))
print(fact(100))

# 解决递归调用栈溢出的方法是通过尾递归优化，事实上尾递归和循环的效果是一样的，所以，把循环看成是一种特殊的尾递归函数也是可以的。
# 尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。
# 这样，编译器或者解释器就可以把尾递归做优化，使递归本身无论调用多少次，都只占用一个栈帧，不会出现栈溢出的情况。
def fec(n):
	return fac_iter(n,1)

def fac_iter(num,product):
	if num==1:
		return product
	return fac_iter(num-1,num*product)

print(fact(6))

def move(n,a,b,c):
	if n==1:
		print(a,'-->', c)
	else:
		move(n-1,a,c,b)		#move the n-1 from a to b
		move(1,a,b,c)       #now,a has just one dish,so just move it to c
		move(n-1,b,a,c)     #now,move the n-1 dishes from b to c

move(4,'A','B','C')
