import os
import threading
import time
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor
import sys

nums = [50, 63, 8]


def cpu_bound_func(num):
    print(f"{os.getpid()} process | {threading.get_ident()} thread, {num}")
    numbers = range(1, num)
    total = 1
    for i in numbers:
        for j in numbers:
            for k in numbers:
                total *= i * j * k
    return total


def main():
    result = [cpu_bound_func(num) for num in nums]
    print(result)


def multi_thread_main():
    executor = ThreadPoolExecutor(max_workers=3)
    results = list(executor.map(cpu_bound_func, nums))
    print(results)


def multi_process_main():
    executor = ProcessPoolExecutor(max_workers=3)
    results = list(executor.map(cpu_bound_func, nums))
    print(results)


if __name__ == "__main__":

    sys.set_int_max_str_digits(1000000)
    start1 = time.time()
    main()
    end1 = time.time()
    print(end1 - start1)  # 44.26초

    start2 = time.time()
    multi_thread_main()
    end2 = time.time()
    print(end2 - start2)  # 44.259초

    start3 = time.time()
    multi_process_main()
    end3 = time.time()
    print(end3 - start3)  # 39.72초

# 멀티 쓰레드는 cpu bound 환경에서 별 이득을 보지 못함. GIL 때문에.
# 단, 멀티 프로세스에서는 이득을 봄.
