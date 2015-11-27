'''
urllib

urllib提供了一系列用于操作URL的功能。

urllib提供的功能就是利用程序去执行各种HTTP请求。如果要模拟浏览器完成特定功能，需要把请求伪装成浏览器。伪装的方法是先监控浏览器发出的请求，再根据浏览器的请求头来伪装，User-Agent头就是用来标识浏览器的。
'''

'''
Get

urllib的request模块可以非常方便地抓取URL内容，也就是发送一个GET请求到指定的页面，然后返回HTTP的响应：
'''
'''
# 对网页进行抓取，并返回响应：
from urllib import request

url = 'https://api.douban.com/v2/book/2129650'
with request.urlopen(url) as f:
    data = f.read()
    print('Status:', f.status,f.reason)
    for k,v in f.getheaders():
        print('%s:%s' % (k,v))
    print(data.decode('utf-8'))
'''







print('----模拟浏览器发送GET请求----')
'''
如果我们要想模拟浏览器发送GET请求，就需要使用Request对象.
通过往Request对象添加HTTP头，我们就可以把请求伪装成浏览器。

例如，模拟iPhone 6去请求豆瓣首页：
'''
from urllib import request
'''
url = 'http://www.douban.com/'
req = request.Request(url)
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')

with request.urlopen(req) as f:
    print('status:',f.status,f.reason)
    for k,v in f.getheaders():
        print('%s:%s' % (k,v))
    print(f.read().decode('utf-8'))
'''



print('----以POST发送一个请求----')
'''
Post

如果要以POST发送一个请求，只需要把参数data以bytes形式传入。
'''
# 我们模拟一个微博登录，先读取登录的邮箱和口令，然后按照weibo.cn的登录页的格式以username=xxx&password=xxx的编码传入：
from urllib import request,parse

print('Login to weibo.cn...')
email = '18767162147'
passwd = '123456'

login_data = parse.urlencode([
    ('username',email),
    ('password',passwd),
    ('entry','mweibo'),
    ('client_id',''),
    ('savestate','1'),
    ('ec',''),
    ('pagerefer','https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
])

req = request.Request('https://passport.weibo.cn/sso/login')
req.add_header('Origin', 'https://passport.weibo.cn')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
req.add_header('Referer', 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')

with request.urlopen(req, data=login_data.encode('utf-8')) as f:
    print('Status:',f.status,f.reason)
    for k,v in f.getheaders():
        print('%s:%s' % (k,v))
    print('Data:',f.read().decode('utf-8'))

'''
Login to weibo.cn...
Status: 200 OK
Server:nginx/1.2.0
Date:Wed, 18 Nov 2015 01:17:48 GMT
Content-Type:text/html
Transfer-Encoding:chunked
Connection:close
Vary:Accept-Encoding
Cache-Control:no-cache, must-revalidate
Expires:Sat, 26 Jul 1997 05:00:00 GMT
Pragma:no-cache
Access-Control-Allow-Origin:https://passport.weibo.cn
Access-Control-Allow-Credentials:true
DPOOL_HEADER:dryad45
SINA-LB:aGEuOTAuZzEucXhnLmxiLnNpbmFub2RlLmNvbQ==
SINA-TS:ZGNjYTk0Y2UgMCAwIDAgNCA0ODAK
登录成功：
Data: {"retcode":20000000,"msg":"","data":{"loginresulturl":"https:\/\/passport.weibo.com\/sso\/crossdomain?entry=mweibo&action=login&proj=1&ticket=ST-MTk1NTAzMjcxNw%3D%3D-1447809422-gz-2C1D9275A244AFBEC6C3994B7615CBE0&display=0&cdurl=https%3A%2F%2Flogin.sina.com.cn%2Fsso%2Fcrossdomain%3Fentry%3Dmweibo%26action%3Dlogin%26proj%3D1%26ticket%3DST-MTk1NTAzMjcxNw%253D%253D-1447809422-gz-FE1989D8F7BC5227D9D27A1379670EF5%26display%3D0%26cdurl%3Dhttps%253A%252F%252Fpassport.sina.cn%252Fsso%252Fcrossdomain%253Fentry%253Dmweibo%2526action%253Dlogin%2526display%253D0%2526ticket%253DST-MTk1NTAzMjcxNw%25253D%25253D-1447809422-gz-057CDD10C8F2E7EB8E9797ADB86B4477","uid":"1955032717"}}
登录失败：
Data: {"retcode":50011002,"msg":"\u7528\u6237\u540d\u6216\u5bc6\u7801\u9519\u8bef","data":{"im":1,"username":"18767162147","errline":604}}
'''


'''
Handler

如果还需要更复杂的控制，比如通过一个Proxy(代理服务器)去访问网站，我们需要利用ProxyHandler来处理
'''
import urllib.request

proxy_handler = urllib.request.ProxyHandler({'http':'http://www.example.com:3128/'})
proxy_auth_handler = urllib.request.ProxyBasicAuthHandler()
proxy_auth_handler.add_password('realm','host','username','password')
opener = urllib.request.build_opener(proxy_handler,proxy_auth_handler)
with opener.open('http://www.example.com/login.html') as f:
    pass






