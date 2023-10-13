import random
def generate_random_list(length):
    random_list = []
    for i in range(length):
        random_list.append(random.randint(0, 100))
    random_list.sort()
    return random_list

# 选择排序
def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

# 归并排序
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged
random_list = generate_random_list(10)
print("原始数据：", random_list)
sorted_list1 = selection_sort(random_list.copy())
print("选择排序结果(时间复杂度为O(n^2)：", sorted_list1)
sorted_list2 = merge_sort(random_list.copy())
print("归并排序结果(时间复杂度为O(n*logn))：", sorted_list2)