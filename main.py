import threading


def iterate_print(iter):
    for item in iter:
        print(item)


if __name__ == '__main__':
    t1 = threading.Thread(target=iterate_print, args=(range(5),))
    t2 = threading.Thread(target=iterate_print, args=('Python',))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print('Koniec programu')