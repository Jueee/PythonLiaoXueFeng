'''
SMTP发送邮件

SMTP是发送邮件的协议，Python内置对SMTP的支持，可以发送纯文本邮件、HTML邮件以及带附件的邮件。
'''
'''
Python对SMTP支持有smtplib和email两个模块，email负责构造邮件，smtplib负责发送邮件。
'''
from email.mime.text import MIMEText

# 构造一个最简单的纯文本邮件：
# 第一个参数就是邮件正文
# 第二个参数是MIME的subtype，传入'plain'表示纯文本，最终的MIME就是'text/plain'
# 最后一定要用utf-8编码保证多语言兼容性。
msg = MIMEText('hello , send by Python...','plain','utf-8')

# 输入Email地址和口令:
from_addr = '921550356@qq.com'
password = 'balabala'

# 输入收件人地址:
to_addr = 'To:weiyq10580@hundsun.com'

# 输入SMTP服务器地址:
smtp_server = 'smtp.qq.com'

import smtplib
if __name__ != '__main__':
    server = smtplib.SMTP(smtp_server, 25)     # SMTP协议默认端口是25
    # 用set_debuglevel(1)就可以打印出和SMTP服务器交互的所有信息
    server.set_debuglevel(1)
    # login()方法用来登录SMTP服务器
    server.login(from_addr,password)
    # sendmail()方法就是发邮件
    # 由于可以一次发给多个人，所以传入一个list
    # 邮件正文是一个str，as_string()把MIMEText对象变成str。
    server.sendmail(from_addr,[to_addr],msg.as_string())
    server.quit()



'''
仔细观察，发现如下问题：
1、邮件没有主题；
2、收件人的名字没有显示为友好的名字，比如Mr Green <green@example.com>；
3、明明收到了邮件，却提示不在收件人中。

这是因为邮件主题、如何显示发件人、收件人等信息并不是通过SMTP协议发给MTA
而是包含在发给MTA的文本中的.

我们必须把From、To和Subject添加到MIMEText中，才是一封完整的邮件：
'''
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.mime.base import MIMEBase 
from email.mime.multipart import MIMEMultipart
from email.utils import parseaddr, formataddr
import smtplib

def _format_addr(s):
    name,addr = parseaddr(s)
    return formataddr((Header(name,'utf-8').encode(),addr))

msg = MIMEText('Hello,send by Python...','plain','utf-8')
msg['From'] = _format_addr('Python爱好者<%s>' %from_addr)
msg['To'] = _format_addr('管理员<%s>' % to_addr)
msg['Subject'] = Header('来自SMTP的问候....','utf-8').encode()


if __name__ != '__main__':
    server = smtplib.SMTP(smtp_server, 25)     # SMTP协议默认端口是25
    # 用set_debuglevel(1)就可以打印出和SMTP服务器交互的所有信息
    server.set_debuglevel(1)
    # login()方法用来登录SMTP服务器
    server.login(from_addr,password)
    # sendmail()方法就是发邮件
    # 由于可以一次发给多个人，所以传入一个list
    # 邮件正文是一个str，as_string()把MIMEText对象变成str。
    server.sendmail(from_addr,[to_addr],msg.as_string())
    server.quit()



'''
发送HTML邮件

在构造MIMEText对象时，把HTML字符串传进去，再把第二个参数由plain变为html就可以了：
'''
with open('samples/sina.html','rb') as f: 
    nine = f.read()

msg = MIMEText(nine,'html','utf-8')

if __name__ != '__main__':
    server = smtplib.SMTP(smtp_server, 25)     # SMTP协议默认端口是25
    # 用set_debuglevel(1)就可以打印出和SMTP服务器交互的所有信息
    server.set_debuglevel(1)
    # login()方法用来登录SMTP服务器
    server.login(from_addr,password)
    # sendmail()方法就是发邮件
    # 由于可以一次发给多个人，所以传入一个list
    # 邮件正文是一个str，as_string()把MIMEText对象变成str。
    server.sendmail(from_addr,[to_addr],msg.as_string())
    server.quit()



'''
发送附件

带附件的邮件可以看做包含若干部分的邮件：文本和各个附件本身.

所以，可以构造一个MIMEMultipart对象代表邮件本身，然后往里面加上一个MIMEText作为邮件正文，再继续往里面加上表示附件的MIMEBase对象即可：
'''
msg = MIMEMultipart()
msg['From'] = _format_addr('Python爱好者<%s>' %from_addr)
msg['To'] = _format_addr('管理员<%s>' % to_addr)
msg['Subject'] = Header('来自SMTP的问候....','utf-8').encode()

# 邮件正文是MIMEText:
msg.attach(MIMEText('send with file...','plain','utf-8'))

# 添加附件就是加上一个MIMEBase，从本地读取一个图片:
with open('samples/sample.png','rb') as f:
    # 设置附件的MIME和文件名，这里是png类型:
    mime = MIMEBase('image','png',filename='name-sample.png')
    # 加上必要的头信息:
    mime.add_header('Content-Disposition','attachment',filename='name-sample.png')
    mime.add_header('Content-ID','<0>')
    mime.add_header('X-Attachment-ID','0')
    # 把附件的内容读进来:
    mime.set_payload(f.read())
    # 用Base64编码:
    encoders.encode_base64(mime)
    # 添加到MIMEMultipart:
    msg.attach(mime)

