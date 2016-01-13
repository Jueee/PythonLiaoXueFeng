c = [
    '决',
    '决决',
    '决决决',
    '决决决决',
    '决决决决决',
    '决决决决决决',
    '决决决决决决决'
]
print('----正常字符串格式化：----')
for x in range(len(c)):
    print('|%20s|' % c[x])
'''
执行结果：
----正常字符串格式化：----
|                   决|
|                  决决|
|                 决决决|
|                决决决决|
|               决决决决决|
|              决决决决决决|
|             决决决决决决决|
'''

print()
print()
print()

def chinese(data):
    count = 0
    for s in data:
        if ord(s) > 127:
            count += 1
    return count

print('----通过函数计算长度格式化：----')
for x in range(len(c)):
    number = chinese(c[x])
    newStr = '{0:{wd}}'.format(c[x],wd=20-number)
    print('|%s|' % newStr)


'''
----通过函数计算长度格式化：----
|决                  |
|决决                |
|决决决              |
|决决决决            |
|决决决决决          |
|决决决决决决        |
|决决决决决决决      |
'''