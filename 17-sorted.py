# Python内置的sorted()函数就可以对list进行排序
print(sorted([123,22,323,41,5232]))


print(sorted([35,-23,-2323,322,-232]))
print(sorted([35,-23,-2323,322,-232], key = abs))

# 默认情况下，对字符串排序，是按照ASCII的大小比较的，由于'Z' < 'a'，结果，大写字母Z会排在小写字母a的前面。
print(sorted(['Bod','as','sf','afa','zoasd']))

print(sorted(['Bod','as','sf','afa','zoasd'], key = str.lower))

# 要进行反向排序，不必改动key函数，可以传入第三个参数reverse=True：
print(sorted(['Bod','as','sf','afa','zoasd'], key = str.lower, reverse = True))

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
	return t[0].lower()
def by_score(t):
	return t[1]
L2 = sorted(L, key = by_name)
print(L2)

L3 = sorted(L, key = by_score)
print(L3)