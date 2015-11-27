'''
多进程（multiprocessing）

Unix/Linux操作系统提供了一个fork()系统调用，它非常特殊。普通的函数调用，调用一次，返回一次，但是fork()调用一次，返回两次，因为操作系统自动把当前进程（称为父进程）复制了一份（称为子进程），然后，分别在父进程和子进程内返回。

子进程永远返回0，而父进程返回子进程的ID。
这样做的理由是，一个父进程可以fork出很多子进程，所以，父进程要记下每个子进程的ID，而子进程只需要调用getppid()就可以拿到父进程的ID。
'''
import os

if __name__ == '__main__':
	print('test Process (%s) start...' % os.getpid())
try:
	pid = os.fork()
	if pid == 0:
		print('I am child process (%s) and my parent is %s' % (os.getpid(),os.getppid()))
	else:
		print('I (%s) just created a child process (%s).' % (os.getpid(), pid))
except Exception as e:
	'''
	由于Windows没有fork调用，上面的代码在Windows上无法运行。
	'''
	pass

if __name__ == '__main__':
	print()

'''
multiprocessing

multiprocessing 模块是跨平台版本的多进程模块。

multiprocessing 模块提供了一个 Process 类来代表一个进程对象，下面的例子演示了启动一个子进程并等待其结束：
'''
from multiprocessing import Process
import os

# 子进程要执行的代码
def run_proc(name):
	print('Run child process %s (%s)' % (name,os.getpid()))

if __name__ == '__main__':
	print('Parent process %s.' % os.getpid())
	p = Process(target=run_proc, args=('test',))
	print('child process will start.')
	p.start()
	p.join()
	print('Child process end.')



if __name__ == '__main__':
	print()


'''
Pool

如果要启动大量的子进程，可以用进程池的方式批量创建子进程.

对Pool对象调用join()方法会等待所有子进程执行完毕，调用join()之前必须先调用close()，调用close()之后就不能继续添加新的Process了。
'''
from multiprocessing import Pool
import os, time,random

def long_time_task(name):
	print('Run task %s (%s)...' % (name,os.getpid()))
	start = time.time()
	time.sleep(random.random() * 3)
	end = time.time()
	print('Task %s runs %0.2f seconds.' % (name,(end-start)))

if __name__=='__main__':
	print('Parent process %s.' % os.getpid())
	p = Pool(4)
	for i in range(6):
		p.apply_async(long_time_task, args=(i,))
	print('Waiting for all subprocesses done...')
	p.close()
	p.join()
	print('All subprocesses done.')


if __name__ == '__main__':
	print()


'''
子进程

很多时候，子进程并不是自身，而是一个外部进程。我们创建了子进程后，还需要控制子进程的输入和输出。

subprocess模块可以让我们非常方便地启动一个子进程，然后控制其输入和输出。

下面的例子演示了如何在Python代码中运行命令nslookup www.python.org，这和命令行直接运行的效果是一样的：
'''
import subprocess

if __name__=='__main__':
	print('$ nslookup www.python.org')
	r = subprocess.call(['nslookup','www.python.org'])
	print('Exit code:',r)



if __name__ == '__main__':
	print('如果子进程还需要输入，则可以通过communicate()方法输入：')

import subprocess

if __name__=='__main__':
	print('$ nslookup')
	p = subprocess.Popen(['nslookup'], stdin = subprocess.PIPE, stdout=subprocess.PIPE,stderr=subprocess.PIPE)
	output,err=p.communicate(b'set q=mx\npython.org\nexit\n')
	print(output)
	print('Exit code:',p.returncode)



if __name__ == '__main__':
	print('进程间通信')


'''
进程间通信

Process之间肯定是需要通信的，操作系统提供了很多机制来实现进程间的通信。Python的multiprocessing模块包装了底层的机制，提供了Queue、Pipes等多种方式来交换数据。

我们以Queue为例，在父进程中创建两个子进程，一个往Queue里写数据，一个从Queue里读数据：
'''
from multiprocessing import Process,Queue
import os,time,random

# 写数据进程执行的代码
def write(q):
	print('Process to write:%s' % os.getpid())
	for value in ['A','B','C']:
		print('Put %s to queue...' % value)
		q.put(value)
		time.sleep(random.random())

# 读数据进程执行的代码
def read(q):
	print('Process to read:%s' % os.getpid())
	while True:
		value = q.get(True)
		print('Get %s from queue.' % value)

if __name__=='__main__':
	# 父进程创建Queue，并传给各个子进程：
	q = Queue()
	pw = Process(target=write,args=(q,))
	pr = Process(target=read,args=(q,))
	# 启动子进程pw，写入:
	pw.start()
	# 启动子进程pr，读取:
	pr.start()
	# 等待pw结束:
	pw.join()
	# pr进程里是死循环，无法等待其结束，只能强行终止:
	pr.terminate()