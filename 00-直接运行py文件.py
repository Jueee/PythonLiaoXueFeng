直接运行py文件

还有同学问，能不能像.exe文件那样直接运行.py文件呢？在Windows上是不行的，但是，在Mac和Linux上是可以的，方法是在.py文件的第一行加上一个特殊的注释：

#!/usr/bin/env python3

print('hello, world')


然后，通过命令给hello.py以执行权限：

$ chmod a+x hello.py




就可以直接运行hello.py了