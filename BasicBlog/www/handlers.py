import re, time, json, logging, hashlib, base64, asyncio

from coroweb import get, post

from models import User, Comment, Blog, next_id


@get('/')
def index(request):
 #   users = yield from User.findAll()
    summary = 'balabala'
    blogs = [
        Blog(id='1',name='Testr Blog',summary=summary,created_at=time.time()-120),
        Blog(id='2',name='Something New',summary=summary,created_at=time.time()-3600),
        Blog(id='3',name='Learn Swift',summary=summary,created_at=time.time()-7200)
    ]
    return {
        '__template__':'blogs.html',
  #      'users':users,
        'blogs':blogs
    }
'''
@get('/api/users')
def api_get_users(* ,page='1'):
    page_index = get_page_index(page)
    num = yield from User.findNumber('count(id)')
    p = Page(num,page_index)
    if num == 0:
        return dict(page=0, users=())
    users = yield from User.findAll(orderBy='created_at desc',limit=(p.offset,p.limit))
    for u in users:
        u.passwd = '******'
    return dict(page=p,users=users)
'''

@get('/api/users')
def api_get_users():
    users = yield from User.findAll(orderBy='created_at desc')
    for u in users:
        u.passwd = '******'
    return dict(users=users)