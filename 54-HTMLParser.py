'''
HTMLParser

Python提供了HTMLParser来非常方便地解析HTML
'''
from html.parser import HTMLParser
from html.entities import name2codepoint

class MyHTMLParser(HTMLParser):
    def handle_starttag(self,tag,attrs):
        print('<%s>' % tag)
    def handle_endtag(self,tag):
        print('<%s>' % tag)
    def handle_startendtag(self,tag,attrs):
        print('<%s>' % tag)
    def handle_data(self,data):
        print(data)
    def handle_comment(self,data):
        print('<!-->',data,'-->')
    def handle_entityred(self,name):
        print('&#%s;' % name)
# feed()方法可以多次调用，也就是不一定一次把整个HTML字符串都塞进去，可以一部分一部分塞进去。
# 特殊字符有两种，一种是英文表示的&nbsp;，一种是数字表示的&#1234;，这两种字符都可以通过Parser解析出来。
parser = MyHTMLParser()

parser.feed('''<html>
<head></head>
<body>
<!-- test html parser -->
    <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
</body></html>''')


print('----解析网页----')

from html.parser import HTMLParser
from html.entities import name2codepoint

class JueHTMLParser(HTMLParser):
    def __init__(self):
        super(JueHTMLParser,self).__init__()
        self._flag = ''

    def handle_starttag(self,tag,attrs):
        if ('class','event-title') in attrs:
            self._flag = 'Title:'
        elif ('class','event-location') in attrs:
            self._flag = 'Location:'
        elif tag == 'time':
            self._flag = 0

    def handle_data(self,data):
        if self._flag in('Title:','Location:'):
            if self._flag == 'Title:':
                print('-'*30)
            print(self._flag,data.strip())
            self._flag = ''
        if isinstance(self._flag,int):
            l = ['-',',','\n']
            if self._flag < 3:
                print('Time:',data.strip(),end=l[self._flag])
                self._flag += 1

parser = JueHTMLParser()
with open('samples/sample.html') as f:
    parser.feed(f.read())
'''
关于time这段，我理解运行的时候是这样的：

1、网页中时间的html是这样的：
<time datetime="2015-09-18T00:00:00+00:00">18 Sept. – 20 Sept. <span class="say-no-more"> 2015</span></time>
2、解析的时候，解析出来的tag是time，attrs是2015-09-18T00:00:00+00:00
3、解析的时候，解析出来的data是分三段的（也就是<time...和</time>之间的数据，其中包括了<span.../span>之间的数据）：
    （A）18 Sept.
    （B）20 Sept
    （C）2015
    这三段数据打印的格式是：A-B,C\n
    其中‘-’，‘，’和‘\n’是由程序插入到打印输出中的。这就是列表l = ['-', ',', '\n']的用处。知道了l的这个用法，相信你可以理解下标如果控制在A、B、C间输出对应的列表值了。
'''