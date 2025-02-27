# 选择排序

def select_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i,n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[min_index],arr[i] = arr[i], arr[min_index]
    return arr

# 冒泡排序
def bubble_sort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            if arr[j] < arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr


# 插入排序
def insertion_sort(arr):
    n = len(arr)
    for i in range(n):
        pass






if __name__ == '__main__':
    unsort_list = [12, 22, 32, 55, 65, 76, 8789, 56, 234, 123, 43, 562, 1, 43]
    # 选择排序
    res = select_sort(unsort_list)
    print("排序后的列表是：", res)

    # 冒泡排序
    res = bubble_sort(unsort_list)
    print("排序后的列表是：", res)

    # 插入排序
    # res = insertion_sort(unsort_list)
    # print("排序后的列表是：", res)
