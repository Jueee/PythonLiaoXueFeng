'''
MySQL

mysql> show variables like '%char%';
+--------------------------+--------------------------------------------------------+
| Variable_name            | Value                                                  |
+--------------------------+--------------------------------------------------------+
| character_set_client     | utf8                                                   |
| character_set_connection | utf8                                                   |
| character_set_database   | utf8                                                   |
| character_set_filesystem | binary                                                 |
| character_set_results    | utf8                                                   |
| character_set_server     | utf8                                                   |
| character_set_system     | utf8                                                   |
| character_sets_dir       | /usr/local/mysql-5.1.65-osx10.6-x86_64/share/charsets/ |
+--------------------------+--------------------------------------------------------+
8 rows in set (0.00 sec)
'''
'''
安装MySQL驱动

MySQL官方提供了mysql-connector-python驱动，但是安装的时候需要给pip命令加上参数--allow-external：

$ pip install mysql-connector-python --allow-external mysql-connector-python
'''
# 导入MySQL驱动:
import mysql.connector

# 注意把password设为你的root口令:
conn = mysql.connector.connect(user='root',password='password',database='test')
cursor = conn.cursor()
# 创建user表:
try:
    # 执行一条SQL语句，创建user表:
    cursor.execute('create table book(id varchar(20) primary key,name varchar(20),user_id varchar(20))')
except Exception as e:
    pass
try:
    # 继续执行一条SQL语句，插入一条记录:
    cursor.execute("insert into user(id,name) values ('5','民生')")
    # 通过rowcount获得插入的行数:
    print(cursor.rowcount)
except Exception as e:
    pass

# 关闭Cursor:
cursor.close()
# 提交事务:
conn.commit()
# 关闭Connection:
conn.close()


'''
查询记录：
'''
conn = mysql.connector.connect(user='root', password='password', database='test')
cursor = conn.cursor()
# 执行查询语句:
cursor.execute('select * from user where id=%s',['2'])
# 获得查询结果集:
values = cursor.fetchall()
print(values)
cursor.execute('select * from user')
values = cursor.fetchall()
print(values)
cursor.close()
conn.close()
