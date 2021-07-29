import threading
import time
import logging
import random

logging.basicConfig(level=logging.DEBUG, format='(%(threadName)-9s) %(message)s', )


class Counter(object):
    def __init__(self, start=0):
        self.lock = threading.Lock()
        self.value = start

    def increment(self):
        logging.debug('Waiting for a lock')
        self.lock.acquire()
        try:
            logging.debug('Acquire a lock')
            self.value = self.value + 1
        finally:
            logging.debug('Lock released')
            self.lock.release()


def worker(counter_instance: Counter):
    for i in range(2):
        r = random.random()
        logging.debug(f'Sleeping {round(r, 2)}')
        time.sleep(r)
        counter_instance.increment()
    logging.debug('Done')


if __name__ == '__main__':
    counter = Counter()
    threads = []
    for i in range(2):
        t = threading.Thread(target=worker, args=(counter,))
        t.start()
        threads.append(t)

    logging.debug('Waiting for worker threads')
    for t in threads:
        t.join()

    logging.debug(f'Counter: {counter.value}')
