'''
async/await

用asyncio提供的@asyncio.coroutine可以把一个generator标记为coroutine类型，然后在coroutine内部用yield from调用另一个coroutine实现异步操作。

为了简化并更好地标识异步IO，从Python 3.5开始引入了新的语法async和await，可以让coroutine的代码更简洁易读。

请注意，async和await是针对coroutine的新语法，要使用新的语法，只需要做两步简单的替换：
1、把@asyncio.coroutine替换为async；
2、把yield from替换为await。
剩下的代码保持不变。

注意新语法只能用在Python 3.5以及后续版本，如果使用3.4版本，则仍需使用上一节的方案。
'''
import asyncio

@asyncio.coroutine
def hello():
    print('Hello World...')
    r = yield from asyncio.sleep(1)
    print('Hello again...')


# 新语法重新编写如下：
async def hello():
    print('Hello World...')
    r = await asyncio.sleep(1)
    print('Hello again...')















