import threading
import time
import timeit


class ThreadWithReturnValue(threading.Thread):
    def __init__(self, target, args=(), kwargs=None):
        if kwargs is None:
            kwargs = {}
        self.target = target
        self.args = args
        self.kwargs = kwargs
        self.result = None
        super().__init__()

    def run(self):
        self.result = self.target(*self.args, **self.kwargs)

    def join(self, timeout=None):
        super().join(timeout)
        return self.result


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


def without_threading_func(urls):
    for url in urls:
        crawl(url, 'without_threads.txt')


def with_threading_func(urls):
    threads = []
    for url in urls:
        th = threading.Thread(target=crawl, args=(url, 'with_threads.txt'))
        th.start()
        threads.append(th)

    for th in threads:
        th.join()



if __name__ == '__main__':
    wo_threading = "without_threading_func(urls)"
    with_threading = "with_threading_func(urls)"

    setup = '''
from __main__ import without_threading_func, with_threading_func
    
urls = [
        "https://jsonplaceholder.typicode.com/comments/1",
        "https://jsonplaceholder.typicode.com/comments/2",
        "https://jsonplaceholder.typicode.com/comments/3"
    ]
    '''
    print("Bez wątków:", timeit.timeit(stmt=wo_threading, setup=setup, number=100))
    print("Z wątkami:", timeit.timeit(stmt=with_threading, setup=setup, number=100))
