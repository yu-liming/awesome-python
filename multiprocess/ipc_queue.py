'''
FilePath: /multiprocess/ipc_queue.py
Description: 
'''
from multiprocessing import Process, Queue
import time

# 向对列中写入数据
def write_task(q):
    if not q.full():
        for i in range(5):
            message = "消息" + str(i)
            q.put(message)
            print("写入: %s" % message)

# 从队列读取数据
def read_task(q):
    time.sleep(1)
    while not q.empty():
        print("读取: %s" % q.get(True, 2))    # 等待 2 秒，如果还没有读取到任何消息，则抛出异常

if __name__ == '__main__':
    print("---父进程开始---")
    q = Queue()     # 父进程创建 Queue，并传递给子进程
    pw = Process(target=write_task, args=(q,))
    pr = Process(target=read_task, args=(q,))
    pw.start()
    pr.start()

    print("---等待子进程结束---")
    time.sleep(3)
    print("---等待子进程结束---")
    pw.join()
    pr.join()
    print("---父进程结束---")