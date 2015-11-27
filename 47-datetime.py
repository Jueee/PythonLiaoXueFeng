'''
datetime

datetime 是 Python 处理日期和时间的标准库。

datetime是模块，datetime模块还包含一个datetime类。

通过from datetime import datetime导入的才是datetime这个类。
'''

# 获取当前日期和时间
from datetime import datetime

now = datetime.now()

print(now)
print(type(now))



# 获取指定日期和时间
# 要指定某个日期和时间，我们直接用参数构造一个datetime：
from datetime import datetime

dt = datetime(2015,4,21,22,3,32)
print(dt)




# datetime转换为timestamp
'''
在计算机中，时间实际上是用数字表示的。
我们把1970年1月1日 00:00:00 UTC+00:00时区的时刻称为epoch time，记为0（1970年以前的时间timestamp为负数），当前时间就是相对于epoch time的秒数，称为timestamp。
'''
from datetime import datetime

dt = datetime(2014,2,3,3,42,43)
print(dt.timestamp())

print(datetime.now().timestamp())




# timestamp转换为datetime
# 转换是在timestamp和本地时间做转换。
from datetime import datetime

t = 1391370163
print(datetime.fromtimestamp(t))

t = 123232
print(datetime.fromtimestamp(t))

t = 32232323129
print(datetime.fromtimestamp(t))


t = 1429417200.0
print(datetime.fromtimestamp(t))    # 本地时间
print(datetime.utcfromtimestamp(t)) # UTC时间

print('----str转换为datetime----')


# str转换为datetime
# 转换方法是通过datetime.strptime()实现，需要一个日期和时间的格式化字符串：
# 注意转换后的datetime是没有时区信息的。
from datetime import datetime

cday = datetime.strptime('2015-6-1 18:43:23','%Y-%m-%d %H:%M:%S')
print(cday)



# datetime转换为str
from datetime import datetime

now = datetime.now()
print(now.strftime('%a,%b %d %H:%M'))



print('----datetime加减----')
# datetime加减
from datetime import datetime,timedelta

now = datetime.now()
print(now)
print(now + timedelta(hours=10))
print(now - timedelta(days=1))
print(now + timedelta(days=3,hours=4))





print('----本地时间转换为UTC时间----')
# 本地时间转换为UTC时间
# 一个datetime类型有一个时区属性tzinfo，但是默认为None，所以无法区分这个datetime到底是哪个时区
# 除非强行给datetime设置一个时区：
from datetime import datetime,timedelta,timezone

tz_utc_8 = timezone(timedelta(hours=8))     # 创建时区UTC+8:00
now = datetime.now()
print(now)

dt = now.replace(tzinfo = tz_utc_8)
print(dt)





print('----时区转换----')
# 时区转换
# 拿到UTC时间，并强制设置时区为UTC+0:00
# 时区转换的关键在于，拿到一个datetime时，要获知其正确的时区，然后强制设置时区，作为基准时间。
# 利用带时区的datetime，通过astimezone()方法，可以转换到任意时区。
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
print(utc_dt)

bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print(bj_dt)

tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt)

tokyo_dt2 = bj_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt2)



