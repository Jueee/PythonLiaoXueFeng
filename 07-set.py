'''
set

set和dict类似，也是一组key的集合，但不存储value。
由于key不能重复，所以，在set中，没有重复的key。
'''

# 要创建一个set，需要提供一个list作为输入集合
s = set([1, 2, 3])
print(s)
print(type(s))

# 重复元素在set中自动被过滤
s = set([3, 23, 233, 12, 23, 3])
print(s)


# 通过add(key)方法可以添加元素到set中，可以重复添加，但不会有效果
s.add(4)
print(s)
s.add(4)
print(s)


# 通过remove(key)方法可以删除元素
s.remove(3)
print(s)



# set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作
s1 = set([1,2,3])
s2 = set([2,3,4])
print(s1 & s2)
print(s1 | s2)










