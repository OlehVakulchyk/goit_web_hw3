import sys
from multiprocessing import Process, cpu_count
import time


def factorize(num):
    list_del = []
    for i in range(1, (num + 1) // 2):
        if num % i == 0:
            list_del.append(i)
    list_del.append(num)
    print(list_del)
    sys.exit(0)


def main(*numbers):
    mp = []
    start = time.time()
    print(f'CPU: {cpu_count()}')
    for number in numbers:
        pr = Process(target=factorize, args=(number, ))
        pr.start()
        mp.append(pr)
    # [print(pr.exitcode, end=' ') for pr in mp]
    # print('')
    [el.join() for el in mp]
    # print(mp)
    # [print(pr.exitcode, end=' ') for pr in mp]
    end = time.time()
    print(f'\nFinish! Total time: {end - start} sec')


if __name__ == '__main__':
    main(128, 255, 99999, 10651060, 123456789, 234567890)