'''
base64

Base64是一种用64个字符来表示任意二进制数据的方法。

Python内置的base64可以直接进行base64的编解码：
'''
'''
如果要编码的二进制数据不是3的倍数，最后会剩下1个或2个字节，Base64用\x00字节在末尾补足后，再在编码的末尾加上1个或2个=号，表示补了多少字节，解码的时候，会自动去掉。
'''
import base64

e = base64.b64encode(b'binary\x00string')
print(e)

d = base64.b64decode(b'YmluYXJ5AHN0cmluZw===')
print(d)


# 由于标准的Base64编码后可能出现字符+和/，在URL中就不能直接作为参数
# 所以又有一种"url safe"的base64编码，其实就是把字符+和/分别变成-和_
e1 = base64.b64encode(b'i\xb7\x1d\xfb\xef\xff')
print(e1)

e2 = base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff')
print(e2)

e3 = base64.urlsafe_b64decode('abcd--__')
print(e3)


'''
Base64是一种通过查表的编码方法，不能用于加密，即使使用自定义的编码表也不行。

Base64适用于小段内容的编码，比如数字证书签名、Cookie的内容等。

由于=字符也可能出现在Base64编码中，但=用在URL、Cookie里面会造成歧义，所以，很多Base64编码后会把=去掉：

去掉=后怎么解码呢？因为Base64是把3个字节变为4个字节，所以，Base64编码的长度永远是4的倍数，因此，需要加上=把Base64字符串的长度变为4的倍数，就可以正常解码了。
'''
# 写一个能处理去掉=的base64解码函数：
import base64

def safe_base64_decode(s):
    if len(s)%4 != 0:
        print(len(s)%4)
        s = s + (4 - len(s)%4) * '='
    return base64.b64decode(s)

print(safe_base64_decode('YWJjZA='))