import multiprocessing
import time
import threading
from datetime import datetime
from multiprocessing import Pool


def read_info(name):
    all_data = []
    with open(name, 'r', encoding='UTF-8') as file:
        while True:
            line = file.readline().strip('\n')
            all_data.append(line)
            if not line:
                break

filenames = ['file 1.txt', 'file 2.txt', 'file 3.txt', 'file 4.txt']

time_start1 = datetime.now()

read_info('file 1.txt')
read_info('file 2.txt')
read_info('file 3.txt')
read_info('file 4.txt')

time_end1 = datetime.now()
time_res1 = time_end1 - time_start1
print(f'Линейная: {time_res1}')


if __name__ == '__main__':
    time_start2 = datetime.now()
    with multiprocessing.Pool(processes=1) as pool:
        pool.map(read_info, filenames)

    time_end2 = datetime.now()
    time_res2 = time_end2 - time_start2
    print(f'Многопроцессорная: {time_res2}')