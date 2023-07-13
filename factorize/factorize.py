import time


def factorize(*numbers):
    for num in numbers:
        list_del = []
        for i in range(1, (num + 1) // 2):
            if num % i == 0:
                list_del.append(i)
        list_del.append(num)
        print(list_del)


def main():
    start = time.time()
    factorize(128, 255, 99999, 10651060, 123456789, 234567890)
    end = time.time()
    print(f'\nEnd! Total time: {end - start} sec')


if __name__ == '__main__':
    main()

