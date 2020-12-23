'''
FilePath: /multiprocess/process2.py
Description: 
'''
from multiprocessing import Process
import time
import os

class SubProcess(Process):
    def __init__(self, interval, name=''):
        Process.__init__(self)      # 调用父类的初始化方法
        self.interval = interval
        if name:
            self.name = name

    # 重写 run() 方法
    def run(self):
        print("子进程 (%s) 开始执行，父进程为 (%s)" % (os.getpid(), os.getppid()))
        t_start = time.time()
        time.sleep(self.interval)
        t_end = time.time()
        print("子进程 (%s) 执行结束，耗时%0.2f秒" % (os.getpid(), t_end - t_start))

if __name__ == '__main__':
    print("---父进程开始执行---")
    print("父进程 PID: %s" % os.getpid())
    p1 = SubProcess(interval=1, name='test')
    p2 = SubProcess(interval=2)
    p1.start()  # 对一个不包含 target 属性的 Process 类执行 start() 方法，就会运行这个类中的 run() 方法
    p2.start()

    print("p1.is_alive = %s" % p1.is_alive())
    print("p2.is_alive = %s" % p2.is_alive())

    print("p1.name = %s" % p1.name)
    print("p1.pid = %s" % p1.pid)
    print("p2.name = %s" % p2.name)
    print("p2.pid = %s" % p2.pid)

    print("---等待子进程---")
    p1.join()
    p2.join()
    print("---父进程执行结束---")