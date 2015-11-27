# list是一种有序的集合，可以随时添加和删除其中的元素。

classmates = ['Mich', 'Bob', 'Tra']
print(classmates)

print(len(classmates))

print(classmates[0], classmates[len(classmates)-1])

# 如果要取最后一个元素，除了计算索引位置外，还可以用-1做索引，直接获取最后一个元素
print(classmates[-1])

# list是一个可变的有序表，所以，可以往list中追加元素到末尾
classmates.append('Adam')
print(classmates)

# 也可以把元素插入到指定的位置，比如索引号为1的位置：
classmates.insert(2, 'Jack')
print(classmates)

# 要删除list末尾的元素，用pop()方法
classmates.pop()
print(classmates)

# 要删除指定位置的元素，用pop(i)方法，其中i是索引位置
classmates.pop(1)
print(classmates)

# 要把某个元素替换成别的元素，可以直接赋值给对应的索引位置
classmates[1] = 'Jue'
print(classmates)

# list里面的元素的数据类型也可以不同
L = ['Apple', 123, True]
print(L)

# list元素也可以是另一个list
s= ['python', 'java', ['asp', 'php'], 'scheme']
print(len(s))

s[1] = L
print(s)






