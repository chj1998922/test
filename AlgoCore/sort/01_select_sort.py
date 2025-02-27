def selection_sort(arr):
    """
    使用选择排序对数组进行排序
    :param arr: 需要排序的数组
    :return: 排序后的数组
    """
    n = len(arr)
    for i in range(n):
        # 假设当前位置 i 是最小值的索引
        min_index = i
        # 在剩余未排序的部分中找到最小值
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # 将找到的最小值与当前位置 i 的值交换
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

# 测试选择排序
if __name__ == "__main__":
    unsorted_list = [64, 34, 25, 12, 22, 11, 90]
    print("未排序数组:", unsorted_list)
    sorted_list = selection_sort(unsorted_list)
    print("排序后数组:", sorted_list)
