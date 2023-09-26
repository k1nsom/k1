import math
k = eval (input('请输入一个数：'))
zs=int(k)
k=k-zs
print(zs,end='')
print('.',end='')
for i in range(1,100):
    k=k*2
    if(k>=1):
        print(1,end='')
        k-=int(k)


