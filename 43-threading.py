'''
多线程

进程是由若干线程组成的，一个进程至少有一个线程。

Python的标准库提供了两个模块：_thread和threading，_thread是低级模块，threading是高级模块，对_thread进行了封装。

启动一个线程就是把一个函数传入并创建Thread实例，然后调用start()开始执行：
'''

'''
由于任何进程默认就会启动一个线程，我们把该线程称为主线程，主线程又可以启动新的线程.

Python的threading模块有个current_thread()函数，它永远返回当前线程的实例。

主线程实例的名字叫MainThread，子线程的名字在创建时指定，我们用LoopThread命名子线程。
名字仅仅在打印时用来显示，完全没有其他意义，如果不起名字Python就自动给线程命名为Thread-1，Thread-2……
'''
import time,threading

# 新线程执行的代码:
def loop():
	print('thread %s is running...' % threading.current_thread().name)
	n = 0
	while n < 5:
		n = n + 1
		print('thread %s >>> %s' % (threading.current_thread().name, n))
		time.sleep(1)
	print('thread %s ended.' % threading.current_thread().name)

if __name__=='__main__':
	print('thread %s is running...' % threading.current_thread().name)
	t = threading.Thread(target = loop, name = 'LoopThread')
	t.start()
	t.join()
	print('thread %s ended.' % threading.current_thread().name)




'''
Lock

多线程和多进程最大的不同在于:
1、多进程中，同一个变量，各自有一份拷贝存在于每个进程中，互不影响
2、多线程中，所有变量都由所有线程共享，所以，任何一个变量都可以被任何一个线程修改

因此，线程之间共享数据最大的危险在于多个线程同时改一个变量，把内容给改乱了。
'''
import time,threading

# 假定这是你的银行存款:
balance = 0

def change_it(n):
	# 先存后取，结果应该为0:
	global balance
	balance = balance + n
	balance = balance - n

def run_thread(n):
	for i in range(1000000):
		change_it(n)

# 当t1、t2交替执行时，只要循环次数足够多，balance的结果就不一定是0了。
t1 = threading.Thread(target=run_thread,args=(5,))
t2 = threading.Thread(target=run_thread,args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)


'''
如果我们要确保balance计算正确，就要给change_it()上一把锁，当某个线程开始执行change_it()时，我们说，该线程因为获得了锁，因此其他线程不能同时执行change_it()，只能等待，直到锁被释放后，获得该锁以后才能改。
由于锁只有一个，无论多少线程，同一时刻最多只有一个线程持有该锁，所以，不会造成修改的冲突。

创建一个锁就是通过threading.Lock()来实现.

获得锁的线程用完后一定要释放锁，否则那些苦苦等待锁的线程将永远等待下去，成为死线程。
所以我们用try...finally来确保锁一定会被释放。
'''
balance = 0
lock = threading.Lock()
def run_thread(n):
	for i in range(1000000):
		# 先要获取锁:
		lock.acquire()
		try:
			change_it(n)
		finally:
			# 改完了一定要释放锁:
			lock.release()

t1 = threading.Thread(target=run_thread,args=(5,))
t2 = threading.Thread(target=run_thread,args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)




'''
多核CPU

如果你不幸拥有一个多核CPU，你肯定在想，多核应该可以同时执行多个线程。

如果写一个死循环的话，会出现什么情况呢？

打开Mac OS X的Activity Monitor，或者Windows的Task Manager，都可以监控某个进程的CPU使用率。
我们可以监控到一个死循环线程会100%占用一个CPU。
如果有两个死循环线程，在多核CPU中，可以监控到会占用200%的CPU，也就是占用两个CPU核心。
要想把N核CPU的核心全部跑满，就必须启动N个死循环线程。
试试用Python写个死循环：
'''
'''
import threading,multiprocessing

def loop():
	x = 0
	while True:
		x = x ^ 1

for i in range(multiprocessing.cpu_count()):
	t = threading.Thread(target = loop)
	t.start()
'''
'''
因为Python的线程虽然是真正的线程，但解释器执行代码时，有一个GIL锁：Global Interpreter Lock，任何Python线程执行前，必须先获得GIL锁，然后，每执行100条字节码，解释器就自动释放GIL锁，让别的线程有机会执行。这个GIL全局锁实际上把所有线程的执行代码都给上了锁，所以，多线程在Python中只能交替执行，即使100个线程跑在100核CPU上，也只能用到1个核。

GIL是Python解释器设计的历史遗留问题，通常我们用的解释器是官方实现的CPython，要真正利用多核，除非重写一个不带GIL的解释器。

所以，在Python中，可以使用多线程，但不要指望能有效利用多核。如果一定要通过多线程利用多核，那只能通过C扩展来实现，不过这样就失去了Python简单易用的特点。

不过，也不用过于担心，Python虽然不能利用多线程实现多核任务，但可以通过多进程实现多核任务。多个Python进程有各自独立的GIL锁，互不影响。


Python解释器由于设计时有GIL全局锁，导致了多线程无法利用多核。多线程的并发在Python中就是一个美丽的梦。
'''


