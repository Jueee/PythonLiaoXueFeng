'''
struct

struct模块来解决bytes和其他二进制数据类型的转换。
'''
'''
# struct的pack函数把任意数据类型变成bytes：

pack的第一个参数是处理指令，'>I'的意思是：
>表示字节顺序是big-endian，也就是网络序，I表示4字节无符号整数。
后面的参数个数要和处理指令一致。
'''
import struct

print(struct.pack('>I', 10240099))




'''
unpack把bytes变成相应的数据类型

根据>IH的说明，后面的bytes依次变为I：4字节无符号整数和H：2字节无符号整数。
'''
import struct

print(struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80'))


'''
struct模块定义的数据类型可以参考Python官方文档：
https://docs.python.org/3/library/struct.html#format-characters


Format  C Type              Python type     Standard size   Notes
x       pad                 byte            no value         
c       char                bytes of length 1   1    
b       signed char         integer         1   (1),(3)
B       unsigned char       integer       1   (3)
?       _Bool               bool        1   (1)
h       short               integer     2   (3)
H       unsigned short      integer 2   (3)
i       int                 integer 4   (3)
I       unsigned int        integer 4   (3)
l       long                integer 4   (3)
L       unsigned long       integer 4   (3)
q       long long           integer 8   (2), (3)
Q       unsigned long long  integer 8   (2), (3)
n       ssize_t             integer     (4)
N       size_t              integer     (4)
f       float               float   4   (5)
d       double              float   8   (5)
s       char[]              bytes        
p       char[]              bytes        
P       void *              integer     (6)


'''

'''
Windows的位图文件（.bmp）是一种非常简单的文件格式，我们来用struct分析一下


BMP格式采用小端方式存储数据，文件头的结构按顺序如下：

两个字节：'BM'表示Windows位图，'BA'表示OS/2位图；
一个4字节整数：表示位图大小；
一个4字节整数：保留位，始终为0；
一个4字节整数：实际图像的偏移量；
一个4字节整数：Header的字节数；
一个4字节整数：图像宽度；
一个4字节整数：图像高度；
一个2字节整数：始终为1；
一个2字节整数：颜色数。

'''
import os.path

# 找一个bmp文件，读入前30个字节来分析：
with open('samples/sample.bmp','rb') as f:
    s = f.read(30)
    print(s)
    t = struct.unpack('<ccIIIIIIHH',s)
    print(t)

def isBMP(file):
    if not isinstance(file,str):
        print('Not BMP')
        return
    if os.path.splitext(file)[1] != '.bmp':
        print('Not BMP')
        return
    try:
        with open(file,'rb') as f:
            s = f.read(30)
            t = struct.unpack('<ccIIIIIIHH',s)
            print('图片大小：',t[6],'*',t[7], '颜色数',t[9])
    except Exception as e:
        print('wrong path!')
    

isBMP('samples/sample.bmp')

