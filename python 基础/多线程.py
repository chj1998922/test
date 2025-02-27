import concurrent.futures
import time


# 定义一个模拟任务的函数
def task(n):
    return n * n


if __name__ == '__main__':
    all_data = [i for i in range(1000)]
    size = 10
    batch_data = [all_data[i: i + size] for i in range(0, len(all_data), size)]

    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        for i in batch_data:
            res = executor.map(task, i)
            print(list(res))
            print("*********")
