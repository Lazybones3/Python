import asyncio
'''
def callback(sleep_times):
    print("sleep {} success".format(sleep_times))
def stoploop(loop):
    loop.stop()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    # 进入循环立即执行
    # loop.call_soon(callback, 2)
    # loop.call_soon(stoploop, loop)
    # loop.run_forever()
    # 进入循环n秒后执行
    # loop.call_later(2, callback, 2)
    # loop.call_later(1, callback, 1)
    # loop.call_later(3, callback, 3)
    # loop.run_forever()
    # 指定时间启动
    now = loop.time()
    loop.call_at(now+2, callback, 2)
    loop.call_at(now+1, callback, 1)
    loop.call_at(now+3, callback, 3)
    loop.run_forever()
'''
# 查看启动的时间
def callback(loop):
    print("success time {}".format(loop.time()))

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    now = loop.time()
    loop.call_at(now+2, callback, loop)
    loop.call_at(now+1, callback, loop)
    loop.call_at(now+3, callback, loop)
    loop.call_soon(callback, loop)
    loop.run_forever()
