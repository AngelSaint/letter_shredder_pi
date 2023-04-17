import multiprocessing as mp
import time


def ImageRecognitionPipeline(seconds):
    time.sleep(seconds)
    print("func_1", time.time()-time_begin)


def WebserverPipeline(seconds):
    time.sleep(seconds)
    print("func_2", time.time()-time_begin)


if __name__ == '__main__':
    time_begin = time.time()
    p1 = mp.Process(target=ImageRecognitionPipeline, args=(0,))
    p2 = mp.Process(target=WebserverPipeline, args=(0,))

    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print("main", time.time() - time_begin)
