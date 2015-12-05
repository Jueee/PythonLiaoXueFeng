
# 20151130-02
# 由于我们的Web App建立在asyncio的基础上，因此用aiohttp写一个基本的app.py：
import logging; logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time
from datetime import datetime

from aiohttp import web

from jinja2 import Environment, FileSystemLoader
from coroweb import add_routes, add_static
from orm import create_pool
from apis import APIError
from config import configs

def init_jinja2(app, **kw):
    logging.info('init jinja2...')
    options = dict(
        autoescape = kw.get('autoescape', True),
        block_start_string = kw.get('block_start_string','{%'),
        block_end_string = kw.get('block_end_string','%}'),
        variable_start_string = kw.get('variable_start_string','{{'),
        variable_end_string = kw.get('variable_end_string','}}'),
        auto_reload = kw.get('auto_reload',True)
    )
    path = kw.get('path',None)
    if path is None:
        path = os.path.join(os.path.dirname(os.path.abspath(__file__)),'templates')
    logging.info('set jinja2 template path:%s' % path)
    env = Environment(loader=FileSystemLoader(path),**options)
    filters = kw.get('filters',None)
    if filters is not None:
        for name,f in filters.items():
            env.filters[name] = f
    app['__templating__'] = env
'''
middleware

middleware是一种拦截器，一个URL在被某个函数处理前，可以经过一系列的middleware的处理。
一个middleware可以改变URL的输入、输出，甚至可以决定不继续处理而直接返回。
middleware的用处就在于把通用的功能从每个URL处理函数中拿出来，集中放到一个地方。
'''
# 例如，一个记录URL日志的logger可以简单定义如下：
@asyncio.coroutine
def logger_factory(app, handler):
    @asyncio.coroutine
    def logger(request):
        # 记录日志:
        logging.info('Request:%s %s' % (request.method, request.path))
        # 继续处理请求
        return (yield from handler(request))
    return logger

# 而response这个middleware把返回值转换为web.Response对象再返回，以保证满足aiohttp的要求：
@asyncio.coroutine
def response_factory(app,handler):
    @asyncio.coroutine
    def response(request):
        logging.info('Response handler...')
        # 结果:
        r = yield from handler(request)
        if isinstance(r, web.StreamResponse):
            return r
        if isinstance(r, bytes):
            resp = web.Response(body=r.encode('utf-8'))
            resp.content_type = 'application/octet-stream'
            return resp
        if isinstance(r, str):
            if r.startswith('redirect:'):
                return web.HTTPFound(r[9:])
            resp = web.Response(body=r.encode('utf-8'))
            resp.content_type = 'text/html;charset=utf-8'
            return resp
        if isinstance(r,dict):
            template = r.get('__template__')
            if template is None:
                resp = web.Response(body=json.dumps(r,ensure_ascii=False,default=lambda o:o.__dict__).encode('utf-8'))
                resp.content_type = 'application/json;charset=utf-8'
                return resp
            else:
                resp = web.Response(body=app['__templating__'].get_template(template).render(**r).encode('utf-8'))
                resp.content_type = 'text/html;charset=utf-8'
                return resp
        if isinstance(r, int) and t>=100 and t< 600:
            return web.Response(t)
        if isinstance(r.tuple) and len(r)==2:
            t,m = r
            if isinstance(t,int) and t>=100 and t<600:
                return web.Response(t, str(m))
        # default:
        resp = web.Response(body=str(r).encode('utf-8'))
        resp.content_type = 'text/plain;charset=utf-8'
        return resp
    return response


def datetime_filter(t):
    delta = int(time.time - t)
    if delta < 60:
        return u'1分钟前'
    dt = datetime.fromtimestamp(t)
    return u'%s年%s月%s日' % (dt.year,dt.month,dt.day)


@asyncio.coroutine
def init(loop):
    yield from create_pool(loop=loop, **configs.db)
    app = web.Application(loop=loop, middlewares=[
        logger_factory, response_factory
    ])
    init_jinja2(app,filters=dict(datetime=datetime_filter))
    add_routes(app, 'handlers')
    add_static(app)
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