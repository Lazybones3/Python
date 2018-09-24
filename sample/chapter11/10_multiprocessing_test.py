import multiprocessing
import time

# 多进程编程
def get_html(n):
    time.sleep(n)
    print("sub_progress success")
    return n

#继承类的方式实现多进程
class MyProgress(multiprocessing.Process):
    def run(self):
        pass

if __name__ == "__main__":
    '''
    progress = multiprocessing.Process(target=get_html,args=(2,))
    print(progress.pid)
    progress.start()
    print(progress.pid)
    progress.join()
    print("main progress end")
    '''

    # 使用进程池
    # 进程池中的进程数量与cpu数量相等
    pool = multiprocessing.Pool(multiprocessing.cpu_count())
    # result = pool.apply_async(get_html, args=(3,))
    # # 等待所有任务完成
    # pool.close()
    # pool.join()
    # print(result.get())

    #imap
    # for result in pool.imap(get_html, [1,5,3]):
    #     print("{} sleep success".format(result))

    #imap_unordered
    for result in pool.imap_unordered(get_html, [1,5,3]):
        print("{} sleep success".format(result))