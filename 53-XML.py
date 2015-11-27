'''
XML

DOM vs SAX

操作XML有两种方法：DOM和SAX。

DOM会把整个XML读入内存，解析为树，因此占用内存大，解析慢，优点是可以任意遍历树的节点。
SAX是流模式，边读边解析，占用内存小，解析快，缺点是我们需要自己处理事件。

正常情况下，优先考虑SAX，因为DOM实在太占内存。
'''
'''
在Python中使用SAX解析XML非常简洁，通常我们关心的事件是start_element，end_element和char_data，准备好这3个函数，然后就可以解析xml了。

当SAX解析器读到一个节点时：
<a href="/">python</a>

会产生3个事件：
start_element事件，在读取<a href="/">时；
char_data事件，在读取python时；
end_element事件，在读取</a>时。
'''

from xml.parsers.expat import ParserCreate

class DefaultSaxHandler(object):
    def start_element(self,name,attrs):
        print('sax:start_element:%s,attrs:%s' % (name,attrs))
    def end_element(self,name):
        print('sax:end_element:%s' % name)
    def char_data(self,text):
        print('sax:char_data：%s' % text)

xml = r'''<?xml version="1.0"?>
<ol>
    <li><a href="/python">Python</a></li>
    <li><a href="/ruby">Ruby</a></li>
</ol>
'''

if __name__ != '__main__':
    handler = DefaultSaxHandler()
    parser = ParserCreate()
    parser.StartElementHandler = handler.start_element
    parser.EndElementHandler = handler.end_element
    parser.CharacterDataHandler = handler.char_data
    parser.Parse(xml)
        


L = []
count = 0
class WeatherSaxHandler(object):
    count = 0
    def start_element(self,name,attrs):
        global L,count
        if name == 'yweather:location':
            L.insert(0,attrs['city'])
            L.insert(1,attrs['country'])
        if name == 'yweather:forecast' and count==0:
            count=count+1
            L.insert(2,attrs['text'])
            L.insert(3,attrs['low'])
            L.insert(4,attrs['high'])
        if name == 'yweather:forecast' and count==1:
            count=count+1
            L.insert(5,attrs['text'])
            L.insert(6,attrs['low'])
            L.insert(7,attrs['high'])
    def end_element(self,name):
        print('sax:end_element:%s' % name)
    def char_data(self,text):
        print('sax:char_data：%s' % text)

with open('samples/sample.xml','rb') as f:
    xml = f.read()
    handler = WeatherSaxHandler()
    parser = ParserCreate()
    parser.StartElementHandler = handler.start_element
  #  parser.EndElementHandler = handler.end_element
  #  parser.CharacterDataHandler = handler.char_data
    parser.Parse(xml)

print(L)