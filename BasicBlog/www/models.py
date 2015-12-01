
'''
我们先考虑如何定义一个User对象，然后把数据库表users和它关联起来。

yield 英文意思是生产，是 python 的关键字，在函数返回值时用来替换 return 产生一个值。yield 表达式只能用于定义生成器函数中，在函数外使用 yield 会导致 SyntaxError: 'yield' outside function 。
'''
import time,uuid
import asyncio
from orm import Model, StringField, IntegerField,BooleanField,FloatField,TextField,create_pool

def next_id():
    return '%015d%s000' % (int(time.time() * 1000), uuid.uuid4().hex)

class User(Model):
    __table__ = 'users'

    # 在编写ORM时，给一个Field增加一个default参数可以让ORM自己填入缺省值，非常方便。
    # 并且，缺省值可以作为函数对象传入，在调用save()时自动计算。
    print('next_id',next_id(),type(next_id()))
    id = StringField(primary_key=True, default=next_id(),ddl='varchar(50)')
    email = StringField(ddl='varchar(50)')
    passwd = StringField(ddl='varchar(50)')
    admin = BooleanField()
    name = StringField(ddl='varchar(50)')
    image = StringField(ddl='varchar(500)')
    created_at = FloatField(default=time.time)

class Blog(Model):
    __table__ = 'bolgs'

    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    user_id = StringField(ddl='varchar(50)')
    user_name = StringField(ddl='varchar(50)')
    user_image = StringField(ddl='varchar(500)')
    name = StringField(ddl='varchar(50)')
    summary = StringField(ddl='varchar(200)')
    content = TextField()
    created_at = FloatField(default=time.time)

class Comment(Model):
    __table__ = 'comments'

    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    blog_id = StringField(ddl='varchar(50)')
    user_id = StringField(ddl='varchar(50)')
    user_name = StringField(ddl='varchar(50)')
    user_image = StringField(ddl='varchar(500)')
    content = TextField()
    created_at = FloatField(default=time.time)        


def test(loop):
    yield from create_pool(loop=loop,user='www-data',password='www-data',db='awesome')
    u = User(name='test',email='hellojue@foxmail.com',passwd = '12132',image='about:blank')
    yield from u.save()


# 测试代码
if __name__=='__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(test(loop))
    loop.run_forever()