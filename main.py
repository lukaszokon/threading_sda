import time
import timeit


def print_cube(num):
    time.sleep(5)
    print(f'Cube: {num ** 3}')


def print_square(num):
    time.sleep(5)
    return num ** 2


def iterate_print(iter):
    for item in iter:
        print(item)

import requests


def crawl(url, dest):
    try:
        result = requests.get(url).text
        with open(dest, 'a') as f:
            f.write(result)

    except requests.exceptions.RequestException:
        print("Błędny URL")


def count(_from, _to):
    while _from >= _to:
        _from -= 1


def without_threading_func():
    count(400000,0)


def with_threading_func():
    import threading
    th1 = threading.Thread(target=count, args=(400000,300000))
    th2 = threading.Thread(target=count, args=(300000,200000))
    th3 = threading.Thread(target=count, args=(200000, 100000))
    th4 = threading.Thread(target=count, args=(100000, 0))

    th1.start()
    th2.start()
    th3.start()
    th4.start()

    th1.join()
    th2.join()
    th3.join()
    th4.join()


def with_multiprocessing_func():
    import multiprocessing
    p1 = multiprocessing.Process(target=count, args=(400000,200000))
    p2 = multiprocessing.Process(target=count, args=(200000,0))

    p1.start()
    p2.start()

    p1.join()
    p2.join()



if __name__ == '__main__':

    wo_threading = "without_threading_func()"
    with_threading = "with_threading_func()"
    with_multiprocessing = "with_multiprocessing_func()"


    setup = 'from __main__ import without_threading_func, with_threading_func, with_multiprocessing_func'
    print("Bez wątków:", timeit.timeit(stmt=wo_threading, setup=setup, number=100))
    print("Z wątkami:", timeit.timeit(stmt=with_threading, setup=setup, number=100))
    print("Z podprocesami:", timeit.timeit(stmt=with_multiprocessing, setup=setup, number=10))
