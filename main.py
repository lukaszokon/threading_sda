import threading
import time


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


if __name__ == '__main__':
    t1 = ThreadWithReturnValue(target=print_square, args=(10,))
    t2 = threading.Thread(target=print_cube, args=(10,))

    t1.start()
    t2.start()

    print(t1.join())
    t2.join()

    print('Koniec programu')
