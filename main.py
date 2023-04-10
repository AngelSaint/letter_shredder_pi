import sys
import multiprocessing as mp
import time


def func_1(time_begin, seconds):
    time.sleep(seconds)
    print("func_1", time.time()-time_begin)


def func_2(time_begin, seconds):
    time.sleep(seconds)
    print("func_2", time.time()-time_begin)


if __name__ == '__main__':
    time_begin = time.time()
    p1 = mp.Process(target=func_1, args=(time_begin, 3))
    p2 = mp.Process(target=func_2, args=(time_begin, 2))
    print("main", time.time()-time_begin)

