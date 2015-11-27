'''
HTTP协议

'''
'''
跟踪了新浪的首页，我们来总结一下HTTP请求的流程：

步骤1：浏览器首先向服务器发送HTTP请求，请求包括：
方法：GET还是POST，GET仅请求资源，POST会附带用户数据；
路径：/full/url/path；
域名：由Host头指定：Host: www.sina.com.cn
如果是POST，那么请求还包括一个Body，包含用户数据。

步骤2：服务器向浏览器返回HTTP响应，响应包括：
响应代码：200表示成功，3xx表示重定向，4xx表示客户端发送的请求有错误，5xx表示服务器端处理时发生了错误；
响应类型：由Content-Type指定；
以及其他相关的Header；
通常服务器的HTTP响应会携带内容，也就是有一个Body，包含响应的内容，网页的HTML源码就在Body中。

步骤3：如果浏览器还需要继续向服务器请求其他资源，比如图片，就再次发出HTTP请求，重复步骤1、2。

'''
'''
Web采用的HTTP协议采用了非常简单的请求-响应模式，从而大大简化了开发。
一个HTTP请求只处理一个资源。
'''

'''
HTTP格式

一个HTTP包含Header和Body两部分，其中Body是可选的。
'''
'''
HTTP协议是一种文本协议，所以，它的格式也非常简单。

HTTP GET请求的格式：
GET /path HTTP/1.1
Header1: Value1
Header2: Value2
Header3: Value3

每个Header一行一个，换行符是\r\n。

HTTP POST请求的格式：
POST /path HTTP/1.1
Header1: Value1
Header2: Value2
Header3: Value3

body data goes here...

当遇到连续两个\r\n时，Header部分结束，后面的数据全部是Body。


HTTP响应的格式：
200 OK
Header1: Value1
Header2: Value2
Header3: Value3

body data goes here...
'''