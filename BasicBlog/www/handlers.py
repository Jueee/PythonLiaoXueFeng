import re, time, json, logging, hashlib, base64, asyncio

from coroweb import get, post
from aiohttp import web
from models import User, Comment, Blog, next_id
from apis import APIValueError,APIError,APIPermissionError
from config import configs

COOKIE_NAME = 'awesession'
_COOKIE_KEY = configs.session.secret

_RE_EMAIL = re.compile(r'^[a-z0-9\.\-\_]+\@[a-z0-9\-\_]+(\.[a-z0-9\-\_]+){1,4}$')
_RE_SHA1 = re.compile(r'^[0-9a-f]{40}$')


def check_admin(request):
    logging.info('request.__user__:%s' % (not request.__user__.admin))
    if request.__user__ is None or not request.__user__.admin:
        logging.info('request.__user__:%s' % request.__user__)
        raise APIPermissionError()

# 计算加密cookie:
def user2cookie(user, max_age):
    expires = str(int(time.time() + max_age))
    s = '%s-%s-%s-%s' % (user.id, user.passwd, expires, _COOKIE_KEY)
    L = [user.id, expires, hashlib.sha1(s.encode('utf-8')).hexdigest()]
    return '-'.join(L)

def text2html(text):
    lines = map(lambda s: '<p>%s<p>' % s.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;'), filter(lambda s:s.strip()!='',text.split('\n')))
    return ''.join(lines)

# 解密 cookie
@asyncio.coroutine
def cookie2user(cookie_str):
    '''
    Parse cookie and load user if cookie is valid.
    '''
    if not cookie_str:
        return None
    try:
        L = cookie_str.split('-')
        if len(L) != 3:
            return None
        uid,expires,sha1 = L
        if int(expires) < time.time():
            return None
        user = yield from User.find(uid)
        if user is None:
            return None
        s = '%s-%s-%s-%s' % (uid, user.passwd, expires, _COOKIE_KEY)
        if sha1 != hashlib.sha1(s.encode('utf-8')).hexdigest():
            logging.info('invalid sha1')
            return None
        user.passwd = '******'
        return user
    except Exception as e:
        logging.exception(e)
        return None

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

@get('/signin')
def signin(request):
    return {
        '__template__':'signin.html'
    }

@get('/manage/blogs/create')
def manage_blog_edit(request):
    return {
        '__template__':'manage_blog_edit.html',
        'id':'',
        'action':'/api/blogs'
    }

@get('/blog/{id}')
def get_blog(id):
    blog = yield from Blog.find(id)
    comments = yield from Comment.findAll('blog_id=?',[id],orderBy='created_at desc')
    for c in comments:
        c.html_content = text2html(c.content)
 #   blog.html_content = markdown2.markdown(blog.content)
    return{
        '__template__':'blog.html',
        'blog':blog,
        'comments':comments    
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
@get('/signout')
def signout(request):
    referer = request.headers.get('Referer')
    r = web.HTTPFound(referer or '/')
    r.set_cookie(COOKIE_NAME, '-deleted-', max_age=0, httponly=True)
    logging.info('user signout out.')
    return r

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

@post('/api/authenticate')
def authenticate(*, email, passwd):
    if not email:
        raise APIValueError('email', 'Invalid email.')
    if not passwd:
        raise APIValueError('passwd', 'Invalid password.')
    users = yield from User.findAll('email=?', [email])
    if len(users) == 0:
        raise APIValueError('email', 'Email not exist.')
    user = users[0]
    # cheek passwd
    sha1 = hashlib.sha1()
    sha1.update(user.id.encode('utf-8'))
    sha1.update(b':')
    sha1.update(passwd.encode('utf-8'))
    if user.passwd != sha1.hexdigest():
        raise APIValueError('passwd', 'Invalid password.')
    # authenticate ok, set cookie.
    r = web.Response()
    r.set_cookie(COOKIE_NAME, user2cookie(user,86400), max_age=86400, httponly=True)
    user.passwd = '******'
    r.contype_type = 'application/json'
    r.body = json.dumps(user, ensure_ascii=False).encode('utf-8')
    return r

@get('/api/blogs/{id}')
def api_get_blog(*, id):
    blog = yield from Blog.find(id)
    return blog


# 编写一个REST API，用于创建一个Blog：
@post('/api/blogs')
def api_create_blog(request, *, name, summary, content):
    check_admin(request)
    if not name or not name.strip():
        raise APIValueError('name', 'name cannot be empty.')
    if not summary or not summary.strip():
        raise APIValueError('summary','summary connot be empty. ')
    if not content or not content.strip():
        raise APIValueError('content', 'content connot be empty.')
    blog = Blog(user_id=request.__user__.id,user_name=request.__user__.name,
            user_image=request.__user__.image,name=name.strip(), summary=summary.strip(),content=content.strip())
    
    logging.info('进入方法。。。')
    yield from blog.save()
    return blog

