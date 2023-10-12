import  time
import  random
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
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
arr1=[]
arr2=[]
print("在100个数字下排序时间对比:")
for i in range(0,100):
    temp=random.randint(0,1000)
    arr1.append(temp)
    arr2.append(temp)
start1=time.time()
shell_sort(arr1,100)
end1=time.time()
print('Shell sort\'s running time: %s Seconds'%(end1-start1))
start1=time.time()
insertion_sort(arr2)
end1=time.time()
print('Insert sort\'s running time: %s Seconds'%(end1-start1))
print("在1000数字下:")
for i in range(0,1000):
    temp=random.randint(0,1000)
    arr1.append(temp)
    arr2.append(temp)
start1=time.time()
shell_sort(arr1,1000)
end1=time.time()
print('Shell sort\'s running time: %s Seconds'%(end1-start1))
start1=time.time()
insertion_sort(arr2)
end1=time.time()
print('Insert sort\'s running time: %s Seconds'%(end1-start1))
print("在10000数据下")
for i in range(0,10000):
    temp=random.randint(0,1000)
    arr1.append(temp)
    arr2.append(temp)
start1=time.time()
shell_sort(arr1,10000)
end1=time.time()
print('Shell sort\'s running time: %s Seconds'%(end1-start1))
start2=time.time()
insertion_sort(arr2)
end2=time.time()
print('Insert sort\'s running time: %s Seconds'%(end2-start2))