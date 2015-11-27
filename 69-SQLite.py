'''
SQLite

SQLite是一种嵌入式数据库，它的数据库就是一个文件。
'''
'''
要操作关系数据库，首先需要连接到数据库，一个数据库连接称为Connection；

连接到数据库后，需要打开游标，称之为Cursor，通过Cursor执行SQL语句，然后，获得执行结果。

Python定义了一套操作数据库的API接口，任何数据库要连接到Python，只需要提供符合Python标准的数据库驱动即可。
'''
'''
由于SQLite的驱动内置在Python标准库中，所以我们可以直接来操作SQLite数据库。
'''
# 导入SQLite驱动:
import sqlite3

# 连接到SQLite数据库
# 数据库文件是test.db
# 如果文件不存在，会自动在当前目录创建:
conn = sqlite3.connect('samples/sample.db')
# 创建一个Cursor:
cursor = conn.cursor()
if __name__ != '__main__':
    # 执行一条SQL语句，创建user表:
    cursor.execute('create table user(id varchar(20) primary key,name varchar(20))')
    # 继续执行一条SQL语句，插入一条记录:
    cursor.execute("insert into user(id,name) values ('1','Michael')")
    # 通过rowcount获得插入的行数:
    print(cursor.rowcount)
# 关闭Cursor:
cursor.close()
# 提交事务:
conn.commit()
# 关闭Connection:
conn.close()


'''
查询记录：
'''
conn = sqlite3.connect('samples/sample.db')
cursor = conn.cursor()
# 执行查询语句:
cursor.execute('select * from user where id=?','2')
# 获得查询结果集:
values = cursor.fetchall()
print(values)
cursor.execute('select * from user')
values = cursor.fetchall()
print(values)
cursor.close()
conn.close()

# 使用Python的DB-API时，只要搞清楚Connection和Cursor对象，打开后一定记得关闭，就可以放心地使用。
# 使用Cursor对象执行insert，update，delete语句时，执行结果由rowcount返回影响的行数，就可以拿到执行结果。
# 使用Cursor对象执行select语句时，通过featchall()可以拿到结果集。结果集是一个list，每个元素都是一个tuple，对应一行记录。
