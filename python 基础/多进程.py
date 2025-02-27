# 1. 数据处理：并行计算列表元素的平方和

import multiprocessing
import time


def handle_request(client_id):
    print(f"开始处理客户端 {client_id} 的请求")
    time.sleep(2)  # 模拟处理请求所需的时间
    print(f"客户端 {client_id} 的请求处理完成")

if __name__ == '__main__':

    pool = multiprocessing.Pool(4)
    pool.map(handle_request, [1,2,3,4,5])
