'''
ThreadLocal

在多线程环境下，每个线程都有自己的数据。
一个线程使用自己的局部变量比使用全局变量好，因为局部变量只有线程自己能看见，不会影响其他线程，而全局变量的修改必须加锁。
'''
# 但是局部变量也有问题，就是在函数调用的时候，传递起来很麻烦：
'''
class Student(object):
	def __init__(self, name):
		self.name = name
		
def process_student(name):
	std = Student(name)
	# std是局部变量，但是每个函数都要用它，因此必须传进去：
	do_task_1(std)
	do_task_2(std)
def do_task_1(std):
	do
'''
'''
一个ThreadLocal变量虽然是全局变量，但每个线程都只能读写自己线程的独立副本，互不干扰。

ThreadLocal解决了参数在一个线程中各个函数之间互相传递的问题。
'''
import threading

# 创建全局ThreadLocal对象:
local_school = threading.local()

def process_student():
	# 获取当前线程关联的student:
	std = local_school.student
	print('hello, %s (in %s)' % (std, threading.current_thread().name))

def process_thread(name):
	# 绑定ThreadLocal的student:
	local_school.student = name
	process_student()

t1 = threading.Thread(target=process_thread,args=('Alice',),name='Thread-A')
t2 = threading.Thread(target=process_thread,args=('Bob',),name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()


