'''

'''
# int()函数可以把字符串转换为整数，当仅传入字符串时，int()函数默认按十进制转换：
print(int('12'))

# 但int()函数还提供额外的base参数，默认值为10。如果传入base参数，就可以做N进制的转换：
print(int('12345', base = 8))
print(int('12345', base = 16))

# 假设要转换大量的二进制字符串，每次都传入int(x, base=2)非常麻烦，于是，我们想到，可以定义一个int2()的函数，默认把base=2传进去：
def int2(x, base = 2):
	return int(x, base)

print(int2('10000'))
print(int2('10101001'))



# functools.partial就是帮助我们创建一个偏函数的，不需要我们自己定义int2()，可以直接使用下面的代码创建一个新的函数int2：
import functools

int3 = functools.partial(int, base = 3)
print(int3('102102'))

'''
functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单。
'''


kw = {'base':5}
print(int('1021234', **kw))