if __name__ != '__main__':
    server = smtplib.SMTP(smtp_server, 25)     # SMTP协议默认端口是25
    # 用set_debuglevel(1)就可以打印出和SMTP服务器交互的所有信息
    server.set_debuglevel(1)
    # login()方法用来登录SMTP服务器
    server.login(from_addr,password)
    # sendmail()方法就是发邮件
    # 由于可以一次发给多个人，所以传入一个list
    # 邮件正文是一个str，as_string()把MIMEText对象变成str。
    server.sendmail(from_addr,[to_addr],msg.as_string())
    server.quit()


'''
发送图片

把一个图片嵌入到邮件正文中.
直接在HTML邮件中链接图片地址行不行？答案是，大部分邮件服务商都会自动屏蔽带有外链的图片，因为不知道这些链接是否指向恶意网站。

要把图片嵌入到邮件正文中，我们只需按照发送附件的方式，先把邮件作为附件添加进去，然后，在HTML中通过引用src="cid:0"就可以把附件作为图片嵌入了。
如果有多个图片，给它们依次编号，然后引用不同的cid:x即可。

把上面代码加入MIMEMultipart的MIMEText从plain改为html，然后在适当的位置引用图片：
'''
msg = MIMEMultipart()
msg['From'] = _format_addr('Python爱好者<%s>' %from_addr)
msg['To'] = _format_addr('管理员<%s>' % to_addr)
msg['Subject'] = Header('来自SMTP的问候....','utf-8').encode()

# 邮件正文是MIMEText:
msg.attach(MIMEText('<html><body><h1>hello</h1>'+'<p><img src="cid:0"></p>'+'</body></html>','html','utf-8'))

# 添加附件就是加上一个MIMEBase，从本地读取一个图片:
with open('samples/sample.png','rb') as f:
    # 设置附件的MIME和文件名，这里是png类型:
    mime = MIMEBase('image','png',filename='name-sample.png')
    # 加上必要的头信息:
    mime.add_header('Content-Disposition','attachment',filename='name-sample.png')
    mime.add_header('Content-ID','<0>')
    mime.add_header('X-Attachment-ID','0')
    # 把附件的内容读进来:
    mime.set_payload(f.read())
    # 用Base64编码:
    encoders.encode_base64(mime)
    # 添加到MIMEMultipart:
    msg.attach(mime)

if __name__ != '__main__':
    server = smtplib.SMTP(smtp_server, 25)     # SMTP协议默认端口是25
    # 用set_debuglevel(1)就可以打印出和SMTP服务器交互的所有信息
    server.set_debuglevel(1)
    # login()方法用来登录SMTP服务器
    server.login(from_addr,password)
    # sendmail()方法就是发邮件
    # 由于可以一次发给多个人，所以传入一个list
    # 邮件正文是一个str，as_string()把MIMEText对象变成str。
    server.sendmail(from_addr,[to_addr],msg.as_string())
    server.quit()


'''
同时支持HTML和Plain格式

如果我们发送HTML邮件，收件人通过浏览器或者Outlook之类的软件是可以正常浏览邮件内容的，但是，如果收件人使用的设备太古老，查看不了HTML邮件怎么办？

办法是在发送HTML的同时再附加一个纯文本，如果收件人无法查看HTML格式的邮件，就可以自动降级查看纯文本邮件。


利用MIMEMultipart就可以组合一个HTML和Plain，要注意指定subtype是alternative：
'''

msg = MIMEMultipart('alternative')
msg['From'] = _format_addr('Python爱好者<%s>' %from_addr)
msg['To'] = _format_addr('管理员<%s>' % to_addr)
msg['Subject'] = Header('来自SMTP的问候....','utf-8').encode()

msg.attach(MIMEText('hello','plain','utf-8'))
msg.attach(MIMEText('<html><body><h1>hello</h1></body></html>','html','utf-8'))


if __name__ != '__main__':
    server = smtplib.SMTP(smtp_server, 25)     # SMTP协议默认端口是25
    # 用set_debuglevel(1)就可以打印出和SMTP服务器交互的所有信息
    server.set_debuglevel(1)
    # login()方法用来登录SMTP服务器
    server.login(from_addr,password)
    # sendmail()方法就是发邮件
    # 由于可以一次发给多个人，所以传入一个list
    # 邮件正文是一个str，as_string()把MIMEText对象变成str。
    server.sendmail(from_addr,[to_addr],msg.as_string())
    server.quit()


'''
加密SMTP

使用标准的25端口连接SMTP服务器时，使用的是明文传输，发送邮件的整个过程可能会被窃听。

要更安全地发送邮件，可以加密SMTP会话，实际上就是先创建SSL安全连接，然后再使用SMTP协议发送邮件。
'''
'''
某些邮件服务商，例如Gmail，提供的SMTP服务必须要加密传输。我们来看看如何通过Gmail提供的安全SMTP发送邮件。

必须知道，Gmail的SMTP端口是587，因此，修改代码如下：

smtp_server = 'smtp.gmail.com'
smtp_port = 587
server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()
# 剩下的代码和前面的一模一样:
server.set_debuglevel(1)
...


只需要在创建SMTP对象后，立刻调用starttls()方法，就创建了安全连接。
'''
