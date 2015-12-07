'''
Day 13 - 提升开发效率

让服务器检测到代码修改后自动重新加载呢
'''
'''
其实Python本身提供了重新载入模块的功能，但不是所有模块都能被重新载入。
另一种思路是检测www目录下的代码改动，一旦有改动，就自动重启服务器。
'''
'''
按照这个思路，我们可以编写一个辅助程序pymonitor.py，让它启动wsgiapp.py，并时刻监控www目录下的代码改动，有改动时，先把当前wsgiapp.py进程杀掉，再重启，就完成了服务器进程的自动重启。
'''
'''
要监控目录文件的变化，我们也无需自己手动定时扫描，Python的第三方库watchdog可以利用操作系统的API来监控目录文件的变化，并发送通知。
我们先用pip安装：
$ pip3 install watchdog
利用watchdog接收文件变化的通知，如果是.py文件，就自动重启wsgiapp.py进程。
'''
'''
利用Python自带的subprocess实现进程的启动和终止，并把输入输出重定向到当前进程的输入输出中：
'''
'''
用下面的命令启动服务器：
cmd:
$ python pymonitor.py app.py
'''
import os, sys, time, subprocess, logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

def log(s):
    print('[Monitor] %s' % s)

class MyFileSystemEventHandler(FileSystemEventHandler):
    """docstring for MyFileSystemEventHandler"""
    def __init__(self, fn):
        super(MyFileSystemEventHandler, self).__init__()
        self.restart = fn
    
    def on_any_event(self, event):
        if event.src_path.endswith('.py'):
            log('Python source file changed:%s' % event.src_path)
            self.restart()

command = ['echo', 'ok']
process = None

def kill_process():
    global process
    if process:
        log('Kill process [%s]...' % process.pid)
        process.kill()
        process.wait()
        log('Process ended with codee %s.' % process.returncode)
        process = None

def start_process():
    global process, command
    log('Start process %s...' % ' '.join(command))
    process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr)

def restart_process():
    kill_process()
    start_process()

def start_watch(path, callback):
    observer = Observer()
    observer.schedule(MyFileSystemEventHandler(restart_process), path, recursive=True)
    observer.start()
    log('Watching directory %s...' % path)
    start_process()
    try:
        while True:
            time.sleep(0.5)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == '__main__':
    argv = sys.argv[1:]
    if not argv:
        print('Usage: ./pymonotor your-script.py')
        exit(0)
    if argv[0]  != 'python':
        argv.insert(0, 'python')
    command = argv
    path = os.path.abspath('.')
    start_watch(path, None)