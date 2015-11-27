'''
在Python中，安装第三方模块，是通过包管理工具pip完成的。

如果你正在使用Mac或Linux，安装pip本身这个步骤就可以跳过了。

如果你正在使用Windows，请参考安装Python一节的内容，确保安装时勾选了pip和Add python.exe to Path。

在命令提示符窗口下尝试运行pip，如果Windows提示未找到命令，可以重新运行安装程序添加pip。

注意：Mac或Linux上有可能并存Python 3.x和Python 2.x，因此对应的pip命令是pip3。
'''

'''
现在，让我们来安装一个第三方库——Python Imaging Library，这是Python下非常强大的处理图像的工具库。
不过，PIL目前只支持到Python 2.7，并且有年头没有更新了，因此，基于PIL的Pillow项目开发非常活跃，并且支持最新的Python 3。

一般来说，第三方库都会在Python官方的pypi.python.org网站注册，要安装一个第三方库，必须先知道该库的名称，可以在官网或者pypi上搜索。
比如Pillow的名称叫Pillow，因此，安装Pillow的命令就是：

pip install Pillow



耐心等待下载并安装后，就可以使用Pillow了。
'''

# 随便找个图片生成缩略图：
from PIL import Image

im = Image.open('samples/sample.png')
print(im.format, im.size, im.mode)

im.thumbnail((200,100))
im.save('samples/thumb.jpg', 'JPEG')