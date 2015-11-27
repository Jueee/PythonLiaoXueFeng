
# 表示模块的文档注释，任何模块代码的第一个字符串都被视为模块的文档注释；
' a test module '

__author__ = 'Michael Liao'

import sys

def test():
	print(sys.argv)
	args = sys.argv
	if len(args)==1:
		print('Hello World')
	elif len(args)==2:
		print('Hello, %s !' % args[1])
	else:
		print('Too many arguments!')

if __name__ == '__main__':
	test()

	print(sys.path)