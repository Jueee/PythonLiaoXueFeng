
# 20151130-02
# 由于我们的Web App建立在asyncio的基础上，因此用aiohttp写一个基本的app.py：
import logging; logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time
from datetime import datetime

from aiohttp import web

def index(request):
    return web.Response(body=b'<h1>Awesome</h1>')

@asyncio.coroutine
def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET','/',index)
    srv = yield from loop.create_server(app.make_handler(),'127.0.0.1',9000)
    logging.info('server started at http://127.0.0.1:9000...')
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()


'''
运行python app.py，Web App将在9000端口监听HTTP请求，并且对首页/进行响应：
$ python3 app.py
INFO:root:server started at http://127.0.0.1:9000...
这里我们简单地返回一个Awesome字符串，在浏览器中可以看到效果.

这说明我们的Web App骨架已经搭好了，可以进一步往里面添加更多的东西。
'''