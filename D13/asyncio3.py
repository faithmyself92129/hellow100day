"""异常I/O操作-asyncio模块"""

import asyncio

async def wget(host):
    print('wget %s...' % host)
    connect = asyncio.open_connection(host, 80)
    #异步方式等待连接结果
    reader, writer = await connect
    header = 'GET / HTTP/1.0\r\nHost:%s \r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    #异步I/o方式执行写操作
    await writer.drain()
    while True:
        #异步I/o方式执行读操作
        line = await reader.readline()
        if line == b'\r\n':
            break
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))

    writer.close()

loop = asyncio.get_event_loop()
#通过生成是语法创建一个装有三个携程的列表
hosts_list = ['www.sina.cn', 'www.sohu.com', 'www.163.com']
tasks = [wget(host) for host in hosts_list]
#下面的方法将异步I/O操作放入Eventloop自刀执行完成
loop.run_until_complete(asyncio.wait(tasks))
loop.close()




