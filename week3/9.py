l1=[]
l2=[]
n=eval(input())
for i in range(0,n):
    l1.append(eval(input()))
for i in range(0,n):
    sum=1
    for j in range(0,n):
        if(j!=i):
           sum*=l1[j]
    l2.append(sum)
for i in range(0,n):
    print(l2[i],end=' ')