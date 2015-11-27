'''
SQLAlchemy


'''

# 用tuple表示一行很难看出表的结构。
# 如果把一个tuple用class实例来表示，就可以更容易地看出表的结构来：
class User(object):
    def __init__(self, id, name):
        self.id = id
        self.name = name

'''
这就是传说中的ORM技术：Object-Relational Mapping，把关系数据库的表结构映射到对象上。
'''        
'''
ORM框架

在Python中，最有名的ORM框架是SQLAlchemy。

首先通过pip安装SQLAlchemy：
$ pip install sqlalchemy

ORM就是把数据库表的行与相应的对象建立关联，互相转换。
'''
# 利用上次我们在MySQL的test数据库中创建的user表，用SQLAlchemy来试试：

# 第一步，导入SQLAlchemy，并初始化DBSession：

# 导入
from sqlalchemy import Column,String,create_engine
from sqlalchemy import ForeignKey
from sqlalchemy.orm import sessionmaker,relationship
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()

# 定义User对象:
class User(Base):
    # 表的名字:
    __tablename__ = 'user'
    # 表的结构:
    id = Column(String(20),primary_key=True)
    name = Column(String(20))

'''
create_engine()用来初始化数据库连接。
SQLAlchemy用一个字符串表示连接信息：
'数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名'
'''
# 初始化数据库连接:
engine = create_engine('mysql+mysqlconnector://root:password@localhost:3306/test')
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)

# 有了ORM，我们向数据库表中添加一行记录，可以视为添加一个User对象：
# 创建session对象:
session = DBSession()
try:
    # 创建新User对象:
    new_user = User(id='7',name='Bob')
    # 添加到session:
    session.add(new_user)
    # 提交即保存到数据库:
    session.commit()
except Exception as e:
    pass
# 关闭session:
session.close()


# 有了ORM，查询出来的可以不再是tuple，而是User对象。
# SQLAlchemy提供的查询接口如下：
# 创建Session:
session = DBSession()
# 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
user = session.query(User).filter(User.id=='5').one()
# 打印类型和对象的name属性:
print('type:',type(user))
print('name:',user.name)

user = session.query(User).filter(User.name=='Bob').all()
# 打印类型和对象的name属性:
print('type:',type(user))
for x in range(len(user)):
    print('id:',user[x].id,'name:',user[x].name)

# 关闭session
session.close()

# 由于关系数据库的多个表还可以用外键实现一对多、多对多等关联，相应地，ORM框架也可以提供两个对象之间的一对多、多对多等功能。
# 如果一个User拥有多个Book，就可以定义一对多关系如下：
class Users(Base):
    __tablename__ = 'users'
    id = Column(String(20), primary_key=True)
    name = Column(String(20))
    # 一对多
    books = relationship('Book')

class Book(Base):
    __tablename__ = 'book'
    id = Column(String(20), primary_key=True)
    name = Column(String(20))
    # “多”的一方的book表是通过外键关联到user表的:
    user_id = Column(String(20),ForeignKey('users.id'))

engine = create_engine('mysql+mysqlconnector://root:password@localhost:3306/test')
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)
        
session = DBSession()
try:
    # 创建新User对象:
    for x in range(20):
        new_user = Users(id=str(x),name='Bob'+str(x))
        # 添加到session:
        session.add(new_user)
    # 提交即保存到数据库:
    session.commit()
except Exception as e:
    pass
finally:
    session.close()

session = DBSession()
try:
    # 创建新User对象:
    for x in range(20):
        new_user = Book(id=str(x),name='Book'+str(x),user_id=str(x))
        # 添加到session:
        session.add(new_user)
    # 提交即保存到数据库:
    session.commit()
except Exception as e:
    pass
# 关闭session:
session.close()
        
session = DBSession()
users = session.query(Users).filter(Users.name=='Bob1').all()

# 打印类型和对象的name属性:
print('type:',type(users))
for x in range(len(users)):
    # 当我们查询一个User对象时，该对象的books属性将返回一个包含若干个Book对象的list。
    print('id:',users[x].id,'name:',users[x].name,'books:',users[x].books)
    print('----Bob1所拥有的书----')
    for y in range(len(users[x].books)):
        book  = users[x].books[y]
        print('第',y+1,'本：',book.id,book.name)

print('----查询所有的书----')
book = session.query(Book).filter(Book.name=='Book1').all()
# 打印类型和对象的name属性:
print('type:',type(book))
for x in range(len(book)):
    print('id:',book[x].id,'name:',book[x].name)

print('----模糊查询所有的书----')
book = session.query(Book).filter(Book.name.like('Book1%')).all()
# 打印类型和对象的name属性:
print('type:',type(book))
for x in range(len(book)):
    print('id:',book[x].id,'name:',book[x].name)

# 关闭session
session.close()


'''
    #简单查询
    print(session.query(User).all())
    print(session.query(User.name, User.fullname).all())
    print(session.query(User, User.name).all())
     
    #带条件查询
    print(session.query(User).filter_by(name='user1').all())
    print(session.query(User).filter(User.name == "user").all())
    print(session.query(User).filter(User.name.like("user%")).all())
     
    #多条件查询
    print(session.query(User).filter(and_(User.name.like("user%"), User.fullname.like("first%"))).all())
    print(session.query(User).filter(or_(User.name.like("user%"), User.password != None)).all())
     
    #sql过滤
    print(session.query(User).filter("id>:id").params(id=1).all())
     
    #关联查询 
    print(session.query(User, Address).filter(User.id == Address.user_id).all())
    print(session.query(User).join(User.addresses).all())
    print(session.query(User).outerjoin(User.addresses).all())
     
    #聚合查询
    print(session.query(User.name, func.count('*').label("user_count")).group_by(User.name).all())
    print(session.query(User.name, func.sum(User.id).label("user_id_sum")).group_by(User.name).all())
     
    #子查询
    stmt = session.query(Address.user_id, func.count('*').label("address_count")).group_by(Address.user_id).subquery()
    print(session.query(User, stmt.c.address_count).outerjoin((stmt, User.id == stmt.c.user_id)).order_by(User.id).all())
     
    #exists
    print(session.query(User).filter(exists().where(Address.user_id == User.id)))
    print(session.query(User).filter(User.addresses.any()))
'''






