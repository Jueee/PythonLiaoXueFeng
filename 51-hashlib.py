'''
hashlib

摘要算法简介
Python的hashlib提供了常见的摘要算法，如MD5，SHA1等等。

摘要算法又称哈希算法、散列算法。它通过一个函数，把任意长度的数据转换为一个长度固定的数据串（通常用16进制的字符串表示）。

摘要算法就是通过摘要函数f()对任意长度的数据data计算出固定长度的摘要digest，目的是为了发现原始数据是否被人篡改过。

摘要算法之所以能指出数据是否被篡改过，就是因为摘要函数是一个单向函数，计算f(data)很容易，但通过digest反推data却非常困难。
而且，对原始数据做一个bit的修改，都会导致计算出的摘要完全不同。
'''

# 计算出一个字符串的MD5值
# MD5是最常见的摘要算法，速度很快，生成结果是固定的128 bit字节，通常用一个32位的16进制字符串表示。
import hashlib

md5 = hashlib.md5()
md5.update('jue'.encode('utf-8'))
print(md5.hexdigest())

# 如果数据量很大，可以分块多次调用update()，最后计算的结果是一样的：
m = hashlib.md5()
m.update('j'.encode('utf-8'))
m.update('u'.encode('utf-8'))
m.update('e'.encode('utf-8'))
print(m.hexdigest())



# 另一种常见的摘要算法是SHA1，调用SHA1和调用MD5完全类似：
# SHA1的结果是160 bit字节，通常用一个40位的16进制字符串表示。
import hashlib

s = hashlib.sha1()
s.update('jue'.encode('utf-8'))
print(s.hexdigest())




def calc_md5(password):
    md5 = hashlib.md5()
    md5.update(password.encode('utf-8'))
    return md5.hexdigest()

db = {
    'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9'
}
def login(user,password):
    try:
        return db[user] == calc_md5(password)
    except KeyError as e:
        return '没有该用户'
    

print(login('michael','123456'))
print(login('bob','abc999'))
print(login('alice','alice2008'))
print(login('michael','23'))
print(login('bob','abc23999'))
print(login('alice','alic34e2008'))
print(login('alsdice','alice2008'))