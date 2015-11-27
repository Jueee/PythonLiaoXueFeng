'''
WSGI接口

一个Web应用的本质就是：
1、浏览器发送一个HTTP请求；
2、服务器收到请求，生成一个HTML文档；
3、服务器把HTML文档作为HTTP响应的Body发送给浏览器；
4、浏览器收到HTTP响应，从HTTP Body取出HTML文档并显示。

所以，最简单的Web应用就是先把HTML用文件保存好，用一个现成的HTTP服务器软件，接收用户请求，从文件中读取HTML，返回。
'''
'''
需要一个统一的接口，让我们专心用Python编写Web业务。
这个接口就是WSGI：Web Server Gateway Interface。

WSGI接口定义非常简单，它只要求Web开发者实现一个函数，就可以响应HTTP请求。

无论多么复杂的Web应用程序，入口都是一个WSGI处理函数。
HTTP请求的所有输入信息都可以通过environ获得，HTTP响应的输出都可以通过start_response()加上函数返回值作为Body。
'''
'''
符合WSGI标准的一个HTTP处理函数，它接收两个参数：
1、environ：一个包含所有HTTP请求信息的dict对象.
2、start_response：一个发送HTTP响应的函数.

在application()函数中，调用：
start_response('200 OK', [('Content-Type', 'text/html')])
就发送了HTTP响应的Header，注意Header只能发送一次，也就是只能调用一次start_response()函数。

start_response()函数接收两个参数，一个是HTTP响应码，一个是一组list表示的HTTP Header，每个Header用一个包含两个str的tuple表示。
'''
def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b'<h1>Hello World!</h1>']


'''
Python内置了一个WSGI服务器，这个模块叫wsgiref，它是用纯Python编写的WSGI服务器的参考实现。
所谓“参考实现”是指该实现完全符合WSGI标准，但是不考虑任何运行效率，仅供开发和测试使用。
'''
# 从wsgiref模块导入:
from wsgiref.simple_server import make_server

if __name__!='__main__':
    # 创建一个服务器，IP地址为空，端口是8000，处理函数是application:
    httpd = make_server('',8000,application)
    print('Serving HTTP on port 8000...')
    httpd.serve_forever()

'''
启动成功后，打开浏览器，输入http://localhost:8000/，就可以看到结果了.
'''





'''
稍微改造一下，从environ里读取PATH_INFO，这样可以显示更加动态的内容：
'''
def application2(environ,start_response):
    start_response('200 OK',[('Content-Type','text/html')])
    body = '<h1>Hello,  %s </h1>' % (environ['PATH_INFO'][1:] or 'web...')
    return [body.encode('utf-8')]

if __name__=='__main__':
    # 创建一个服务器，IP地址为空，端口是8000，处理函数是application:
    httpd = make_server('',8000,application2)
    print('Serving HTTP on port 8000...')
    httpd.serve_forever()
