def bubble_sort(arr):
    """
    使用冒泡排序对数组进行排序
    :param arr: 需要排序的数组
    :return: 排序后的数组
    """
    n = len(arr)
    # 外层循环，表示比较次数
    for i in range(n):
        # 内层循环，进行相邻元素比较
        swapped = False  # 标志是否有交换
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # 交换相邻元素
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # 如果没有交换，说明数组已经有序，提前结束排序
        if not swapped:
            break
    return arr

# 测试冒泡排序
if __name__ == "__main__":
    unsorted_list = [64, 34, 25, 12, 22, 11, 90]
    print("未排序数组:", unsorted_list)
    sorted_list = bubble_sort(unsorted_list)
    print("排序后数组:", sorted_list)
