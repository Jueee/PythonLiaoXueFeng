def foo():
	r = some_function()
	if r==(-1):
		return (-1)
	return r

def bar():
	r = foo()
	if r==(-1):
		print('Error')
	else:
		pass

try:
	print('try...')
	r = 10/0
	print('result:',r)
except ZeroDivisionError as e:
	print('except:',e)
finally:
	print('finally...')
print('End')


'''
当我们认为某些代码可能会出错时，就可以用try来运行这段代码，如果执行出错，则后续代码不会继续执行，而是直接跳转至错误处理代码，即except语句块，执行完except后，如果有finally语句块，则执行finally语句块，至此，执行完毕。
'''


try:
	print('try...')
	r = 10/int('a')
	print('result:',r)
except ValueError as e:
	print('ValueError:',e)
except ZeroDivisionError as e:
	print('ZeroDivisionError:',e)
finally:
	print('finally...')
print('End')


# 如果没有错误发生，可以在except语句块后面加一个else，当没有错误发生时，会自动执行else语句：

try:
	print('try...')
	r = 10/int('2')
	print('result:',r)
except ValueError as e:
	print('ValueError:',e)
except ZeroDivisionError as e:
	print('ZeroDivisionError:',e)
else:
	print('no error!')
finally:
	print('finally...')
print('End')


'''
Python所有的错误都是从BaseException类派生的，常见的错误类型和继承关系看这里：

BaseException
 +-- SystemExit
 +-- KeyboardInterrupt
 +-- GeneratorExit
 +-- Exception
      +-- StopIteration
      +-- StopAsyncIteration
      +-- ArithmeticError
      |    +-- FloatingPointError
      |    +-- OverflowError
      |    +-- ZeroDivisionError
      +-- AssertionError
      +-- AttributeError
      +-- BufferError
      +-- EOFError
      +-- ImportError
      +-- LookupError
      |    +-- IndexError
      |    +-- KeyError
      +-- MemoryError
      +-- NameError
      |    +-- UnboundLocalError
      +-- OSError
      |    +-- BlockingIOError
      |    +-- ChildProcessError
      |    +-- ConnectionError
      |    |    +-- BrokenPipeError
      |    |    +-- ConnectionAbortedError
      |    |    +-- ConnectionRefusedError
      |    |    +-- ConnectionResetError
      |    +-- FileExistsError
      |    +-- FileNotFoundError
      |    +-- InterruptedError
      |    +-- IsADirectoryError
      |    +-- NotADirectoryError
      |    +-- PermissionError
      |    +-- ProcessLookupError
      |    +-- TimeoutError
      +-- ReferenceError
      +-- RuntimeError
      |    +-- NotImplementedError
      |    +-- RecursionError
      +-- SyntaxError
      |    +-- IndentationError
      |         +-- TabError
      +-- SystemError
      +-- TypeError
      +-- ValueError
      |    +-- UnicodeError
      |         +-- UnicodeDecodeError
      |         +-- UnicodeEncodeError
      |         +-- UnicodeTranslateError
      +-- Warning
           +-- DeprecationWarning
           +-- PendingDeprecationWarning
           +-- RuntimeWarning
           +-- SyntaxWarning
           +-- UserWarning
           +-- FutureWarning
           +-- ImportWarning
           +-- UnicodeWarning
           +-- BytesWarning
           +-- ResourceWarning
'''
print('=======================')
'''
使用try...except捕获错误还有一个巨大的好处，就是可以跨越多层调用，比如函数main()调用foo()，foo()调用bar()，结果bar()出错了，这时，只要main()捕获到了，就可以处理：
'''
def foo(s):
	return 10/int(s)
def bar(s):
	return foo(s) * 2
def main():
	try:
		bar('0')
	except Exception as e:
		print('Error:',e)
	finally:
		print('finally...')
main()

'''
def main():
	bar('0')
main()

记录错误

如果不捕获错误，自然可以让Python解释器来打印出错误堆栈，但程序也被结束了。
既然我们能捕获错误，就可以把错误堆栈打印出来，然后分析错误原因，同时，让程序继续执行下去。

Python内置的logging模块可以非常容易地记录错误信息：
通过配置，logging还可以把错误记录到日志文件里，方便事后排查。
'''
import logging

def foo(s):
	return 10/int(s)
def bar(s):
	return foo(s) * 2
def main():
	try:
		bar('0')
	except Exception as e:
		logging.exception(e)
main()

print()
print('-----')



'''
抛出错误

因为错误是class，捕获一个错误就是捕获到该class的一个实例。
因此，错误并不是凭空产生的，而是有意创建并抛出的。Python的内置函数会抛出很多类型的错误，我们自己编写的函数也可以抛出错误。

如果要抛出错误，首先根据需要，可以定义一个错误的class，选择好继承关系，然后，用raise语句抛出一个错误的实例：
'''
class FooError(ValueError):
	pass

def foo(s):
	n = int(s)
	if n==0:
		raise FooError('invalid value:%s' % s)
	return 10/s

foo('0')
		


