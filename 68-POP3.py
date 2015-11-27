'''
POP3

收取邮件就是编写一个MUA作为客户端，从MDA把邮件获取到用户的电脑或者手机上。
收取邮件最常用的协议是POP协议，目前版本号是3，俗称POP3。
'''
'''
Python内置一个poplib模块，实现了POP3协议，可以直接用来收邮件。

注意到POP3协议收取的不是一个已经可以阅读的邮件本身，而是邮件的原始文本，这和SMTP协议很像，SMTP发送的也是经过编码后的一大段文本。

要把POP3收取的文本变成可以阅读的邮件，还需要用email模块提供的各种类来解析原始文本，变成可阅读的邮件对象。

所以，收取邮件分两步：
第一步：用poplib把邮件的原始文本下载到本地；
第二步：用email解析原始文本，还原为邮件对象。
'''
'''
通过POP3下载邮件
'''
'''
POP3/SMTP服务客户端设置：
POP3服务器：pop.sina.cn
SMTP服务器：smtp.sina.cn

IMAP4服务/SMTP服务客户端设置：
IMAP服务器：imap.sina.cn
SMTP服务器：smtp.sina.cn
'''
import poplib
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr

# 输入邮件地址, 口令和POP3服务器地址:
email = '18767162147@sina.cn'
password = 'xinlang427299'
pop3_server = 'pop.sina.cn'

# 连接到POP3服务器:
server = poplib.POP3(pop3_server)
# 可以打开或关闭调试信息:
server.set_debuglevel(1)
# 可选:打印POP3服务器的欢迎文字:
print(server.getwelcome().decode('utf-8'))
print()

# 身份认证
server.user(email)
server.pass_(password)

# stat()返回邮件数量和占用空间:
print('Message:%s. Size:%s' % server.stat())

# list()返回所有邮件的编号:
resp,mails,octets = server.list()
# 可以查看返回的列表类似[b'1 82923', b'2 2184', ...]
print(mails)

# 获取最新一封邮件, 注意索引号从1开始:
index = len(mails)
resp,lines,octets = server.retr(index)

# lines存储了邮件的原始文本的每一行,
# 可以获得整个邮件的原始文本:
msg_content = b'\r\n'.join(lines).decode('utf-8')
# 稍后解析出邮件:
msg = Parser().parsestr(msg_content)
print('msg type:',type(msg))

# 可以根据邮件索引号直接从服务器删除邮件:
# server.dele(index)
# 关闭连接:
server.quit()


'''
解析邮件

解析邮件的过程和上一节构造邮件正好相反
'''
# 我们要递归地打印出Message对象的层次结构：

# indent用于缩进显示:
def print_info(msg, indent=0):
    if indent == 0:
        for header in ['From','To','Subject']:
            value = msg.get(header, '')
            if value:
                if header == 'Subject':
                    value = decode_str(value)
                else:
                    hdr, addr = parseaddr(value)
                    name = decode_str(hdr)
                    value = u'%s <%s>' % (name, addr)
            print('%s%s:%s' % ('    ' * indent, header, value))
    if (msg.is_multipart()):
        parts = msg.get_payload()
        for n, part in enumerate(parts):
            print('%s part %s' % ('    ' * indent,n))
            print('%s-----------------', ('    ' * indent))
            print_info(part, indent + 1)
    else:
        content_type = msg.get_content_type()
        if content_type == 'text/plain' or content_type == 'text/html':
            content = msg.get_payload(decode=True)
            charset = guess_charset(msg)
            if charset:
                content = content.decode(charset)
            print('%s Text:%s' % ('    ' * indent, content + '...'))
        else:
            print('%s Attachment:%s' % ('    ' * indent, content_type))


# 邮件的Subject或者Email中包含的名字都是经过编码后的str，要正常显示，就必须decode：
def decode_str(s):
    value, charset = decode_header(s)[0]
    if charset:
        value = value.decode(charset)
    return value    

# decode_header()返回一个list，因为像Cc、Bcc这样的字段可能包含多个邮件地址，所以解析出来的会有多个元素。
# 上面的代码我们偷了个懒，只取了第一个元素。
# 文本邮件的内容也是str，还需要检测编码，否则，非UTF-8编码的邮件都无法正常显示：
def guess_charset(msg):
    charset = msg.get_charset()
    if charset is None:
        content_type = msg.get('Content-Type','').lower()
        pos = content_type.find('charset=')
        if pos >= 0:
            charset = content_type[pos+8:].strip()
    return charset

if __name__ != '__main__':
    print(print_info(msg))




