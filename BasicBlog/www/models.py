
'''
我们先考虑如何定义一个User对象，然后把数据库表users和它关联起来。
'''
from orm import Model, StringField, IntegerField

class User(Model):
    __table__ = 'users'

    id = IntegerField(primary_key=True)
    name = StringField()

def test():
    print('--')
    user = yield from User.find('123')
    print(user)
def test2():
    user = yield from User(id=123, name='Michael')
    yield from user.save()
if __name__=='__main__':
    print('--')
    test2()
    #user = User(id=123, name='Michael')
    # 存入数据库:
    #user.insert()
    # 查询所有User对象: