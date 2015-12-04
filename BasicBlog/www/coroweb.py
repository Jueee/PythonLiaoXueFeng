'''
Day 5 - 编写Web框架

'''

'''
从使用者的角度来说，aiohttp相对比较底层，编写一个URL的处理函数需要这么几步：

第一步，编写一个用@asyncio.coroutine装饰的函数：
@asyncio.coroutine
def handle_url_():
    pass

第二步，传入的参数需要自己从request中获取：
url_param = request.match_info['key']
query_params = parse_qs(request.query_string)

最后，需要自己构造Response对象：
text = render('template',data)
return web.Response(text.encode('utf-8'))
'''
'''
这些重复的工作可以由框架完成。

例如，处理带参数的URL/blog/{id}可以这么写：
@get('/blog/{id}')
def get_blog(id):
    pass

处理query_string参数可以通过关键字参数**kw或者命名关键字参数接收：
@get('/api/commects')
def api_comments(*, page= '1'):
    pass

对于函数的返回值，不一定是web.Response对象，可以是str、bytes或dict。
如果希望渲染模板，我们可以这么返回一个dict：
return {
    '__template__':'index.html',
    'data':'...'
}

编写简单的函数而非引入request和web.Response还有一个额外的好处，就是可以单独测试，否则，需要模拟一个request才能测试。
'''

import asyncio, os, inspect, logging, functools
from urllib import parse
from aiohttp import web
from apis import APIError

# 要把一个函数映射为一个URL处理函数，我们先定义@get()：
def get(path):
    '''
    Define decorator @get('/path)
    '''
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            return func(*args, **kw)
        wrapper.__method__ = 'GET'
        wrapper.__route__ = path
        return wrapper
    return decorator


# @post与@get定义类似。
def post(path):
    '''
    Define decorator @post('/path)
    '''
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            return func(*args, **kw)
        wrapper.__method__ = 'POST'
        wrapper.__route__ = path
        return wrapper
    return decorator


'''
定义RequestHandler

URL处理函数不一定是一个coroutine，因此我们用RequestHandler()来封装一个URL处理函数。

RequestHandler是一个类，由于定义了__call__()方法，因此可以将其实例视为函数。

RequestHandler目的就是从URL函数中分析其需要接收的参数，从request中获取必要的参数，调用URL函数，然后把结果转换为web.Response对象，这样，就完全符合aiohttp框架的要求：

'''
def has_request_arg(fn):
    sig = inspect.signature(fn)
    params = sig.parameters
    found = False
    for name,param in params.items():
        if name == 'request':
            found = True
            continue
        if found and (params.kind != inspect.Parameter.VAR_POSITIONAL and params.kind != inspect.Parameter.KEYWORD and param.kind != inspect.Parameter.VAR_KEYWORD):
            raise ValueError('request parameter must be the last named parameter in function:%s%s' % (fn.__name__,str(sig)))
        return found


class RequestHandler(object):
    def __init__(self, app, fn):
        self._app = app
        self._func = fn
        self._has_request_arg = has_request_arg(fn)

    @asyncio.coroutine
    def __call__(self, request):
        kw = None
        if kw is None:
            kw = dict(**request.match_info)
        else:
            pass
        if self._has_request_arg:
            kw['request'] = request
        logging.info('call with args:%s' % str(kw))
        try:
            r = yield from self._func(**kw)
            return r
        except APIError as e:
            return dict(error=e.error,data=e.data,message=e.message)
        
def add_static(app):
    pass

# add_route函数，用来注册URL处理函数：
def add_route(app, fn):
    method = getattr(fn, '__method__', None)
    path = getattr(fn, '__route__', None)
    if path is None or method is None:
        raise ValueError('@get or @post not defined in %s.' % str(fn))
    if not asyncio.iscoroutinefunction(fn) and not inspect.isgeneratorfunction(fn):
        fn = asyncio.coroutine(fn)
    logging.info('add route %s %s => %s(%s)' % (method, path, fn.__name__, ','.join(inspect.signature(fn).parameters.keys())))
    app.router.add_route(method,path,RequestHandler(app,fn))


'''
最后一步，把很多次add_route()注册的调用：
add_route(app, handles.index)
add_route(app, handles.blog)
add_route(app, handles.create_comment)
...

变成自动扫描：
# 自动把handler模块的所有符合条件的函数注册了:
add_routes(app, 'handlers')
'''
def add_routes(app, module_name):
    n = module_name.rfind('.')
    if n == (-1):
        mod = __import__(module_name, globals(), locals())
    else:
        name = module_name[n+1:]
        mod = getattr(__import__(module_name[:n],globals(),locals(),[name]),name)
    for attr in dir(mod):
        if attr.startswith('_'):
            continue
        fn = getattr(mod, attr)
        if callable(fn):
            method = getattr(fn, '__method__', None)
            path = getattr(fn, '__method__', None)
            if method and path:
                add_route(app, fn)







