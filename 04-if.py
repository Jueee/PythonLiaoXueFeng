'''
条件判断

计算机之所以能做很多自动化的任务，因为它可以自己做条件判断。
'''
age = 2
if age >= 18:
	print('your age is', age)
	print('adult')
elif age >= 6:
	print('teenager')
else:
	print('your age is', age)
	print('kid')