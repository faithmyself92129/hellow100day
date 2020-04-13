"""异步I/O操作-asycio模块"""


import  asyncio
import threading

#通过async修饰的函数不再是普通函数而使一个协程
#注意async和await将在3.7中作为关键字出现
async  def hello():
    print('%s:hello, world' % threading.current_thread())
    await asyncio.sleep(2)
    print('%s:goodbye,world!' % threading.current_thread())

loop = asyncio.get_event_loop()
# m = hello()
# tasks = loop.create_task(m)
tasks =  hello()

loop.run_until_complete(tasks)
loop.close()

