def insertion_sort(arr):
    # 遍历数组中的每一个元素（从第二个元素开始）
    for i in range(1, len(arr)):
        # 当前要插入的元素
        key = arr[i]
        # 前一个元素的索引
        j = i - 1
        # 将比 key 大的元素向右移动
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        # 插入 key
        arr[j + 1] = key

    return arr

# 测试
data = [9, 5, 1, 4, 3]
sorted_data = insertion_sort(data)
print("排序后的结果:", sorted_data)
