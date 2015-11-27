'''
使用枚举类

'''
'''
当我们需要定义常量时，一个办法是用大写变量通过整数来定义，例如月份：

JAN = 1
FEB = 2
MAR = 3
...
NOV = 11
DEC = 12
好处是简单，缺点是类型是int，并且仍然是变量。

更好的方法是为这样的枚举类型定义一个class类型，然后，每个常量都是class的一个唯一实例。Python提供了Enum类来实现这个功能：
'''
from enum import Enum

Month = Enum('Month',('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

# value属性则是自动赋给成员的int常量，默认从1开始计数。
for name, member in Month.__members__.items():
	print(name,'=>',member,',',member.value)


# 如果需要更精确地控制枚举类型，可以从Enum派生出自定义类：
from enum import Enum,unique
# @unique装饰器可以帮助我们检查保证没有重复值。
@unique
class Weekday(Enum):
	Sun = 0
	Mon = 1
	Tue = 2
	Wed = 3
	Thu = 4
	Fri = 5
	Sat = 6
# 既可以用成员名称引用枚举常量，又可以直接根据value的值获得枚举常量。
day1 = Weekday.Mon
print(day1)

print(Weekday.Tue)

print(Weekday['Thu'])

print(Weekday.Thu.value)

print(day1 == Weekday.Mon)

print(day1 == Weekday.Thu)

print(Weekday(1))

print(day1 == Weekday(1))

for name, member in Weekday.__members__.items():
	print(name,'=>',member,',',member.value)

