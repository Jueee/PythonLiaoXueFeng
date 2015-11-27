'''
PIL

PIL：Python Imaging Library，已经是Python平台事实上的图像处理标准库了。
'''
'''
安装Pillow

在命令行下直接通过pip安装：

$ pip install pillow
如果遇到Permission denied安装失败，请加上sudo重试。
'''
'''
操作图像 
'''

# 图像缩放操作

from PIL import Image

# 打开一个jpg图像文件，注意是当前路径:
im = Image.open('samples/sample.png')
# 获得图像尺寸:
w,h = im.size
print('Original image size:%sx%s' % (w,h))
# 缩放到50%:
im.thumbnail((w//2,h//2))
print('Resize image to:%sx%s' % (w//2,h//2))
# 把缩放后的图像用jpeg格式保存:
im.save('samples/jue.jpg','jpeg')



# 模糊效果
from PIL import Image,ImageFilter

# 打开一个jpg图像文件
im = Image.open('samples/sample.png')
# 应用模糊滤镜:
im2 = im.filter(ImageFilter.BLUR)
im2.save('samples/blur.jpg','jpeg')



'''
PIL的ImageDraw提供了一系列绘图方法，让我们可以直接绘图。

比如要生成字母验证码图片：
'''
from PIL import Image,ImageDraw,ImageFont,ImageFilter
import random

# 随机字母
def rndChar():
    return chr(random.randint(65,90))

# 随机颜色1
def rndColor():
    return (random.randint(64,255),random.randint(64,255),random.randint(64,255))

# 随机颜色2
def rndColor2():
    return(random.randint(32,127),random.randint(32,127),random.randint(32,127))   

# 240 * 60
width = 60*4
height = 60
image = Image.new('RGB',(width,height),(255,255,255))
# 创建Font 对象
font = ImageFont.truetype('arial.ttf',36)
# 创建Draw 对象
draw = ImageDraw.Draw(image)
# 填充每个像素
for x in range(width):
    for y in range(height):
        draw.point((x,y),fill=rndColor())
char = ''
# 输出文字
for x in range(4):
    t = rndChar()
    char += t
    draw.text((60 * x + 10,10),t, font = font, fill=rndColor2())
# 模糊
image = image.filter(ImageFilter.BLUR)
image.save('samples/code.jpg','jpeg')

print(char)







