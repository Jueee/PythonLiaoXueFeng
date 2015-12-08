import re, time, json, logging, hashlib, base64, asyncio

from coroweb import get, post
from aiohttp import web
from models import User, Comment, Blog, next_id
from apis import APIValueError,APIError
from config import configs

COOKIE_NAME = 'awesession'
_COOKIE_KEY = configs.session.secret

_RE_EMAIL = re.compile(r'^[a-z0-9\.\-\_]+\@[a-z0-9\-\_]+(\.[a-z0-9\-\_]+){1,4}$')
_RE_SHA1 = re.compile(r'^[0-9a-f]{40}$')

def user2cookie(user, max_age):
    expires = str(int(time.time() + max_age))
    s = '%s-%s-%s-%s' % (user.id, user.passwd, expires, _COOKIE_KEY)
    L = [user.id, expires, hashlib.sha1(s.encode('utf-8')).hexdigest()]
    return '-'.join(L)

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

@get('/register')
def register(request):
    return {
        '__template__':'register.html'
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


@get('/api/users')
def api_get_users():
    users = yield from User.findAll(orderBy='created_at desc')
    for u in users:
        u.passwd = '******'
    return dict(users=users)
'''


@post('/api/users')
def api_register_user(*, email, name, passwd):
    if not name or not name.strip():
        raise APIValueError('name')
    if not email or not _RE_EMAIL.match(email):
        raise APIValueError('email')
    if not passwd or not _RE_SHA1.match(passwd):
        logging.info("pppp%s" % 'balab222ala')
        raise APIValueError('passwd')
    logging.info("pppp%s" % 'balabala')
    users = yield from User.findAll('email=?', [email])
    logging.info("pppp%s" % len(users))
    if len(users) > 0 :
        raise APIError('register:failed','email','Email is alreadly in use.')
    uid = next_id()
    sha1_passwd  = '%s:%s' % (uid, passwd)
    logging.info("pppp%s" % sha1_passwd)
    user = User(id=uid,name=name.strip(),email=email,passwd=hashlib.sha1(sha1_passwd.encode('utf-8')).hexdigest(),image='http://www.gravatar.com/avatar/%s?d=mm&s=120' % hashlib.md5(email.encode('utf-8')).hexdigest())
    yield from user.save()
    # make session cookie:
    r = web.Response()
    r.set_cookie(COOKIE_NAME, user2cookie(user,86400), max_age=86400, httponly=True)
    user.passwd = '******'
    r.contype_type = 'application/json'
    r.body = json.dumps(user, ensure_ascii=False).encode('utf-8')
    return r