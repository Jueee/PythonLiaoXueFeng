'''
通过列表生成式，我们可以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限的。而且，创建一个包含100万个元素的列表，不仅占用很大的存储空间，如果我们仅仅需要访问前面几个元素，那后面绝大多数元素占用的空间都白白浪费了。

所以，如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？这样就不必创建完整的list，从而节省大量的空间。在Python中，这种一边循环一边计算的机制，称为生成器：generator。

'''

'''
要创建一个generator，有很多种方法。

第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator：
创建L和g的区别仅在于最外层的[]和()，L是一个list，而g是一个generator。
'''
L = [x * x for x in range(10)]
print(L)
g = (x * x for x in range(10))
print(g,type(g))
# 如果要一个一个打印出来，可以通过next()函数获得generator的下一个返回值
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print('----')

g = (x * x for x in range(10))
for n in g:
	print(n)
print('====================')

def fib(max):
	n,a,b = 0,0,1
	while n < max:
		print(b)
		a,b = b, a+b
		n= n+1
	return 'done'
fib(10)
'''
generator和函数的执行流程不一样。

函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。

用for循环调用generator时，发现拿不到generator的return语句的返回值。如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中
g = fib(6)
>>> while True:
...     try:
...         x = next(g)
...         print('g:', x)
...     except StopIteration as e:
...         print('Generator return value:', e.value)
...         break

'''
print('===========================')
def fib2(max):
	n,a,b = 0,0,1
	while n < max:
		yield b
		a,b = b, a+b
		n= n+1
	return 'done'
for n in fib2(10):
	print(n)



def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield(3)
    print('step 3')
    yield(5)

o = odd()
next(o)
next(o)
next(o)