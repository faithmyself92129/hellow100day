"""异步I/O 操作-asyncio模块"""

import asyncio
import threading

async def hello():
    print('%s:hello,world!' % threading.current_thread())
    #休眠不会堵塞主线程因为使用异步I/o操作
    #注意有yield from才会等待休眠操作执行完成
    await asyncio.sleep(2)


    print('%s: goodbye, world!' % threading.current_thread())

loop = asyncio.get_event_loop()
tasks = [hello(), hello()]
#等待两个异步I/o操作执行结束
loop.run_until_complete(asyncio.wait(tasks))
print('game over')
loop.close()



