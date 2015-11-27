'''
tuple

另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改
'''
classmates = ('Min', 'Bob', 'Ana')

print(classmates[1])



# tuple的陷阱：当你定义一个tuple时，在定义的时候，tuple的元素就必须被确定下来
t = (1, 2)
print(t)

t= ()
print(t)

t = (1)
print(t, type(t))

# 只有1个元素的tuple定义时必须加一个逗号,，来消除歧义
t = (1,)

print(t)
print(len(t), type(t))

# Python在显示只有1个元素的tuple时，也会加一个逗号,，以免你误解成数学计算意义上的括号。

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
print(L[0][0])
print(L[1][1])
print(L[2][2])