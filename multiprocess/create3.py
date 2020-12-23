'''
FilePath: /multiprocess/create3.py
Description: 
'''
from multiprocessing import Pool
import time
import os

def task(name):
    print("子进程 (%s) 开始执行 task %s..." % (os.getpid(), name))
    time.sleep(1)       # 休眠 1 秒

if __name__ == '__main__':
    print("---父进程开始执行---")
    print("父进程 PID: %s" % os.getpid())
    p = Pool(3)         # 定义一个进程池，最大进程数为 3
    begin = time.time()
    print('begin: ', begin)
    for i in range(10):
        p.apply_async(task, args=(i,))  # 使用非阻塞方式调用 task() 函数
        # p.apply(task, args=(i,))

    print("等待所有子进程结束")
    p.close()
    p.join()
    end = time.time()
    print('end: ', end)
    print(end - begin)
    print("---父进程执行结束---")