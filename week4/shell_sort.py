def shell_sort(array, length):
    h = 1
    while h < length / 3:
        h = int(3 * h + 1)
    while h >= 1:
        for i in range(h, length):
            j = i
            while j >= h and array[j] < array[j - h]:
                array[j], array[j - h] = array[j - h], array[j]
                j -= h
        h = int(h / 3)
print("输入数组个数：")
n=eval(input())
arr=[]
for i in range(0,n):
    arr.append(eval(input()))
shell_sort(arr,n)
for i in range(0,n):
    print(arr[i],end=' ')
#时间复杂度O(n^2)
#空间复杂度O(1)