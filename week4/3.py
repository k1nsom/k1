def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
print("输入数组个数：")
n=eval(input())
arr=[]
for i in range(1,n+1):
    arr.append(eval(input()))
insertion_sort(arr)
print("排序后数列排序为：")
for i in range(0,n):
    print(arr[i],end=' ')
