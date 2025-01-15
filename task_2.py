from time import time
from multiprocessing import Pool, cpu_count

def find_divisors(num):
    divisors = []
    for dev in range(1, abs(num) + 1):
        if num % dev == 0:
            divisors.append(dev)
    return divisors
# *********without multiprocessing***********************
def factorize1(*numbers)->list:
    return [find_divisors(number) for number in numbers]

# **********with multiprocessing*************************
def factorize2(*numbers):
    with Pool(processes=cpu_count()) as pool:
        return pool.map(find_divisors, numbers)

# *******************************************************

if __name__ == "__main__":
    st_time = time()
    a, b, c, d  = factorize2(128, 255, 99999, 10651060)
    print(f'Час виконання: {time() - st_time} секунд')

    # Перевірка 1
    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]

    st_time = time()
    a, b, c, d  = factorize2(128, 255, 99999, 10651060)
    print(f'Час виконання: {time() - st_time}')

    # Перевірка 2
    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]
